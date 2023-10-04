import os
import random
import requests

from datetime import datetime, timezone

BLUESKY_HANDLE = os.environ['BLUESKY_HANDLE']
BLUESKY_APP_PASSWORD = os.environ['BLUESKY_APP_PASSWORD']

resp = requests.post(
    "https://bsky.social/xrpc/com.atproto.server.createSession",
    json={"identifier": BLUESKY_HANDLE, "password": BLUESKY_APP_PASSWORD},
)
session = resp.json()

now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

# text = random.choice(['Tau Time!', 'tau time', 'TAU TIME', 'Tau Time', '\u03C4\u23F3'])

text = 'TEST POST! HI FROM AN API CALL'

text = 'Unicode Test: \u03C4'
post = {
    "$type": "app.bsky.feed.post",
    "text": text,
    "createdAt": now,
}

resp = requests.post(
    "https://bsky.social/xrpc/com.atproto.repo.createRecord",
    headers={"Authorization": "Bearer " + session["accessJwt"]},
    json={
        "repo": session["did"],
        "collection": "app.bsky.feed.post",
        "record": post,
    },
)
