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

@bot.message_handler(
    func=lambda message: True,
    content_types=["text"]
)
def echo(message):
    print(dir(message))
    bot.reply_to(message, message.text)

bot.infinity_polling()
