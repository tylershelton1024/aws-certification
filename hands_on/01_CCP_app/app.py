from flask import Flask
import os
import re
import json
import glob
import markdown

app = Flask(__name__)

# This file lives at hands_on/01_CCP_app/app.py - go up 3 levels to reach
# the repo root, then into resources/.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESOURCES_DIR = os.path.join(REPO_ROOT, "resources")


def list_topic_folders():
    """Returns sorted (folder_name, folder_path) pairs for every topic directory,
    across every book under resources/books/ and every channel under
    resources/youtube_channels/. Both share the same <source>/topics/<topic>/
    shape, so one pattern covers both - a new book or channel needs no code
    change here, only a new folder on disk."""
    pattern_books = os.path.join(RESOURCES_DIR, "books", "*", "topics", "*") + os.sep
    pattern_channels = os.path.join(RESOURCES_DIR, "youtube_channels", "*", "topics", "*") + os.sep
    paths = sorted(glob.glob(pattern_books)) + sorted(glob.glob(pattern_channels))
    folders = []
    for path in paths:
        folder_name = os.path.basename(os.path.normpath(path))
        folders.append((folder_name, path))
    return folders


def get_topic_label(folder_path):
    """Reads the topic's notes.md frontmatter title, falling back to the folder name."""
    notes_path = os.path.join(folder_path, "notes.md")
    if os.path.exists(notes_path):
        with open(notes_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r'^title:\s*"?([^"\n]+?)"?\s*$', content, re.MULTILINE)
        if match:
            return match.group(1).replace(" - Notes", "")
    return os.path.basename(os.path.normpath(folder_path))


def load_topic_flashcards(folder_path):
    """Reads flashcards_data.js, strips the 'const <name> = ... ;' wrapper,
    and parses the remainder as JSON. Works because every key in that file
    is already quoted - valid JS and valid JSON at once."""
    data_path = os.path.join(folder_path, "flashcards_data.js")
    if not os.path.exists(data_path):
        return None
    with open(data_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"const\s+\w+\s*=\s*(\{.*\})\s*;?\s*$", content, re.DOTALL)
    if not match:
        return None
    return json.loads(match.group(1))


FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def load_topic_notes_html(folder_path):
    """Reads notes.md and deeper_dive_notes.md, strips the YAML frontmatter
    block, and converts what's left to HTML via the markdown package."""
    result = {"core_html": None, "deeper_html": None}

    notes_path = os.path.join(folder_path, "notes.md")
    if os.path.exists(notes_path):
        with open(notes_path, "r", encoding="utf-8") as f:
            content = FRONTMATTER_RE.sub("", f.read(), count=1)
        result["core_html"] = markdown.markdown(content)

    deeper_path = os.path.join(folder_path, "deeper_dive_notes.md")
    if os.path.exists(deeper_path):
        with open(deeper_path, "r", encoding="utf-8") as f:
            content = FRONTMATTER_RE.sub("", f.read(), count=1)
        result["deeper_html"] = markdown.markdown(content)

    return result


QUESTION_RE = re.compile(
    r"^(\d+)\.\s+(.+?)\n((?:[ \t]*-\s*[A-D]\)\s*.+\n?)+)",
    re.MULTILINE,
)
OPTION_LINE_RE = re.compile(r"([A-D])\)\s*(.+?)\s*$")
ANSWER_RE = re.compile(r"^(\d+)\.\s+([A-D])\s*-\s*(.+?)\s*$", re.MULTILINE)


def _parse_questions_section(content):
    """Parses one questions .md file's body (frontmatter already stripped)
    into a list of question dicts, matching each question to its Answer Key
    entry by number - not by position - so a gap or reorder can't misalign
    them. Anything malformed (no matching answer, wrong option count) is
    skipped rather than raised, since topics are authored incrementally and
    a half-written file (or a '_TBD_' placeholder) must not break the app."""
    questions_part, _, answer_part = content.partition("## Answer Key")

    answers = {}
    for num_str, letter, explanation in ANSWER_RE.findall(answer_part):
        answers[int(num_str)] = (letter, explanation.strip())

    questions = []
    for num_str, stem, options_block in QUESTION_RE.findall(questions_part):
        num = int(num_str)
        options = []
        for line in options_block.splitlines():
            match = OPTION_LINE_RE.search(line.strip())
            if match:
                options.append({"letter": match.group(1), "text": match.group(2)})
        if num not in answers or len(options) != 4:
            continue
        correct, explanation = answers[num]
        questions.append({
            "number": num,
            "question": stem.strip(),
            "options": options,
            "correct": correct,
            "explanation": explanation,
        })

    questions.sort(key=lambda q: q["number"])
    return questions


