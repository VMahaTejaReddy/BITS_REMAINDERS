import requests
from datetime import date
import os
import sys

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = "6126399992"

DEADLINES = [
    {
        "date": date(2026, 4, 24),
        "subjects": ["Operating Systems", "Environmental Studies", "Building Database Applications"],
        "task": "Week 5 & 6 Graded Quiz",
        "time": "11:59 PM IST"
    },
    {
        "date": date(2026, 5, 3),
        "subjects": ["Operating Systems", "Environmental Studies", "Building Database Applications"],
        "task": "Staff Graded Assignment 2 (Week 5 & 6)",
        "time": "11:58 PM IST"
    },
    {
        "date": date(2026, 5, 6),
        "subjects": ["Operating Systems", "Environmental Studies", "Building Database Applications"],
        "task": "Week 5 & 6 Graded Quiz",
        "time": "11:59 PM IST"
    },
    {
        "date": date(2026, 5, 20),
        "subjects": ["Operating Systems", "Environmental Studies", "Building Database Applications"],
        "task": "Staff Graded Assignment 3 (Week 5 & 6)",
        "time": "11:58 PM IST"
    },
]

def send_telegram(message):
    if not BOT_TOKEN:
        print("ERROR: TELEGRAM_BOT_TOKEN is empty or not set!")
        sys.exit(1)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    print(f"Sending to chat_id: {CHAT_ID}")
    print(f"Using token (first 10 chars): {BOT_TOKEN[:10]}...")

    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    })

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    if not response.ok:
        print("ERROR: Telegram API rejected the request!")
        sys.exit(1)

def main():
    today = date.today()
    print(f"Today: {today}")

    alerts = []
    for d in DEADLINES:
        days_left = (d["date"] - today).days
        print(f"Deadline {d['date']} → {days_left} days away")
        if days_left >= 0:
            subject_list = "\n".join([f"  • {s}" for s in d["subjects"]])
            alerts.append(
                f"⚠️ <b>DEADLINE TOMORROW</b>\n"
                f"📚 <b>{d['task']}</b>\n"
                f"{subject_list}\n"
                f"🕐 Due: {d['date'].strftime('%b %d, %Y')} at {d['time']}\n"
                f"👉 Submit on Coursera before midnight!"
            )

    print(f"Alerts to send: {len(alerts)}")
    if alerts:
        for alert in alerts:
            send_telegram(alert)
        print("All messages sent.")
    else:
        print("No upcoming deadlines.")

if __name__ == "__main__":
    main()
