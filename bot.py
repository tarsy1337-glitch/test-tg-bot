import os

import telebot
from dotenv import load_dotenv

load_dotenv()
tg_token = os.environ.get("TG_TOKEN")

bot = telebot.TeleBot(tg_token)

@bot.message_handler(commands=["start", "hello"])
def start_handler(message):
    print("Сообщение принято")
    bot.reply_to(message, "Привет!")

bot.infinity_polling()

@bot.message_handler(
    func=lambda mes: True,
    content_types=["text"]
)
def echo(message):
    print(dir(message))
    bot.reply_to(message, message.text)