def load_topic_questions(folder_path):
    """Reads practice_questions.md and deeper_dive_questions.md and parses
    each into a list of question dicts. Always returns {"core": [...],
    "deeper": [...]} - either list is empty (never None, never raises) if
    the file is missing or has no complete question+answer pairs yet."""
    result = {"core": [], "deeper": []}

    core_path = os.path.join(folder_path, "practice_questions.md")
    if os.path.exists(core_path):
        with open(core_path, "r", encoding="utf-8") as f:
            content = FRONTMATTER_RE.sub("", f.read(), count=1)
        result["core"] = _parse_questions_section(content)

    deeper_path = os.path.join(folder_path, "deeper_dive_questions.md")
    if os.path.exists(deeper_path):
        with open(deeper_path, "r", encoding="utf-8") as f:
            content = FRONTMATTER_RE.sub("", f.read(), count=1)
        result["deeper"] = _parse_questions_section(content)

    return result


# ---------------------------------------------------------------------------
# Design system: one shared stylesheet + page shell, used by every route.
# Kept as plain (non f-string) strings on purpose - CSS/JS use lots of real
# braces, and plain strings need zero escaping. Only render_page() below
# does f-string interpolation, and only of whole variables, never raw braces.
# ---------------------------------------------------------------------------

BASE_STYLE = """
:root {
  --bg: #F5F5F7;
  --surface: #FFFFFF;
  --text: #1D1D1F;
  --muted: #6E6E73;
  --border: #D2D2D7;
  --accent: #0071E3;
  --accent-text: #FFFFFF;
  --correct: #34C759;
  --incorrect: #FF3B30;
  --radius: 18px;
  --shadow: 0 1px 3px rgba(0,0,0,0.08), 0 8px 24px rgba(0,0,0,0.06);
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #000000;
    --surface: #1C1C1E;
    --text: #F5F5F7;
    --muted: #98989D;
    --border: #38383A;
    --accent: #0A84FF;
    --accent-text: #FFFFFF;
    --correct: #30D158;
    --incorrect: #FF453A;
    --shadow: 0 1px 3px rgba(0,0,0,0.4), 0 8px 24px rgba(0,0,0,0.3);
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
main {
  max-width: 640px;
  margin: 0 auto;
  padding: 32px 20px 110px;
}
h1 {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 8px 0 4px;
}
.subtitle { color: var(--muted); font-size: 1.05rem; margin: 0 0 28px; }
a { color: var(--accent); }

.back-link {
  display: inline-flex; align-items: center; gap: 4px;
  color: var(--accent); text-decoration: none;
  font-weight: 600; font-size: 0.95rem; margin-bottom: 16px;
}
.back-link svg { width: 18px; height: 18px; }

/* Bottom nav bar - thumb-friendly, always in the same place */
.navbar {
  position: fixed; bottom: 0; left: 0; right: 0;
  display: flex; justify-content: space-around;
  background: var(--surface);
  border-top: 1px solid var(--border);
  padding: 10px 0 calc(10px + env(safe-area-inset-bottom));
  box-shadow: 0 -1px 6px rgba(0,0,0,0.05);
}
.nav-item {
  display: flex; flex-direction: column; align-items: center; gap: 4px;
  text-decoration: none; color: var(--muted);
  font-size: 0.75rem; font-weight: 600;
  min-width: 64px; min-height: 44px; padding: 4px; border-radius: 12px;
}
.nav-item.active { color: var(--accent); }
.nav-item svg { width: 26px; height: 26px; }

/* Big tappable link-cards on the home screen */
.card-link {
  display: flex; align-items: center; gap: 16px;
  background: var(--surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 18px 20px;
  margin-bottom: 14px;
  text-decoration: none;
  color: var(--text);
  min-height: 44px;
}
.card-link .icon-wrap {
  width: 48px; height: 48px; border-radius: 14px;
  background: var(--accent); color: #fff;
  display: flex; align-items: center; justify-content: center;
  flex: none;
}
.card-link .icon-wrap svg { width: 26px; height: 26px; }
.card-link .label { font-size: 1.15rem; font-weight: 600; }
.card-link .desc { font-size: 0.9rem; color: var(--muted); margin-top: 2px; }
.card-link .chevron { margin-left: auto; color: var(--border); flex: none; }

/* Pills - big tappable topic picker instead of a tiny dropdown */
.pill-row { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px; margin-bottom: 20px; -webkit-overflow-scrolling: touch; }
.pill {
  flex: none; padding: 10px 18px; border-radius: 999px;
  background: var(--surface); border: 1px solid var(--border);
  color: var(--text); font-size: 0.95rem; font-weight: 600;
  cursor: pointer; white-space: nowrap; min-height: 44px;
}
.pill.active { background: var(--accent); border-color: var(--accent); color: var(--accent-text); }

/* Segmented control - Core vs Deeper Dive */
.segment { display: flex; background: var(--border); border-radius: 12px; padding: 3px; margin-bottom: 20px; }
.segment button {
  flex: 1; border: none; background: transparent; padding: 10px 0;
  border-radius: 9px; font-size: 0.95rem; font-weight: 600; color: var(--muted);
  cursor: pointer; min-height: 40px;
}
.segment button.active { background: var(--surface); color: var(--text); box-shadow: 0 1px 2px rgba(0,0,0,0.15); }

/* Flip card */
.flip-card {
  background: var(--surface); border-radius: var(--radius); box-shadow: var(--shadow);
  min-height: 220px; display: flex; align-items: center; justify-content: center;
  text-align: center; padding: 32px; cursor: pointer;
  font-size: 1.2rem; font-weight: 600;
  transition: transform 0.12s ease;
}
.flip-card:active { transform: scale(0.98); }
.flip-card.flipped { color: var(--muted); font-weight: 400; font-size: 1.05rem; }
.flip-hint { text-align: center; color: var(--muted); font-size: 0.85rem; margin-top: 10px; }

.big-nav-controls { display: flex; justify-content: center; gap: 20px; margin-top: 20px; align-items: center; }
.round-btn {
  width: 52px; height: 52px; border-radius: 50%; border: none;
  background: var(--surface); box-shadow: var(--shadow); color: var(--text);
  display: flex; align-items: center; justify-content: center; cursor: pointer;
}
.round-btn svg { width: 22px; height: 22px; }
.counter-pill { font-size: 0.9rem; color: var(--muted); font-weight: 600; min-width: 50px; text-align: center; }

/* Rendered notes typography */
.notes-content h1 { font-size: 1.4rem; margin-top: 0; }
.notes-content h2 { font-size: 1.15rem; margin-top: 28px; }
.notes-content h3 { font-size: 1rem; }
.notes-content p, .notes-content li { font-size: 0.98rem; line-height: 1.6; }
.notes-content code { background: var(--border); padding: 2px 6px; border-radius: 5px; font-size: 0.85em; }

/* Practice quiz */
.checklist-row {
  display: flex; align-items: center; gap: 12px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 12px 16px; margin-bottom: 8px;
  cursor: pointer; min-height: 44px; font-size: 0.95rem; font-weight: 600;
}
.checklist-row.checked { border-color: var(--accent); }
.checklist-row .box {
  width: 22px; height: 22px; border-radius: 6px; flex: none;
  border: 2px solid var(--border); display: flex; align-items: center; justify-content: center;
}
.checklist-row.checked .box { background: var(--accent); border-color: var(--accent); color: #fff; }

.score-line { font-size: 0.9rem; color: var(--muted); font-weight: 600; margin-bottom: 12px; }
.question-stem { font-size: 1.05rem; font-weight: 600; line-height: 1.4; margin-bottom: 16px; }

.option-btn {
  display: block; width: 100%; text-align: left;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 14px 16px; margin-bottom: 10px;
  font-size: 0.98rem; color: var(--text); cursor: pointer; min-height: 44px;
}
.option-btn .letter { font-weight: 700; margin-right: 8px; color: var(--muted); }
.option-btn.selected { border-color: var(--accent); border-width: 2px; }
.option-btn.correct { background: rgba(52,199,89,0.15); border-color: var(--correct); }
.option-btn.incorrect { background: rgba(255,59,48,0.15); border-color: var(--incorrect); }

.explanation-box {
  background: var(--surface); border-radius: 12px; padding: 14px 16px;
  margin-bottom: 16px; font-size: 0.92rem; color: var(--muted); line-height: 1.5;
}
.explanation-box .source-label { display: block; font-weight: 700; color: var(--text); margin-bottom: 4px; }

.score-summary { text-align: center; padding: 4px 0 24px; }
.score-summary .big-score { font-size: 2.5rem; font-weight: 700; }

/* Print / export view - hidden on screen, shown only when printing */
.print-only { display: none; }
.print-question { margin-bottom: 14px; page-break-inside: avoid; }
.print-question .opt { margin-left: 16px; }
@media print {
  .navbar, .segment, .pill-row, #chapterChecklist, .big-nav-controls,
  #submitBtn, #retakeBtn, #printBtn, #csvBtn, #quizArea, .back-link, .subtitle { display: none !important; }
  .print-only { display: block !important; }
  body { background: #fff; color: #000; }
  main { max-width: 100%; padding: 0; }
}
"""

