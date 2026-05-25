import random
import requests
import schedule
import time
from datetime import datetime, timedelta

BOT_TOKEN = "8934030214:AAGadz1TF87m5DRfdr-Kj8LWtMiB6sOmf1w"
CHAT_ID = "8274392559"

numbers = [i for i in range(10, 200, 10)]

last_message_id = None

def send_worksheet():
    global last_message_id

    worksheet = "📝 Daily Addition Worksheet\n\n"

    for i in range(1, 21):
        a = random.choice(numbers)
        b = random.choice(numbers)
        worksheet += f"{i}. {a} + {b} = _____\n"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": worksheet
    }

    response = requests.post(url, data=data).json()

    last_message_id = response["result"]["message_id"]

    print("Worksheet sent!")

def delete_worksheet():
    global last_message_id

    if last_message_id:

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteMessage"

        data = {
            "chat_id": CHAT_ID,
            "message_id": last_message_id
        }

        requests.post(url, data=data)

        print("Worksheet deleted!")

# SEND DAILY AT 7 AM
schedule.every().day.at("07:00").do(send_worksheet)

# DELETE DAILY AT 12 AM
schedule.every().day.at("00:00").do(delete_worksheet)

print("Bot is running...")

while True:
    schedule.run_pending()
    time.sleep(1)