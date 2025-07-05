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
        bot.send_message(chat_id=chat_id, text="اهلاً بيك! 🌾 ارسل /بياناتي لتسجيل معلوماتك.")
        user_states[chat_id] = "waiting_for_data"

    elif text == "/بياناتي":
        bot.send_message(chat_id=chat_id, text="ارسل اسمك ورقمك بصيغة:\nالاسم - الرقم")
        user_states[chat_id] = "waiting_for_name_phone"
        user_data[chat_id] = {}

    elif user_states.get(chat_id) == "waiting_for_name_phone":
        try:
            name, phone = text.split(" - ")
            user_data[chat_id]["name"] = name.strip()
            user_data[chat_id]["phone"] = phone.strip()
            bot.send_message(chat_id=chat_id, text=f"تم حفظ بياناتك ✅\nالاسم: {name}\nالرقم: {phone}")
            user_states[chat_id] = None
        except:
            bot.send_message(chat_id=chat_id, text="⚠️ الصيغة غير صحيحة. حاول مرة أخرى:\nالاسم - الرقم")

    else:
        bot.send_message(chat_id=chat_id, text="❓ أمر غير مفهوم، ارسل /start للبدء")

    return "ok"
