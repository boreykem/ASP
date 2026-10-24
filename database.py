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
    
    # Seed default sample scripts if database is empty
    c.execute("SELECT COUNT(*) FROM scripts")
    count = c.fetchone()[0]
    if count == 0:
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sample_scripts = [
            (
                "ដូងក្រអូបធម្មជាតិ អេស៊ីហ្វាម - ផ្អែមឆ្ងាញ់ត្រជាក់បំពង់ក",
                "🎬 [Hook - ៣ វិនាទីដំបូង]\nតើបងប្អូនដឹងទេថា ហេតុអ្វីបានជាដូងក្រអូបពីចំការ អេស៊ីហ្វាម មានរសជាតិផ្អែមក្រអូបប្លែកពីគេ?\n\n🌿 [គុណតម្លៃធម្មជាតិ]\nពីព្រោះដូងក្រអូបយើងត្រូវបានដាំដុះតាមក្បួនសរីរាង្គធម្មជាតិសុទ្ធសាធ ១០០% គ្មានសារធាតុគីមី ទឹកដូងថ្លាត្រជាក់ ជួយប៉ូវកម្លាំង និងធ្វើឱ្យអារម្មណ៍ស្រស់ស្រាយភ្លាមៗ!\n\n📞 [Call to Action]\nកុម្ម៉ង់ឥឡូវនេះ មានសេវាដឹកជញ្ជូនរហ័សដល់គេហដ្ឋាន! ទំនាក់ទំនងតាម Page ឬខលមកលេខក្រុមហ៊ុនផ្ទាល់។",
                now_str
            ),
            (
                "ក្រុមហ៊ុនអេស៊ី បូមលូ - សេវាកម្មរហ័សទាន់ចិត្ត ២៤ ម៉ោង",
                "🚨 [Hook]\nលូស្ទះ បន្ទប់ទឹកជះក្លិន ឬអាងទឹកកខ្វក់មែនទេ? កុំបារម្ភទៀតអី!\n\n🛠️ [ដំណោះស្រាយ]\nក្រុមហ៊ុនអេស៊ី បូមលូ ផ្តល់ជូនសេវាកម្មបូមលូ លាងសម្អាត និងដោះស្រាយបញ្ហាស្ទះលូគ្រប់ប្រភេទ ដោយប្រើរថយន្តទំនើប និងក្រុមការងារជំនាញច្បាស់លាស់ សម្អាតបានស្អាតល្អ ១០០% គ្មានក្លិនរំខាន។\n\n⚡ [CTA]\nទាក់ទងមកយើងខ្ញុំឥឡូវនេះ ដើម្បីទទួលបានតម្លៃសមរម្យ និងសេវាកម្មរហ័សទាន់ចិត្ត ២៤ ម៉ោង!",
                now_str
            )
        ]
        c.executemany(
            "INSERT INTO scripts (topic, content, date) VALUES (?, ?, ?)",
            sample_scripts
        )
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