ICON_HOME = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"/><path d="M5 10v10a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V10"/></svg>'
ICON_CARDS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="7" width="14" height="10" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2"/></svg>'
ICON_NOTES = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2h9l5 5v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z"/><path d="M14 2v6h6"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="13" y2="17"/></svg>'
ICON_PRACTICE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 3v2a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1V3"/><polyline points="9 13 11 15 15 11"/></svg>'
ICON_CHEVRON_LEFT_SMALL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18"><polyline points="15 18 9 12 15 6"/></svg>'
ICON_CHEVRON_RIGHT_SMALL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="18" height="18"><polyline points="9 18 15 12 9 6"/></svg>'
ICON_CHEVRON_LEFT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>'
ICON_CHEVRON_RIGHT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>'


def render_nav(active):
    def item(href, icon, label, key):
        cls = "nav-item active" if key == active else "nav-item"
        return f'<a class="{cls}" href="{href}">{icon}<span>{label}</span></a>'

    return (
        '<nav class="navbar">'
        + item("/", ICON_HOME, "Home", "home")
        + item("/flashcards", ICON_CARDS, "Flashcards", "flashcards")
        + item("/notes", ICON_NOTES, "Notes", "notes")
        + item("/practice", ICON_PRACTICE, "Practice", "practice")
        + "</nav>"
    )


