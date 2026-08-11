"""Tests for the parsing/discovery helpers in app.py.

Run with: pip install -r requirements-dev.txt && pytest

These are isolated unit tests - each one builds a small fake resources/
tree with pytest's tmp_path fixture instead of touching the real repo, so
they stay fast and don't depend on actual chapter content existing.
"""

import pytest

import app as app_module


def _write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@pytest.fixture
def fake_resources(tmp_path, monkeypatch):
    """Points the app at a fake resources/ tree instead of the real repo."""
    resources_dir = tmp_path / "resources"
    monkeypatch.setattr(app_module, "RESOURCES_DIR", str(resources_dir))
    return resources_dir


class TestListTopicFolders:
    def test_finds_book_topics(self, fake_resources):
        topic_dir = fake_resources / "books" / "some_book" / "topics" / "01_intro"
        _write(topic_dir / "notes.md", "# Intro")

        folders = app_module.list_topic_folders()

        assert len(folders) == 1
        assert folders[0][0] == "01_intro"

    def test_finds_channel_topics(self, fake_resources):
        topic_dir = fake_resources / "youtube_channels" / "some_channel" / "topics" / "01_video"
        _write(topic_dir / "notes.md", "# Video notes")

        folders = app_module.list_topic_folders()

        assert len(folders) == 1
        assert folders[0][0] == "01_video"

    def test_combines_and_sorts_both_sources(self, fake_resources):
        _write(fake_resources / "books" / "book_a" / "topics" / "02_second" / "notes.md", "x")
        _write(fake_resources / "books" / "book_a" / "topics" / "01_first" / "notes.md", "x")

        folders = app_module.list_topic_folders()
        names = [name for name, _ in folders]

        assert names == ["01_first", "02_second"]

    def test_empty_when_nothing_exists(self, fake_resources):
        assert app_module.list_topic_folders() == []


