
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
    "Potvorka 😈 ",
    "Myslím na teba 💭 a trochu sa pri tom usmievam 😊",
    "Vrr 🐾 dnes máš energiu, ktorú cítim až sem 😌",
    "Ahoj láska 💖 len malý pozdrav pre teba ✨",
    "Oficiálne priznávam: myslím na teba častejšie než na jedlo. A to je čo povedať. 🍕😂",
    "Milujem ťa. A hej… je to tvoja chyba 😄",
    "Len hlásenie: stále na teba myslím.",
    "Ak by si bola problém, bola by si môj obľúbený.",
    "Milujem ťa. Áno, aj teraz.",
    "Si dôvod, prečo sa usmievam na mobil.",
    "Milujem ťa. Zvykaj si 😌",
    "Keby bola láska šport, ty máš zlato 🥇",
    "Milujem ťa… a nie, nie je to spam.",
    "Si môj denný dôvod na úsmev.",
    "Len som ti chcela pripomenúť, že si úžasná.",
    "Milujem ťa potichu, ale úprimne.",
    "Si presne ten pocit, ktorý chcem mať častejšie.",

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