def render_page(title, active, body_html, extra_script=""):
    """Assembles one full HTML page: shared style + shared bottom nav +
    whatever this specific page's body/script are. Every route builds a
    body_html string and calls this instead of writing its own <html>."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - CCP Study</title>
<style>{BASE_STYLE}</style>
</head>
<body>
<main>
{body_html}
</main>
{render_nav(active)}
<script src="/static/shared.js"></script>
<script>{extra_script}</script>
</body>
</html>"""


@app.route("/")
def index():
    body = f"""
<h1>CCP Study</h1>
<p class="subtitle">Your AWS Cloud Practitioner companion.</p>

<a class="card-link" href="/flashcards">
    <span class="icon-wrap">{ICON_CARDS}</span>
    <span>
        <div class="label">Flashcards</div>
        <div class="desc">Quiz yourself, one term at a time</div>
    </span>
    <span class="chevron">{ICON_CHEVRON_RIGHT_SMALL}</span>
</a>

<a class="card-link" href="/notes">
    <span class="icon-wrap">{ICON_NOTES}</span>
    <span>
        <div class="label">Notes</div>
        <div class="desc">Everything you've learned, organized</div>
    </span>
    <span class="chevron">{ICON_CHEVRON_RIGHT_SMALL}</span>
</a>

<a class="card-link" href="/practice">
    <span class="icon-wrap">{ICON_PRACTICE}</span>
    <span>
        <div class="label">Practice</div>
        <div class="desc">Test yourself and see your score</div>
    </span>
    <span class="chevron">{ICON_CHEVRON_RIGHT_SMALL}</span>
</a>
"""
    return render_page("Home", "home", body)


