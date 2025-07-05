from flask import Flask, request
from telegram import Bot, Update
import json

app = Flask(__name__)

TOKEN = "توكن_بوتك"
bot = Bot(token=TOKEN)

user_states = {}
user_data = {}

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(force=True)

    update = Update.de_json(data, bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="أهلاً بك! أرسل /بياناتي للمتابعة.")
        user_states[chat_id] = "waiting_for_info"

    elif text == "/بياناتي":
        bot.send_message(chat_id=chat_id, text="أرسل اسمك ورقمك بالتسلسل.")
        user_states[chat_id] = "waiting_for_details"
        user_data[chat_id] = {}

    return "ok"
