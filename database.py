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
            content TEXT,
            video_url TEXT
        )
    ''')
    try:
        c.execute("ALTER TABLE scripts ADD COLUMN video_url TEXT")
    except Exception:
        pass

    c.execute('''
        CREATE TABLE IF NOT EXISTS video_approvals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            video_url TEXT,
            script_id INTEGER,
            status TEXT DEFAULT 'PENDING',
            created_at TEXT,
            published_at TEXT,
            results_json TEXT
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

def save_script(topic, content, video_url=None):
    conn = get_connection()
    c = conn.cursor()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute(
        "INSERT INTO scripts (date, topic, content, video_url) VALUES (?, ?, ?, ?)",
        (now_str, topic, content, video_url)
    )
    conn.commit()
    script_id = c.lastrowid
    conn.close()
    return script_id, now_str

def update_script_video(script_id, video_url):
    ensure_initialized()
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE scripts SET video_url = ? WHERE id = ?", (video_url, script_id))
    conn.commit()
    conn.close()
    return True

_initialized = False

def ensure_initialized():
    global _initialized
    if not _initialized or not os.path.exists(DB_NAME):
        init_db()
        _initialized = True

def get_all_scripts():
    ensure_initialized()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, date, topic, content, video_url FROM scripts ORDER BY id DESC")
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return rows

def get_script_by_id(script_id):
    ensure_initialized()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, date, topic, content, video_url FROM scripts WHERE id = ?", (script_id,))
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

def create_video_approval(title, description, video_url, script_id=None):
    ensure_initialized()
    conn = get_connection()
    c = conn.cursor()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('''
        INSERT INTO video_approvals (title, description, video_url, script_id, status, created_at)
        VALUES (?, ?, ?, ?, 'PENDING', ?)
    ''', (title, description, video_url, script_id, now_str))
    conn.commit()
    approval_id = c.lastrowid
    conn.close()
    return approval_id

def get_video_approval(approval_id):
    ensure_initialized()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM video_approvals WHERE id = ?", (approval_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def update_video_approval_status(approval_id, status, results_json=None):
    ensure_initialized()
    conn = get_connection()
    c = conn.cursor()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute('''
        UPDATE video_approvals
        SET status = ?, published_at = ?, results_json = ?
        WHERE id = ?
    ''', (status, now_str, results_json, approval_id))
    conn.commit()
    conn.close()
    return True

def get_all_video_approvals(limit=50):
    ensure_initialized()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM video_approvals ORDER BY id DESC LIMIT ?", (limit,))
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return rows
