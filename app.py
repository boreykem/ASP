from flask import Flask, render_template, request, jsonify
import threading
import time
import datetime
import json
import os
import database
import ai_service
import telegram_service
import topics_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)
app.config["TEMPLATES_AUTO_RELOAD"] = True

if os.environ.get("VERCEL"):
    CONFIG_FILE = "/tmp/config.json"
else:
    CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

DEFAULT_CONFIG = {
    "gemini_key": "",
    "bot_token": "",
    "chat_id": "",
    "language": "km",
    "format": "NotebookLM Video Overview (Explainer Video ៥+ នាទី | សំឡេងខ្មែរ + ស្លាយ/CC អង់គ្លេស)",
    "tone": "ទាក់ទាញ & រំភើប (Hook & Catchy)",
    "auto_daily_topics": True,
    "topics": [],
    "scheduler": {
        "enabled": False,
        "time": "08:00",
        "last_run": None,
        "auto_diverse_topics": True
    }
}

def load_config():
    cfg = DEFAULT_CONFIG.copy()
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
                cfg.update(saved)
        except Exception:
            pass
    # Support environment variables (ideal for Vercel / Cloud Hosting)
    cfg["gemini_key"] = os.environ.get("GEMINI_API_KEY") or cfg.get("gemini_key") or DEFAULT_CONFIG["gemini_key"]
    cfg["bot_token"] = os.environ.get("TELEGRAM_BOT_TOKEN") or cfg.get("bot_token") or DEFAULT_CONFIG["bot_token"]
    cfg["chat_id"] = os.environ.get("TELEGRAM_CHAT_ID") or cfg.get("chat_id") or DEFAULT_CONFIG["chat_id"]
    return cfg

def save_config(cfg):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

# Initialize database
database.init_db()

# ------------------------------------------
# Background Daily Scheduler
# ------------------------------------------
scheduler_state = {
    "running_now": False,
    "last_result": None
}