FLASHCARDS_SCRIPT = """
const topics = __TOPICS_JSON__;
let currentTopic = Object.keys(topics)[0];
let currentDeck = "core";
let index = 0;
let flipped = false;
let activeCards = [];

const pillRow = document.getElementById("pillRow");
const cardEl = document.getElementById("card");
const counterEl = document.getElementById("counter");
const segButtons = document.querySelectorAll(".segment button");

function buildActiveCards() {
    const topic = topics[currentTopic];
    activeCards = topic ? shuffleArray(combineDecks(topic, currentDeck)) : [];
}

function resetProgress() {
    index = 0;
    flipped = false;
    buildActiveCards();
}

function renderPills() {
    pillRow.innerHTML = "";
    Object.keys(topics).forEach(key => {
        const btn = document.createElement("button");
        btn.className = "pill" + (key === currentTopic ? " active" : "");
        btn.textContent = topics[key].label;
        btn.addEventListener("click", () => {
            currentTopic = key;
            resetProgress();
            renderPills(); render();
        });
        pillRow.appendChild(btn);
    });
}

function currentCards() {
    return activeCards;
}

function render() {
    const cards = currentCards();
    if (!cards || cards.length === 0) {
        cardEl.textContent = "No cards yet";
        counterEl.textContent = "";
        return;
    }
    const item = cards[index];
    cardEl.textContent = flipped ? item.definition : item.term;
    cardEl.classList.toggle("flipped", flipped);
    counterEl.textContent = (index + 1) + " / " + cards.length;
}

cardEl.addEventListener("click", () => { flipped = !flipped; render(); });

document.getElementById("prevBtn").addEventListener("click", () => {
    const cards = currentCards();
    if (cards && cards.length) { index = (index - 1 + cards.length) % cards.length; flipped = false; render(); }
});
document.getElementById("nextBtn").addEventListener("click", () => {
    const cards = currentCards();
    if (cards && cards.length) { index = (index + 1) % cards.length; flipped = false; render(); }
});

segButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        segButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentDeck = btn.dataset.deck;
        resetProgress();
        render();
    });
});

renderPills();
resetProgress();
render();
"""


@app.route("/flashcards")
def flashcards_page():
    topics = {}
    for folder_name, folder_path in list_topic_folders():
        decks = load_topic_flashcards(folder_path)
        if decks is None:
            continue
        topics[folder_name] = {
            "label": get_topic_label(folder_path),
            "core": decks.get("core", []),
            "deeper": decks.get("deeper", []),
        }
    script = FLASHCARDS_SCRIPT.replace("__TOPICS_JSON__", json.dumps(topics))

    body = f"""
<a class="back-link" href="/">{ICON_CHEVRON_LEFT_SMALL} Home</a>
<h1>Flashcards</h1>
<p class="subtitle">Tap a card to flip it.</p>

<div class="pill-row" id="pillRow"></div>

<div class="segment">
    <button class="active" data-deck="core">Core</button>
    <button data-deck="deeper">Deeper Dive</button>
    <button data-deck="both">Both</button>
</div>

<div class="flip-card" id="card"></div>
<p class="flip-hint">Tap the card to see the answer</p>

<div class="big-nav-controls">
    <button class="round-btn" id="prevBtn">{ICON_CHEVRON_LEFT}</button>
    <span class="counter-pill" id="counter"></span>
    <button class="round-btn" id="nextBtn">{ICON_CHEVRON_RIGHT}</button>
</div>
"""
    return render_page("Flashcards", "flashcards", body, extra_script=script)


NOTES_SCRIPT = """
const topics = __TOPICS_JSON__;
let currentTopic = Object.keys(topics)[0];
let currentPart = "core_html";

const pillRow = document.getElementById("pillRow");
const notesBody = document.getElementById("notesBody");
const segButtons = document.querySelectorAll(".segment button");

function renderPills() {
    pillRow.innerHTML = "";
    Object.keys(topics).forEach(key => {
        const btn = document.createElement("button");
        btn.className = "pill" + (key === currentTopic ? " active" : "");
        btn.textContent = topics[key].label;
        btn.addEventListener("click", () => {
            currentTopic = key;
            renderPills(); render();
        });
        pillRow.appendChild(btn);
    });
}

function render() {
    notesBody.innerHTML = topics[currentTopic][currentPart];
}

segButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        segButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentPart = btn.dataset.part;
        render();
    });
});

renderPills();
render();
"""


