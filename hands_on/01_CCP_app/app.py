from flask import Flask
import urllib.request
import datetime
import os
import re
import json
import glob
import markdown

app = Flask(__name__)
visit_count = 0

METADATA_BASE = "http://169.254.169.254/latest"

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


def get_instance_metadata():
    try:
        token_req = urllib.request.Request(
            METADATA_BASE + "/api/token",
            method="PUT",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
        )
        token = urllib.request.urlopen(token_req, timeout=2).read().decode()

        def fetch(path):
            req = urllib.request.Request(
                METADATA_BASE + path,
                headers={"X-aws-ec2-metadata-token": token},
            )
            return urllib.request.urlopen(req, timeout=2).read().decode()

        return {
            "instance_id": fetch("/meta-data/instance-id"),
            "availability_zone": fetch("/meta-data/placement/availability-zone"),
            "instance_type": fetch("/meta-data/instance-type"),
        }
    except Exception:
        return {
            "instance_id": "unavailable (not running on EC2?)",
            "availability_zone": "unavailable",
            "instance_type": "unavailable",
        }


@app.route("/")
def index():
    global visit_count
    visit_count += 1
    metadata = get_instance_metadata()
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    return f"""
    <html>
    <head><title>AWS Cloud Practitioner - Hands-On App</title></head>
    <body style="font-family: sans-serif; max-width: 640px; margin: 60px auto;">
        <h1>Hello from EC2</h1>
        <p><strong>Server time:</strong> {now}</p>
        <p><strong>Instance ID:</strong> {metadata['instance_id']}</p>
        <p><strong>Availability Zone:</strong> {metadata['availability_zone']}</p>
        <p><strong>Instance Type:</strong> {metadata['instance_type']}</p>
        <p><strong>Visits since last restart:</strong> {visit_count}</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