def run_daily_automation(cfg):
    scheduler_state["running_now"] = True
    gemini_key = cfg.get("gemini_key")
    bot_token = cfg.get("bot_token")
    chat_id = cfg.get("chat_id")
    lang = cfg.get("language", "km")
    platform = cfg.get("format", "TikTok")
    tone = cfg.get("tone", "ទាក់ទាញ")
    
    # Send start notification to Telegram
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    start_msg = (
        f"🌅 *[Daily Automation - {today_date}]*\n"
        f"ចាប់ផ្តើមបង្កើតស្គ្រីបប្រចាំថ្ងៃទាំង ៥ ដោយស្វ័យប្រវត្តិ (អប់រំ, សេដ្ឋកិច្ច, សង្គម, វិទ្យាសាស្ត្រ, កសិកម្ម, សកលលោក, សាសនា)..."
    ) if lang == "km" else (
        f"🌅 *[Daily Automation - {today_date}]*\n"
        f"Generating 5 daily scripts across Education, Economy, Society, Science, Agriculture, Universe & Religion..."
    )
    telegram_service.send_message(bot_token, chat_id, start_msg)
    
    # ស្វែងរក ៥ ប្រធានបទប្លែកៗគ្នាជារៀងរាល់ថ្ងៃ
    _, topics, source = topics_engine.get_daily_diverse_topics(gemini_key, lang=lang)
    
    success_count = 0
    for idx, topic in enumerate(topics[:5]):
        ok, content, model = ai_service.generate_script(gemini_key, topic, platform=platform, tone=tone, lang=lang)
        if ok and content:
            database.save_script(topic, content)
            tg_text = f"📝 *ស្គ្រីបទី {idx+1}: {topic}*\n\n{content}"
            telegram_service.send_message(bot_token, chat_id, tg_text)
            success_count += 1
        time.sleep(2)
        
    summary = f"✅ បញ្ចប់ការងារស្វ័យប្រវត្តប្រចាំថ្ងៃ! បានបង្កើត និងផ្ញើ {success_count}/5 ស្គ្រីបជោគជ័យ។" if lang == "km" else f"✅ Daily automation finished! Generated and sent {success_count}/5 scripts."
    telegram_service.send_message(bot_token, chat_id, summary)
    
    cfg["scheduler"]["last_run"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_config(cfg)
    scheduler_state["running_now"] = False
    scheduler_state["last_result"] = summary

def scheduler_daemon_loop():
    while True:
        try:
            cfg = load_config()
            sched = cfg.get("scheduler", {})
            if sched.get("enabled"):
                target_time = sched.get("time", "08:00")
                now = datetime.datetime.now()
                current_hm = now.strftime("%H:%M")
                today_str = now.strftime("%Y-%m-%d")
                last_run = sched.get("last_run", "")
                
                # Check if it should trigger now and hasn't run today
                if current_hm == target_time and (not last_run or not last_run.startswith(today_str)):
                    if not scheduler_state["running_now"]:
                        threading.Thread(target=run_daily_automation, args=(cfg,), daemon=True).start()
        except Exception:
            pass
        time.sleep(30)

# Start background scheduler thread (disabled on serverless environments like Vercel)
if not os.environ.get("VERCEL"):
    threading.Thread(target=scheduler_daemon_loop, daemon=True).start()

# ------------------------------------------
# Vercel WSGI Middleware for Routing Fix
# ------------------------------------------
class VercelPathFixMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        matched_path = (
            environ.get("HTTP_X_MATCHED_PATH") or 
            environ.get("HTTP_X_NOW_ROUTE_URI") or 
            environ.get("HTTP_X_VERCEL_REWRITE_SOURCE") or
            environ.get("HTTP_X_ORIGINAL_URI") or
            environ.get("HTTP_X_FORWARDED_URI") or
            environ.get("RAW_URI") or
            environ.get("REQUEST_URI")
        )
        if matched_path:
            if "?" in matched_path:
                matched_path = matched_path.split("?", 1)[0]
            environ["PATH_INFO"] = matched_path
        elif environ.get("PATH_INFO") in ("/api/index.py", "/api/index", "/api"):
            environ["PATH_INFO"] = "/"
        return self.wsgi_app(environ, start_response)

app.wsgi_app = VercelPathFixMiddleware(app.wsgi_app)

# ------------------------------------------
# Flask Routes
# ------------------------------------------
@app.route("/")
@app.route("/api/index")
@app.route("/api/index.py")
def index():
    return render_template("index.html")

@app.route("/api/debug-env")
def debug_env():
    return jsonify({
        "path_info": request.environ.get("PATH_INFO"),
        "raw_headers": {k: v for k, v in request.environ.items() if k.startswith("HTTP_") or "URI" in k or "PATH" in k}
    })

@app.route("/api/config", methods=["GET"])
def get_config():
    return jsonify({"success": True, "config": load_config()})

@app.route("/api/config", methods=["POST"])
def update_config():
    data = request.json or {}
    current = load_config()
    current.update(data)
    save_config(current)
    return jsonify({"success": True, "config": current})

@app.route("/api/daily-topics", methods=["GET"])
def api_get_daily_topics():
    cfg = load_config()
    lang = request.args.get("lang") or cfg.get("language", "km")
    key = cfg.get("gemini_key")
    ok, topics, source = topics_engine.get_daily_diverse_topics(key, lang=lang)
    return jsonify({"success": ok, "topics": topics, "source": source})

@app.route("/api/categories", methods=["GET"])
def api_get_categories():
    return jsonify({"success": True, "categories": topics_engine.CATEGORIES})

@app.route("/api/generate-batch", methods=["POST"])
def api_generate_batch():
    data = request.json or {}
    cfg = load_config()
    key = data.get("gemini_key") or cfg.get("gemini_key")
    bot_token = data.get("bot_token") or cfg.get("bot_token")
    chat_id = data.get("chat_id") or cfg.get("chat_id")
    platform = data.get("format") or cfg.get("format")
    tone = data.get("tone") or cfg.get("tone")
    lang = data.get("lang") or cfg.get("language", "km")
    topics = data.get("topics", [])
    
    # ប្រសិនបើអ្នកប្រើប្រាស់មិនបានវាយប្រធានបទ ត្រូវទាញយក ៥ ប្រធានបទស្វ័យប្រវត្តពី ៧ វិស័យ
    clean_topics = [t.strip() for t in topics if t and t.strip()]
    if not clean_topics:
        _, auto_topics, _ = topics_engine.get_daily_diverse_topics(key, lang=lang)
        clean_topics = auto_topics[:5]
    
    # Save active credentials
    cfg["gemini_key"] = key
    cfg["bot_token"] = bot_token
    cfg["chat_id"] = chat_id
    cfg["format"] = platform
    cfg["tone"] = tone
    cfg["topics"] = clean_topics
    cfg["language"] = lang
    save_config(cfg)
    
    results = []
    for idx, topic in enumerate(clean_topics[:5]):
        ok, content, model = ai_service.generate_script(key, topic, platform=platform, tone=tone, lang=lang)
        if not ok:
            results.append({
                "index": idx + 1,
                "topic": topic,
                "success": False,
                "error": content
            })
            continue
            
        # Save to DB
        script_id, date_str = database.save_script(topic, content)
        
        # Send to Telegram
        tg_text = f"📝 *ស្គ្រីបទី {idx+1}: {topic}*\n\n{content}"
        tg_ok, tg_status = telegram_service.send_message(bot_token, chat_id, tg_text)
        
        results.append({
            "index": idx + 1,
            "id": script_id,
            "topic": topic,
            "success": True,
            "model": model,
            "date": date_str,
            "telegram_sent": tg_ok,
            "telegram_status": tg_status,
            "content": content
        })
        
    return jsonify({"success": True, "results": results, "topics_used": clean_topics})

@app.route("/api/history", methods=["GET"])
def api_get_history():
    scripts = database.get_all_scripts()
    return jsonify({"success": True, "scripts": scripts})

@app.route("/api/history/<int:script_id>", methods=["GET"])
def api_get_script(script_id):
    script = database.get_script_by_id(script_id)
    if script:
        return jsonify({"success": True, "script": script})
    return jsonify({"success": False, "error": "Script not found"}), 404

@app.route("/api/history/<int:script_id>", methods=["DELETE"])
def api_delete_script(script_id):
    deleted = database.delete_script(script_id)
    return jsonify({"success": deleted})

@app.route("/api/history/<int:script_id>/resend", methods=["POST"])
def api_resend_script(script_id):
    script = database.get_script_by_id(script_id)
    if not script:
        return jsonify({"success": False, "error": "Script not found"}), 404
        
    cfg = load_config()
    bot_token = cfg.get("bot_token")
    chat_id = cfg.get("chat_id")
    
    text = f"📝 *[ផ្ញើឡើងវិញ / Resend]* {script['topic']}\n\n{script['content']}"
    ok, msg = telegram_service.send_message(bot_token, chat_id, text)
    return jsonify({"success": ok, "message": msg})

@app.route("/api/scheduler", methods=["GET"])
def api_get_scheduler():
    cfg = load_config()
    sched = cfg.get("scheduler", {})
    return jsonify({
        "success": True,
        "scheduler": sched,
        "state": scheduler_state
    })

@app.route("/api/scheduler", methods=["POST"])
def api_update_scheduler():
    data = request.json or {}
    cfg = load_config()
    sched = cfg.get("scheduler", {})
    sched["enabled"] = bool(data.get("enabled", sched.get("enabled")))
    if "time" in data:
        sched["time"] = data["time"]
    if "auto_diverse_topics" in data:
        sched["auto_diverse_topics"] = bool(data["auto_diverse_topics"])
    cfg["scheduler"] = sched
    save_config(cfg)
    return jsonify({"success": True, "scheduler": sched})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
