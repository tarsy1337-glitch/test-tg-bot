import random
import string
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

db_name = os.environ.get("DB_NAME")

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

def add_item(item):
    key = "".join(random.choices(string.ascii_letter, k=10))
    cursor.execute(
        "INSERT INTO items (key, item) VALUES (?, ?)",
        (key, item,)
    )

def list_item(item):
    res = cursor.execute(
        "SELECT key, name FROM items"
    )
    return res.fetchall() 