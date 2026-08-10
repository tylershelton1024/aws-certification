---
title: "Hands-On 01: CCP App"
tags: [hands_on, ec2, vpc, flask, ccp_app]
updated: 2026-08-09
---

# Hands-On 01: CCP App

A small dynamic Flask app deployed on an EC2 instance inside a custom VPC. Ties back to Chapter 1's `notes.md` (IaaS, EC2) and `deeper_dive_notes.md` (virtualization, VPC/subnets/security groups).

## What it does

- `/` - shows the current server time (proves the page is server-rendered, not static), EC2 instance metadata (instance ID, availability zone, instance type) pulled from AWS's instance metadata service, and an in-memory visit counter. No database yet - deliberately deferred to a future project tied to a storage/database chapter.
- `/flashcards` - a chapter/channel-selector flashcard viewer, discovering every topic under `resources/books/*/topics/*/` and `resources/youtube_channels/*/topics/*/` automatically (`list_topic_folders()`), reading each one's `flashcards_data.js` directly - no duplicated card data, same file the static HTML viewers use.
- `/notes` - the same topic discovery, rendering each topic's `notes.md`/`deeper_dive_notes.md` as real HTML via the `markdown` package, with a Core/Deeper Dive toggle.

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
