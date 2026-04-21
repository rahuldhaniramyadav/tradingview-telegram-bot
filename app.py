from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

@app.route('/')
def home():
    return "Running ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if data.get("signal") == "BUY":
        msg = f"📈 BUY SIGNAL\nSymbol: {data.get('symbol')}\nPrice: {data.get('price')}"
        send_telegram(msg)

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
