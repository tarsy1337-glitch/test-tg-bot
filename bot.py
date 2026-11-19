import os

import telebot
from dotenv import load_dotenv

load_dotenv()
tg_token = os.environ.get("TG_TOKEN")

bot = telebot.TeleBot(tg_token)
# /start
@bot.message_handler(commands=["start", "hello"])
def start_handler(message):
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    print(f"Bot started for: {username}")
    bot.reply_to(message, f"Привет {first_name} {last_name} !")

@bot.message_handler(
    func=lambda message: True,
    content_types=["text"]
)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
