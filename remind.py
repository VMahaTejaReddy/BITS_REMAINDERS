import requests
from datetime import date, datetime
import os

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = "6126399992"

DEADLINES = [
    {
        "date": date(2026, 4, 24),
        "subjects": [
            "Operating Systems",
            "Environmental Studies",
            "Building Database Applications"
        ],
        "task": "Week 5 & 6 Graded Quiz",
        "time": "11:59 PM IST"
    },
    {
        "date": date(2026, 5, 3),
        "subjects": [
            "Operating Systems",
            "Environmental Studies",
            "Building Database Applications"
        ],
        "task": "Staff Graded Assignment 2 (Week 5 & 6)",
        "time": "11:58 PM IST"
    },
    {
        "date": date(2026, 5, 6),
        "subjects": [
            "Operating Systems",
            "Environmental Studies",
            "Building Database Applications"
        ],
        "task": "Week 5 & 6 Graded Quiz",
        "time": "11:59 PM IST"
    },
    {
        "date": date(2026, 5, 20),
        "subjects": [
            "Operating Systems",
            "Environmental Studies",
            "Building Database Applications"
        ],
        "task": "Staff Graded Assignment 3 (Week 5 & 6)",
        "time": "11:58 PM IST"
    },
]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"})

def main():
    today = date.today()
    alerts = []

    for d in DEADLINES:
        days_left = (d["date"] - today).days
        if days_left == 1:
            subject_list = "\n".join([f"  • {s}" for s in d["subjects"]])
            alerts.append(
                f"⚠️ <b>DEADLINE TOMORROW</b>\n"
                f"📚 <b>{d['task']}</b>\n"
                f"{subject_list}\n"
                f"🕐 Due: {d['date'].strftime('%b %d, %Y')} at {d['time']}\n"
                f"👉 Submit on Coursera before midnight!"
            )

    if alerts:
        for alert in alerts:
            send_telegram(alert)
        print(f"Sent {len(alerts)} reminder(s).")
    else:
        print("No deadlines tomorrow. No message sent.")

if __name__ == "__main__":
    main()
