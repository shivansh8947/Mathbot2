import random
import requests

BOT_TOKEN = "8934030214:AAGadz1TF87m5DRfdr-Kj8LWtMiB6sOmf1w"
CHAT_ID = "8274392559"

numbers = [i for i in range(10, 200, 10)]

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

requests.post(url, data=data)

print("Worksheet sent!")