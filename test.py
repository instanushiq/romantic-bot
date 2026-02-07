
import os
from twilio.rest import Client
import random

# 🔑 Twilio údaje
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]


client = Client(account_sid, auth_token)

# 💌 správy
messages = [
    "Láska 💖 dnes si mi prišla na myseľ skôr než káva ☕😌",
    "Potvorka 😈 len tak, aby si vedela, že na teba myslím 😏",
    "Myslím na teba 💭 a trochu sa pri tom usmievam 😊",
    "Vrr 🐾 dnes máš energiu, ktorú cítim až sem 😌",
    "Ahoj láska 💖 len malý pozdrav pre teba ✨"
]

# 🎲 vyber náhodnú správu
text = random.choice(messages)

# 📱 príjemcovia
recipients = [
    "whatsapp:+34680292570",
    "whatsapp:+31617354770"
]

# 📤 pošli JEDNU správu a skonči
for number in recipients:
    client.messages.create(
        from_="whatsapp:+14155238886",
        to=number,
        body=text
    )
    print(f"Správa odoslaná na {number}")

print("✅ Test hotový – program skončil")

