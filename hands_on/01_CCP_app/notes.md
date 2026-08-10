---
title: "Hands-On 01: CCP App"
tags: [hands_on, ec2, vpc, flask, ccp_app]
updated: 2026-08-09
---

# Hands-On 01: CCP App

A small dynamic Flask app deployed on an EC2 instance inside a custom VPC. Ties back to Chapter 1's `notes.md` (IaaS, EC2) and `deeper_dive_notes.md` (virtualization, VPC/subnets/security groups).

## What it does

- Shows the current server time (proves the page is server-rendered, not static).
- Displays EC2 instance metadata (instance ID, availability zone, instance type), pulled from AWS's instance metadata service - the app is "aware" it's running on AWS.
- An in-memory visit counter. Deliberately no database yet - that's deferred to a future project tied to a storage/database chapter, to keep this first build scoped.

## Infrastructure

- Custom VPC with a public subnet, route table, and internet gateway.
- Security group: inbound HTTP open, inbound SSH restricted to one IP only (not open to the world).
- One EC2 instance (t3.micro or t2.micro, free-tier-eligible family), Amazon Linux 2023.
- An EC2 User Data script (`user_data.sh`) installs dependencies and starts the app as a systemd service automatically at launch.

## Known simplifications (being upfront about these, not hiding them)

- `user_data.sh` embeds a copy of `app.py`'s code directly, so the instance doesn't need git or network access to fetch it separately. This means the two files have to be kept in sync by hand if `app.py` changes - fine for a small first project, not how a bigger project should work.
- The app runs via Flask's built-in development server (`app.run()`), which AWS/Flask itself doesn't recommend for production use. A more production-correct setup would sit it behind Gunicorn and Nginx. Kept simple on purpose for this first build.
- The systemd service runs the app as `root` so it can bind to port 80 without extra configuration. Not a security best practice for a real production app, but reasonable for a short-lived learning exercise.

## Security

The EC2 key pair (`.pem` file) created for SSH access is stored locally, outside this repo, and is excluded via `.gitignore`. No account IDs, access keys, or other credential material appear anywhere in this project.
