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
