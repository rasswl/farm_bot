from flask import Flask, request
import telegram

app = Flask(__name__)

# توكن البوت الجديد
TOKEN = "7932173816:AAH_twNyIAd6ZEU8wC6lMKL0RS2FRyaRM_Y"
bot = telegram.Bot(token=TOKEN)

# تخزين الحالات للمستخدمين
user_states = {}
user_data = {}

@app.route("/", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="🌾 توثيق أسماء المزارع العراقية\nأهلاً بك!")
        user_states[chat_id] = "waiting_for_command"

    elif text == "/بياناتي":
        bot.send_message(chat_id=chat_id, text="🌿 شنو اسم المزرعة؟")
        user_states[chat_id] = "waiting_for_farm_name"
        user_data[chat_id] = {}

    return "ok"
