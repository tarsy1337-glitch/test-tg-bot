import os

import telebot
from dotenv import load_dotenv

from db import add_item, list_item

load_dotenv()
tg_token = os.environ.get("TG_TOKEN")

bot = telebot.TeleBot(tg_token)

@bot.message_handler(commands=["start", "hello"])
def start_handler(message):
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""
    print(f"Bot started for: {username}")
    bot.reply_to(message, f"Привет {first_name} {last_name} !")

@bot.message_handler(
    func=lambda message: True,
    content_types=["text"]
)
def echo(message):
    bot.reply_to(message, message.text)

@bot.message_handler(
    commands=["add"]
)
def add_item(message):
    parts = message.text.split(" ")
    item = parts[1] if len(parts) > 1 else None
    if item:
        add_item(item)
        bot.reply_to(message, "Элемент добавлен")
    else:
        bot.reply_to(message, "Элемент не добавлен")
    

@bot.message_handler(
    commands=["list"]
)
def list_item(message):
    items = list_item()
    res = ", ".join(name for _, name in items)
    bot.reply_to(message, res)

bot.infinity_polling()
