---
title: "Hands-On 01: CCP App"
tags: [hands_on, ec2, vpc, flask, ccp_app]
updated: 2026-08-10
---

# Hands-On 01: CCP App

A small dynamic Flask app deployed on an EC2 instance inside a custom VPC. Ties back to Chapter 1's `notes.md` (IaaS, EC2) and `deeper_dive_notes.md` (virtualization, VPC/subnets/security groups).

## What it does

- `/` - three feature cards (Flashcards, Notes, Practice). Previously showed EC2 instance metadata and a visit counter as a "this is really server-rendered" demo; removed once the app had real content to show instead.
- `/flashcards` - a topic-selector flashcard viewer, discovering every topic under `resources/books/*/topics/*/` and `resources/youtube_channels/*/topics/*/` automatically (`list_topic_folders()`), reading each one's `flashcards_data.js` directly - no duplicated card data, same file the static HTML viewers use. Core / Deeper Dive / Both toggle; card order shuffles fresh each time you pick a topic or switch decks.
- `/notes` - the same topic discovery, rendering each topic's `notes.md`/`deeper_dive_notes.md` as real HTML via the `markdown` package, with a Core/Deeper Dive toggle.
- `/practice` (Phase 2) - an interactive practice quiz built from each topic's `practice_questions.md`/`deeper_dive_questions.md` (`load_topic_questions()` parses the Markdown directly - no separate question data file). Single Chapter or Cumulative (pick any combination of chapters via checkboxes) scope; Core / Deeper Dive / Both deck; Immediate (instant feedback per question) or Exam (answer everything, then submit and review) mode. Question order and each question's answer-option order shuffle fresh on every attempt. No progress is saved anywhere - that's Phase 3, not built yet. Includes a "Print / Save PDF" button (browser print, for reading/cross-checking by eye) and a separate "Export CSV" button (structured data, meant for handing to another AI model to check the question/answer content) - both scoped to whatever's currently selected on screen.

`static/shared.js` holds the `shuffleArray()`/`combineDecks()` helpers shared by the Flashcards and Practice scripts, loaded once via `<script src="/static/shared.js">` in the shared page shell - avoids each page redefining the same logic.

## Infrastructure

- Custom VPC with a public subnet, route table, and internet gateway.
- Security group: inbound HTTP open, inbound SSH restricted to one IP only (not open to the world).
- One EC2 instance (t3.micro or t2.micro, free-tier-eligible family), Amazon Linux 2023.
- An EC2 User Data script (`user_data.sh`) clones the `aws-certification` repo onto the instance and runs `app.py` directly from that checkout - so new topics/books/channels become available to the deployed app after a `git pull` + service restart, with no code changes needed.

## Known simplifications (being upfront about these, not hiding them)

- Updating the deployed app requires SSHing in, `git pull` inside `/opt/aws-certification`, then `systemctl restart hands-on-app`. No CI/CD - manual, on purpose, appropriate for a small learning project.
- The app runs via Flask's built-in development server (`app.run()`), which AWS/Flask itself doesn't recommend for production use. A more production-correct setup would sit it behind Gunicorn and Nginx. Kept simple on purpose for this first build.
- The systemd service runs the app as `root` so it can bind to port 80 without extra configuration. Not a security best practice for a real production app, but reasonable for a short-lived learning exercise.
- `user_data.sh` assumes the `aws-certification` GitHub repo is public (no credentials needed to clone). If it's ever made private, this needs a deploy key or similar.

## Security

The EC2 key pair (`.pem` file) created for SSH access is stored locally, outside this repo, and is excluded via `.gitignore`. No account IDs, access keys, or other credential material appear anywhere in this project.
