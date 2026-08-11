---
title: Hands-On Folder
tags: [hands_on, readme]
updated: 2026-08-10
---

# Hands-On

Real, deployed AWS work - not just notes and practice questions. Each entry is something actually built and run on a real AWS account, tied back to whichever chapter(s) it reinforces.

Each entry is a folder named `NN_short_name/`, numbered in the order it was built (not tied to chapter numbers - hands-on projects happen when they happen, not strictly in book order). A short cross-reference line gets added to the relevant chapter's `notes.md` pointing back here.

**Security note:** no account IDs, access keys, secrets, or other credential material ever go in this folder (or anywhere in this repo) - see `personal-ai-profile/security/rules_for_sharing_information.md`. SSH key pairs (`.pem` files) are saved locally, outside the repo, and are excluded via `.gitignore`.

## Entries

- `00_account_setup/` - AWS account creation, root MFA, IAM user, and billing alarm setup. Ties to Chapter 3 (AWS Accounts and Billing).
- `01_CCP_app/` - a small dynamic Flask app deployed on an EC2 instance inside a custom VPC, growing into a real study tool: `/flashcards`, `/notes`, and `/practice` (interactive quiz, Single Chapter or Cumulative, Immediate or Exam mode) all discover and serve content from every topic across `resources/books/` and `resources/youtube_channels/` automatically. Ties to Chapter 1 (AWS Cloud Fundamentals) - IaaS, virtualization, and the VPC/security-group Deeper Dive material.
