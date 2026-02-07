
import os
from twilio.rest import Client
import random

# 🔑 Twilio údaje
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]


client = Client(account_sid, auth_token)

# 💌 správy
messages = [
   "Viem, že teraz pracuješ, ale ja by som si ťa najradšej pritiahla k sebe a nepustila.",
    "Celý večer myslím na to, ako by som sa k tebe pritúlila, keby si tu bola.",
    "Nočná ti síce berie spánok, ale mne berieš myšlienky 😌",
    "Ak cítiš jemné mrazenie, možno to som ja, ako na teba myslím.",
    "Priznávam sa, keby si teraz prišla, nechala by som všetko tak.",
    "Ticho noci má jednu chybu, že v ňom nie si so mnou.",
    "Len si predstav, že ti potichu poviem, ako veľmi sa mi páčiš.",
    "Niektoré myšlienky sú ideálne práve na noc, a ty si jedna z nich.",
    "Ak by som ti mohla poslať dotyk namiesto správy, už by si ho cítila.",
    "Noc a ty, kombinácia, ktorá ma nenechá spať.",
    "Aj unavená si pre mňa nebezpečne príťažlivá.",

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



