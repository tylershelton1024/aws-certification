---
title: Resources Folder
tags: [resources, readme]
updated: 2026-08-10
---

# Resources

Every study source, and the actual structured content built from each one.

## Contents

- `resources_overview.md` - a simple list of the books/courses/channels currently in use.
- `books/` - book-based content. Each book has a `topics/` folder, one subfolder per chapter (a book's chapters are treated as topics for structural consistency with `youtube_channels/`, while still being labeled "Chapter N" in each topic's own title).
- `youtube_channels/` - channel-based content, structured the same way (`topics/` per channel), for when video sources get used.

Both `books/` and `youtube_channels/` share the same shape on purpose: a source folder containing a `topics/` folder, each topic containing the same six-file pattern (notes, deeper-dive notes, questions, deeper-dive questions, flashcards, deeper-dive flashcards, plus generated flashcard files). That's what lets a single discovery pattern in `hands_on/01_CCP_app/app.py` find content from any source type without needing source-specific code.