@app.route("/notes")
def notes_page():
    topics = {}
    for folder_name, folder_path in list_topic_folders():
        html = load_topic_notes_html(folder_path)
        if html["core_html"] is None and html["deeper_html"] is None:
            continue
        topics[folder_name] = {
            "label": get_topic_label(folder_path),
            "core_html": html["core_html"] or "<p><em>No core notes yet.</em></p>",
            "deeper_html": html["deeper_html"] or "<p><em>No deeper dive notes yet.</em></p>",
        }
    script = NOTES_SCRIPT.replace("__TOPICS_JSON__", json.dumps(topics))

    body = f"""
<a class="back-link" href="/">{ICON_CHEVRON_LEFT_SMALL} Home</a>
<h1>Notes</h1>
<p class="subtitle">Everything you've learned, organized by topic.</p>

<div class="pill-row" id="pillRow"></div>

<div class="segment">
    <button class="active" data-part="core_html">Core Notes</button>
    <button data-part="deeper_html">Deeper Dive</button>
</div>

<div class="notes-content" id="notesBody"></div>
"""
    return render_page("Notes", "notes", body, extra_script=script)


PRACTICE_SCRIPT = """
const topics = __TOPICS_JSON__;
const topicKeys = Object.keys(topics);
let currentScope = "single";
let currentTopic = topicKeys[0];
let checkedTopics = new Set(topicKeys);
let currentDeck = "core";
let currentMode = "immediate";
let index = 0;
let answers = {};
let examSubmitted = false;

const pillRow = document.getElementById("pillRow");
const chapterChecklist = document.getElementById("chapterChecklist");
const quizArea = document.getElementById("quizArea");
const counterEl = document.getElementById("counter");
const navControls = document.getElementById("navControls");
const submitBtn = document.getElementById("submitBtn");
const retakeBtn = document.getElementById("retakeBtn");
const printBtn = document.getElementById("printBtn");
const csvBtn = document.getElementById("csvBtn");
const printView = document.getElementById("printView");
const scopeButtons = document.querySelectorAll("#scopeSegment button");
const deckButtons = document.querySelectorAll("#deckSegment button");
const modeButtons = document.querySelectorAll("#modeSegment button");

let activeQuestions = [];

function computeQuestions() {
    if (currentScope === "single") {
        const topic = topics[currentTopic];
        return topic ? combineDecks(topic, currentDeck) : [];
    }
    let combined = [];
    topicKeys.forEach(key => {
        if (checkedTopics.has(key)) {
            combineDecks(topics[key], currentDeck).forEach(q => {
                combined.push(Object.assign({}, q, { sourceLabel: topics[key].label }));
            });
        }
    });
    return combined;
}

function buildActiveQuestions() {
    const shuffled = shuffleArray(computeQuestions()).map(q =>
        Object.assign({}, q, { options: shuffleArray(q.options) })
    );
    activeQuestions = shuffled;
}

function resetProgress() {
    index = 0;
    answers = {};
    examSubmitted = false;
    buildActiveQuestions();
}

function renderPills() {
    pillRow.innerHTML = "";
    topicKeys.forEach(key => {
        const btn = document.createElement("button");
        btn.className = "pill" + (key === currentTopic ? " active" : "");
        btn.textContent = topics[key].label;
        btn.addEventListener("click", () => {
            currentTopic = key;
            resetProgress();
            renderPills();
            render();
        });
        pillRow.appendChild(btn);
    });
}

function renderChecklist() {
    chapterChecklist.innerHTML = "";
    topicKeys.forEach(key => {
        const row = document.createElement("div");
        const isChecked = checkedTopics.has(key);
        row.className = "checklist-row" + (isChecked ? " checked" : "");
        row.innerHTML = `<span class="box"></span><span>${topics[key].label}</span>`;
        row.addEventListener("click", () => {
            if (checkedTopics.has(key)) {
                checkedTopics.delete(key);
            } else {
                checkedTopics.add(key);
            }
            resetProgress();
            renderChecklist();
            render();
        });
        chapterChecklist.appendChild(row);
    });
}

function currentQuestions() {
    return activeQuestions;
}

function optionBtnHtml(opt, state) {
    return `<button class="option-btn ${state}" data-letter="${opt.letter}">
        <span class="letter">${opt.letter}</span>${opt.text}</button>`;
}

function renderPrintView(questions) {
    if (!questions || questions.length === 0) {
        printView.innerHTML = "";
        return;
    }
    const itemsHtml = questions.map((q, i) => {
        const optsHtml = q.options.map(opt =>
            `<div class="opt">${opt.letter}) ${opt.text}</div>`
        ).join("");
        const sourceText = q.sourceLabel ? ` (${q.sourceLabel})` : "";
        return `<div class="print-question">
            <div><strong>${i + 1}. ${q.question}</strong>${sourceText}</div>
            ${optsHtml}
        </div>`;
    }).join("");
    const keyHtml = questions.map((q, i) =>
        `<div>${i + 1}. ${q.correct} - ${q.explanation}</div>`
    ).join("");

    printView.innerHTML = `
        <h1>Practice Questions</h1>
        ${itemsHtml}
        <h2>Answer Key</h2>
        ${keyHtml}
    `;
}

function csvEscape(value) {
    const s = String(value);
    if (/[",\\r\\n]/.test(s)) {
        return '"' + s.replace(/"/g, '""') + '"';
    }
    return s;
}

function questionsToCsv(questions) {
    const header = ["number", "source_chapter", "question", "option_a", "option_b", "option_c", "option_d", "correct_answer", "explanation"];
    const rows = questions.map(q => {
        const byLetter = {};
        q.options.forEach(opt => { byLetter[opt.letter] = opt.text; });
        return [
            q.number,
            q.sourceLabel || "",
            q.question,
            byLetter.A || "",
            byLetter.B || "",
            byLetter.C || "",
            byLetter.D || "",
            q.correct,
            q.explanation,
        ];
    });
    return [header, ...rows].map(row => row.map(csvEscape).join(",")).join("\\r\\n");
}

function downloadCsv() {
    const questions = currentQuestions();
    if (!questions || questions.length === 0) { return; }
    const csv = questionsToCsv(questions);
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "practice_questions.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function render() {
    const questions = currentQuestions();
    renderPrintView(questions);
    navControls.style.display = "flex";
    submitBtn.style.display = "none";
    retakeBtn.style.display = "none";

    if (!questions || questions.length === 0) {
        navControls.style.display = "none";
        quizArea.innerHTML = '<p class="flip-hint">No questions yet for this selection.</p>';
        return;
    }
    if (currentMode === "exam" && examSubmitted) {
        navControls.style.display = "none";
        renderReview(questions);
        return;
    }
    counterEl.textContent = (index + 1) + " / " + questions.length;
    if (currentMode === "exam") {
        renderExamQuestion(questions);
    } else {
        renderImmediateQuestion(questions);
    }
}

function renderImmediateQuestion(questions) {
    const q = questions[index];
    const picked = answers[index];
    const optsHtml = q.options.map(opt => {
        let state = "";
        if (picked) {
            if (opt.letter === q.correct) { state = "correct"; }
            else if (opt.letter === picked) { state = "incorrect"; }
        }
        return optionBtnHtml(opt, state);
    }).join("");
    const answeredIdx = Object.keys(answers).map(Number);
    const correctCount = answeredIdx.filter(i => answers[i] === questions[i].correct).length;
    const explanationHtml = picked
        ? `<div class="explanation-box"><strong>${picked === q.correct ? "Correct." : "Not quite."}</strong> ${q.explanation}</div>`
        : "";
    const sourceHtml = q.sourceLabel ? `<p class="score-line">${q.sourceLabel}</p>` : "";

    quizArea.innerHTML = `
        <p class="score-line">Score: ${correctCount} / ${answeredIdx.length}</p>
        ${sourceHtml}
        <div class="question-stem">${q.question}</div>
        ${optsHtml}
        ${explanationHtml}
    `;
    if (!picked) {
        quizArea.querySelectorAll(".option-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                answers[index] = btn.dataset.letter;
                render();
            });
        });
    }
}

function renderExamQuestion(questions) {
    const q = questions[index];
    const picked = answers[index];
    const optsHtml = q.options.map(opt =>
        optionBtnHtml(opt, opt.letter === picked ? "selected" : "")
    ).join("");
    const answeredCount = Object.keys(answers).length;
    const sourceHtml = q.sourceLabel ? `<p class="score-line">${q.sourceLabel}</p>` : "";

    quizArea.innerHTML = `
        <p class="score-line">Answered: ${answeredCount} / ${questions.length}</p>
        ${sourceHtml}
        <div class="question-stem">${q.question}</div>
        ${optsHtml}
    `;
    quizArea.querySelectorAll(".option-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            answers[index] = btn.dataset.letter;
            render();
        });
    });
    submitBtn.style.display = "block";
}

function renderReview(questions) {
    const correctCount = questions.filter((q, i) => answers[i] === q.correct).length;
    const itemsHtml = questions.map((q, i) => {
        const picked = answers[i];
        const optsHtml = q.options.map(opt => {
            let state = "";
            if (opt.letter === q.correct) { state = "correct"; }
            else if (opt.letter === picked) { state = "incorrect"; }
            return optionBtnHtml(opt, state);
        }).join("");
        const sourceHtml = q.sourceLabel
            ? `<div class="explanation-box"><span class="source-label">${q.sourceLabel}</span>${q.explanation}</div>`
            : `<div class="explanation-box">${q.explanation}</div>`;
        return `<div class="question-stem">${i + 1}. ${q.question}</div>${optsHtml}${sourceHtml}`;
    }).join("");

    quizArea.innerHTML = `
        <div class="score-summary">
            <div class="big-score">${correctCount} / ${questions.length}</div>
            <p class="subtitle">correct</p>
        </div>
        ${itemsHtml}
    `;
    retakeBtn.style.display = "block";
}

document.getElementById("prevBtn").addEventListener("click", () => {
    const n = currentQuestions().length;
    if (n) { index = (index - 1 + n) % n; render(); }
});
document.getElementById("nextBtn").addEventListener("click", () => {
    const n = currentQuestions().length;
    if (n) { index = (index + 1) % n; render(); }
});
submitBtn.addEventListener("click", () => { examSubmitted = true; render(); });
retakeBtn.addEventListener("click", () => { resetProgress(); render(); });
printBtn.addEventListener("click", () => { window.print(); });
csvBtn.addEventListener("click", () => { downloadCsv(); });

scopeButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        scopeButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentScope = btn.dataset.scope;
        pillRow.style.display = currentScope === "single" ? "flex" : "none";
        chapterChecklist.style.display = currentScope === "cumulative" ? "block" : "none";
        resetProgress();
        render();
    });
});
deckButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        deckButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentDeck = btn.dataset.deck;
        resetProgress();
        render();
    });
});
modeButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        modeButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentMode = btn.dataset.mode;
        resetProgress();
        render();
    });
});

renderPills();
renderChecklist();
resetProgress();
render();
"""


