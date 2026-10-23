import sqlite3
import datetime
import os

if os.environ.get("VERCEL"):
    DB_NAME = "/tmp/scripts_database.db"
else:
    DB_NAME = "scripts_database.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scripts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            topic TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_script(topic, content):
    conn = get_connection()
    c = conn.cursor()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute(
        "INSERT INTO scripts (date, topic, content) VALUES (?, ?, ?)",
        (now_str, topic, content)
    )
    conn.commit()
    script_id = c.lastrowid
    conn.close()
    return script_id, now_str

def get_all_scripts():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, date, topic, content FROM scripts ORDER BY id DESC")
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return rows

def get_script_by_id(script_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, date, topic, content FROM scripts WHERE id = ?", (script_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def delete_script(script_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM scripts WHERE id = ?", (script_id,))
    deleted = c.rowcount > 0
    conn.commit()
    conn.close()
    return deleted
