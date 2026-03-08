import requests
import datetime
import pytz
import time
import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
MESSAGE_ID = None

timezones = {
    "🇭🇺 Budapest": "Europe/Budapest",
    "🇷🇴 Bucharest": "Europe/Bucharest",
    "🇦🇷 Argentina": "America/Argentina/Buenos_Aires",
    "🇨🇦 Hamilton": "America/Toronto",
    "🇺🇸 Washington": "America/New_York"
}

def build_message():
    content = "🌍 **WORLD CLOCK**\n\n"
    
    for city, tz in timezones.items():
        now = datetime.datetime.now(pytz.timezone(tz)).strftime("%H:%M")
        content += f"{city} — {now}\n"

    return {"content": content}

while True:

    data = build_message()

    if MESSAGE_ID is None:
        r = requests.post(WEBHOOK_URL + "?wait=true", json=data)
        MESSAGE_ID = r.json()["id"]

    else:
        requests.patch(f"{WEBHOOK_URL}/messages/{MESSAGE_ID}", json=data)

    time.sleep(60)