@app.route("/practice")
def practice_page():
    topics = {}
    for folder_name, folder_path in list_topic_folders():
        decks = load_topic_questions(folder_path)
        if not decks["core"] and not decks["deeper"]:
            continue
        topics[folder_name] = {
            "label": get_topic_label(folder_path),
            "core": decks["core"],
            "deeper": decks["deeper"],
        }
    script = PRACTICE_SCRIPT.replace("__TOPICS_JSON__", json.dumps(topics))

    body = f"""
<a class="back-link" href="/">{ICON_CHEVRON_LEFT_SMALL} Home</a>
<h1>Practice</h1>
<p class="subtitle">Test yourself with practice questions.</p>

<div class="segment" id="scopeSegment">
    <button class="active" data-scope="single">Single Chapter</button>
    <button data-scope="cumulative">Cumulative</button>
</div>

<div class="pill-row" id="pillRow"></div>
<div id="chapterChecklist" style="display:none;margin-bottom:20px;"></div>

<div class="segment" id="deckSegment">
    <button class="active" data-deck="core">Core</button>
    <button data-deck="deeper">Deeper Dive</button>
    <button data-deck="both">Both</button>
</div>

<div class="segment" id="modeSegment">
    <button class="active" data-mode="immediate">Immediate</button>
    <button data-mode="exam">Exam</button>
</div>

<div id="quizArea"></div>

<div class="big-nav-controls" id="navControls">
    <button class="round-btn" id="prevBtn">{ICON_CHEVRON_LEFT}</button>
    <span class="counter-pill" id="counter"></span>
    <button class="round-btn" id="nextBtn">{ICON_CHEVRON_RIGHT}</button>
</div>

<button class="pill" id="submitBtn" style="display:none;width:100%;margin-top:16px;">Submit Quiz</button>
<button class="pill" id="retakeBtn" style="display:none;width:100%;margin-top:16px;">Retake Quiz</button>
<button class="pill" id="printBtn" style="width:100%;margin-top:16px;">Print / Save PDF</button>
<button class="pill" id="csvBtn" style="width:100%;margin-top:10px;">Export CSV (for AI review)</button>

<div class="print-only" id="printView"></div>
"""
    return render_page("Practice", "practice", body, extra_script=script)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
