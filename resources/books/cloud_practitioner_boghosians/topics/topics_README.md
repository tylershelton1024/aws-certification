---
title: Topics Folder
tags: [topics, readme]
updated: 2026-08-10
---

# Topics

Notes and practice questions, organized by chapter of the current study book ("AWS Certified Cloud Practitioner: Understand AWS Like Never Before with Analogies & Real-World Examples" by Rafi Boghosians), not by AWS exam domain directly. Named `topics/` rather than `chapters/` so books and `resources/youtube_channels/` share the exact same structural pattern - each topic's own title still says "Chapter N" where that applies, since that's how the book itself is organized.

Each topic folder is named `NN_topic_title/` and contains these files, split by content type, scope, and role:

- `notes.md` - distilled notes on the book's own core chapter content.
- `deeper_dive_notes.md` - notes on topics that came from questions asked beyond what the book covers directly, kept as a separate file rather than a section within `notes.md`.
- `practice_questions.md` - questions testing retention of `notes.md`, with an answer key at the bottom.
- `deeper_dive_questions.md` - questions testing retention of `deeper_dive_notes.md`, with an answer key at the bottom.
- `flashcards.md` - term/definition flashcards distilled from `notes.md`. Human-readable source of truth for this topic's Core deck.
- `deeper_dive_flashcards.md` - term/definition flashcards distilled from `deeper_dive_notes.md`. Human-readable source of truth for this topic's Deeper Dive deck.

Plus generated files, which should never be hand-edited directly - update the `.md` sources above and regenerate instead:

- `flashcards_data.js` - the single JS data file holding this topic's card data (both decks), generated from `flashcards.md` and `deeper_dive_flashcards.md`. Both `flashcards.html` (this topic) and `../../../../all_flashcards.html` (whole book) load this same file via `<script src="...">`, so card content is never duplicated across HTML files - only this one data file needs to change.
- `flashcards.html` - a self-contained, offline flashcard viewer for this topic (open it directly in a browser). Toggles between the Core and Deeper Dive decks. Contains no card data of its own - it just renders whatever `flashcards_data.js` provides.

This structure is expected to change as studying progresses - topics may get merged, split, or reorganized. See `writing_conventions/overall.md` in personal-ai-profile for the "prefer flexible structure" principle this follows.

## Question and Flashcard Coverage Rules

- **Questions**: for every `##` section heading in `notes.md`/`deeper_dive_notes.md`, the matching `practice_questions.md`/`deeper_dive_questions.md` must have at least 3 questions covering it. Group questions under `###` headings in the questions file matching the notes.md section name exactly - this creates a name-based mapping from question to section (intended for future per-section filtering in the app), independent of any heading *level* differences between the two files (the questions files also use `##` for their own structure - "Core Concepts Questions", "Answer Key" - so `###` is used for section grouping specifically to avoid clashing with that). Count existing questions toward the minimum of 3 before writing new ones - don't duplicate coverage that already exists.
- **Bold-term questions**: every `**bold term**` in a section (excluding structural/label bolding like "**AWS's responsibilities:**" or analogy sentences like "**AWS is the rental car company.**" - only genuine named concepts count) gets its own dedicated question, always in addition to that section's 3-question minimum, not counted toward it. An existing question can satisfy a bold term's requirement if it specifically and substantially tests that term (e.g. a question pairing two bolded terms in contrast can satisfy both terms at once).
- **Flashcards**: every genuine bold term gets exactly one flashcard (1:1 mapping) - no per-section minimum the way questions have. Flashcards are atomic recall aids, not multi-angle testing, so padding out extra near-duplicate cards for the same term doesn't add the same value that multiple question angles do. Periodically audit notes.md/deeper_dive_notes.md's bold terms against flashcards.md/deeper_dive_flashcards.md for gaps.
- **Answer-letter distribution**: never let correct answers cluster on one letter across a question file. After writing or editing any question file, check the actual distribution of correct letters before considering it done - this was found as a real bug once (some files had 60-100% of correct answers landing on B), which would let someone game the quiz by guessing one letter repeatedly.
- **Verification, every time**: after any change to notes/flashcards/questions content, verify all of: (1) ASCII-only via grep, (2) the app's real parser (`load_topic_flashcards`/`load_topic_questions`) actually reads the new content correctly, not just visual review, (3) the full pytest suite still passes, (4) for question files, the answer-letter distribution.
- **Open question, not yet decided**: whether `###` subsections within a `##` section (e.g. Chapter 1's "Service Models" section has IaaS/PaaS/SaaS/Summary as H3 subsections) should trigger their own coverage requirement, separate from the parent section's. Revisit before assuming either way.

## Topics

1. `01_aws_cloud_fundamentals/`
2. `02_aws_global_infrastructure/`
3. `03_aws_accounts_and_billing/`
4. `04_aws_compute_services/`
5. `05_aws_storage_services/`
6. `06_aws_networking_security/`
7. `07_aws_security_and_iam/`
8. `08_aws_monitoring_and_protection/`
9. `09_aws_pricing_and_cost_optimization/`
10. `10_aws_support_and_guidance/`
11. `11_aws_devops_automation/`
12. `12_exploring_aws_in_action/`
