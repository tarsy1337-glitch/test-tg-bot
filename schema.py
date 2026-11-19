import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

db_name = os.environ.get("DB_NAME") or "default.db"

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

def init():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            key text,
            item text
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init()