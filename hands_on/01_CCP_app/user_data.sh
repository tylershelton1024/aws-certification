#!/bin/bash
set -e

# EC2 User Data script - runs once at instance launch (Amazon Linux 2023).
# Installs dependencies, writes the app, and runs it as a systemd service.
#
# NOTE: keep this in sync with app.py by hand if app.py changes - this
# script embeds a copy of it so the instance doesn't need git/network
# access to fetch it separately. Fine for a small first project; a
# future project could pull from S3 or git instead.

dnf update -y
dnf install -y python3-pip

mkdir -p /opt/hands_on_app
cd /opt/hands_on_app

cat > app.py << 'PYEOF'
from flask import Flask
import urllib.request
import datetime

app = Flask(__name__)
visit_count = 0

METADATA_BASE = "http://169.254.169.254/latest"


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
PYEOF

cat > requirements.txt << 'REQEOF'
Flask
REQEOF

pip3 install -r requirements.txt

cat > /etc/systemd/system/hands-on-app.service << 'SERVICEEOF'
[Unit]
Description=AWS Hands-On Flask App
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/hands_on_app/app.py
Restart=always
User=root
WorkingDirectory=/opt/hands_on_app

[Install]
WantedBy=multi-user.target
SERVICEEOF

systemctl daemon-reload
systemctl enable hands-on-app
systemctl start hands-on-app