class TestGetTopicLabel:
    def test_reads_frontmatter_title(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "notes.md", '---\ntitle: "Chapter 1: Something - Notes"\n---\n\n# Body\n')

        label = app_module.get_topic_label(str(topic_dir))

        assert label == "Chapter 1: Something"

    def test_falls_back_to_folder_name_when_no_notes_file(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        topic_dir.mkdir()

        label = app_module.get_topic_label(str(topic_dir))

        assert label == "01_intro"

    def test_falls_back_to_folder_name_when_no_title_line(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "notes.md", "# Just a heading, no frontmatter\n")

        label = app_module.get_topic_label(str(topic_dir))

        assert label == "01_intro"


class TestLoadTopicFlashcards:
    def test_parses_valid_data_file(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "flashcards_data.js", (
            'const chapter01Decks = {\n'
            '  "core": [{ "term": "A", "definition": "B" }],\n'
            '  "deeper": []\n'
            '};\n'
        ))

        decks = app_module.load_topic_flashcards(str(topic_dir))

        assert decks == {"core": [{"term": "A", "definition": "B"}], "deeper": []}

    def test_returns_none_when_file_missing(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        topic_dir.mkdir()

        assert app_module.load_topic_flashcards(str(topic_dir)) is None

    def test_works_regardless_of_variable_name(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "flashcards_data.js", (
            'const someDifferentName = {"core": [], "deeper": []};\n'
        ))

        decks = app_module.load_topic_flashcards(str(topic_dir))

        assert decks == {"core": [], "deeper": []}


class TestLoadTopicNotesHtml:
    def test_strips_frontmatter_and_converts_markdown(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "notes.md", '---\ntitle: "X"\n---\n\n# Heading\n\nSome text.\n')

        result = app_module.load_topic_notes_html(str(topic_dir))

        assert "<h1>Heading</h1>" in result["core_html"]
        assert "---" not in result["core_html"]
        assert "title:" not in result["core_html"]

    def test_deeper_dive_is_none_when_file_missing(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "notes.md", "# Just core\n")

        result = app_module.load_topic_notes_html(str(topic_dir))

        assert result["core_html"] is not None
        assert result["deeper_html"] is None


class TestLoadTopicQuestions:
    def test_returns_empty_lists_when_files_missing(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        topic_dir.mkdir()

        result = app_module.load_topic_questions(str(topic_dir))

        assert result == {"core": [], "deeper": []}

    def test_returns_empty_core_list_for_tbd_placeholder(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "practice_questions.md", (
            '---\n'
            'title: "Chapter 2: AWS Global Infrastructure - Practice Questions"\n'
            'tags: [chapter_02, global_infrastructure, practice_questions]\n'
            'updated: 2026-08-09\n'
            '---\n\n'
            '# Chapter 2: AWS Global Infrastructure - Practice Questions\n\n'
            '_TBD_\n'
        ))

        result = app_module.load_topic_questions(str(topic_dir))

        assert result["core"] == []

    def test_parses_valid_practice_questions_and_matches_by_number(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "practice_questions.md", (
            '---\ntitle: "X"\n---\n\n'
            '# X\n\n'
            '## Core Concepts Questions\n\n'
            '1. What is elasticity?\n'
            '   - A) Fixed pricing\n'
            '   - B) Scale to demand\n'
            '   - C) Manual hardware ordering\n'
            '   - D) No internet needed\n\n'
            '3. What is IaaS?\n'
            '   - A) Managed platform\n'
            '   - B) End-user software\n'
            '   - C) Raw infrastructure you configure\n'
            '   - D) A database service\n\n'
            '## Answer Key\n\n'
            '1. B - Elasticity means scaling to demand.\n'
            '3. C - IaaS gives raw infrastructure control.\n'
        ))

        core = app_module.load_topic_questions(str(topic_dir))["core"]

        assert len(core) == 2
        assert core[0]["number"] == 1
        assert core[0]["question"] == "What is elasticity?"
        assert core[0]["options"] == [
            {"letter": "A", "text": "Fixed pricing"},
            {"letter": "B", "text": "Scale to demand"},
            {"letter": "C", "text": "Manual hardware ordering"},
            {"letter": "D", "text": "No internet needed"},
        ]
        assert core[0]["correct"] == "B"
        assert core[0]["explanation"] == "Elasticity means scaling to demand."
        assert core[1]["number"] == 3
        assert core[1]["correct"] == "C"

    def test_deeper_dive_questions_parsed_independently_from_core(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "practice_questions.md", (
            '---\ntitle: "X"\n---\n\n# X\n\n## Core Concepts Questions\n\n'
            '1. Core question?\n'
            '   - A) a\n   - B) b\n   - C) c\n   - D) d\n\n'
            '## Answer Key\n\n1. A - core explanation\n'
        ))
        _write(topic_dir / "deeper_dive_questions.md", (
            '---\ntitle: "X Deeper"\n---\n\n# X Deeper\n\n## Questions\n\n'
            '1. Deeper question?\n'
            '   - A) w\n   - B) x\n   - C) y\n   - D) z\n\n'
            '## Answer Key\n\n1. D - deeper explanation\n'
        ))

        result = app_module.load_topic_questions(str(topic_dir))

        assert len(result["core"]) == 1
        assert result["core"][0]["question"] == "Core question?"
        assert len(result["deeper"]) == 1
        assert result["deeper"][0]["question"] == "Deeper question?"

    def test_handles_four_space_indented_options(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "deeper_dive_questions.md", (
            '---\ntitle: "X"\n---\n\n# X\n\n## Questions\n\n'
            '11. What does permission denied mean?\n'
            '    - A) Network failed\n'
            '    - B) Instance not running\n'
            '    - C) Key was rejected\n'
            '    - D) Security group blocked\n\n'
            '## Answer Key\n\n11. C - The connection worked, the key was rejected.\n'
        ))

        deeper = app_module.load_topic_questions(str(topic_dir))["deeper"]

        assert len(deeper) == 1
        assert deeper[0]["number"] == 11
        assert len(deeper[0]["options"]) == 4
        assert deeper[0]["options"][2] == {"letter": "C", "text": "Key was rejected"}

    def test_skips_question_with_no_matching_answer_key_entry(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "practice_questions.md", (
            '---\ntitle: "X"\n---\n\n# X\n\n## Core Concepts Questions\n\n'
            '1. Orphan question?\n'
            '   - A) a\n   - B) b\n   - C) c\n   - D) d\n\n'
            '## Answer Key\n\n'
        ))

        result = app_module.load_topic_questions(str(topic_dir))

        assert result["core"] == []

    def test_skips_question_with_malformed_option_count(self, tmp_path):
        topic_dir = tmp_path / "01_intro"
        _write(topic_dir / "practice_questions.md", (
            '---\ntitle: "X"\n---\n\n# X\n\n## Core Concepts Questions\n\n'
            '1. Incomplete question?\n'
            '   - A) a\n   - B) b\n   - C) c\n\n'
            '## Answer Key\n\n1. A - explanation\n'
        ))

        result = app_module.load_topic_questions(str(topic_dir))

        assert result["core"] == []
