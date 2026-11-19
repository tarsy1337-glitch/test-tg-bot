import random
import string
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

db_name = os.environ.get("DB_NAME") or "default.db"

class Db:
    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_item(self, item):
        key = "".join(random.choices(string.ascii_letters, k=10))
        self.cursor.execute(
            "INSERT INTO items (key, item) VALUES (?, ?)",
            (key, item,)
        )
        self.conn.commit()

    def list_item(self):
        res = self.cursor.execute(
            "SELECT key, item FROM items"
        )
        return res.fetchall() 

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()
