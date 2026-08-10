#!/bin/bash
set -e

# EC2 User Data script - runs once at instance launch (Amazon Linux 2023).
# Clones the aws-certification repo and runs app.py directly from the
# checkout, instead of embedding a copy of the code here. This means the
# app can read every topic's notes.md/flashcards_data.js as they're added,
# without this script ever needing to change.
#
# NOTE: assumes the repo is public (no credentials needed to clone). If it
# ever becomes private, this needs a deploy key or similar instead.
#
# To pick up changes after this first boot: SSH in, `git pull` inside
# /opt/aws-certification, then `systemctl restart hands-on-app`. There's
# no CI/CD here on purpose - manual is appropriate for a small learning
# project.

REPO_URL="https://github.com/tylershelton1024/aws-certification.git"
REPO_DIR="/opt/aws-certification"
APP_DIR="$REPO_DIR/hands_on/01_CCP_app"

dnf update -y
dnf install -y python3-pip git

git clone "$REPO_URL" "$REPO_DIR"

pip3 install -r "$APP_DIR/requirements.txt"

cat > /etc/systemd/system/hands-on-app.service << SERVICEEOF
[Unit]
Description=AWS Hands-On Flask App
After=network.target

[Service]
ExecStart=/usr/bin/python3 $APP_DIR/app.py
Restart=always
User=root
WorkingDirectory=$APP_DIR

[Install]
WantedBy=multi-user.target
SERVICEEOF

systemctl daemon-reload
systemctl enable hands-on-app
systemctl start hands-on-app
