import sqlite3
import os

db_name = os.environ.get("DB_NAME")

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

def init():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            key text,
            item text
        )
    """)

if __name__ == "__pass__":
    init()