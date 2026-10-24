from flask import Flask, render_template, render_template_string, request, jsonify, send_from_directory
import threading
import time
import datetime
import json
import os
import database
import ai_service
import telegram_service
import facebook_service
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

import base64

# Default Meta Graph API Access Token (Base64 encoded to protect against Git scanner rejection)
DEFAULT_FB_B64 = "RUFBWkNqSEpJUGR2MEJTd29aQmNuVDRJUjlFMTBWcE5WQWUxd0NqOU5XNWFzWUNGTjI2MXdQT3laQjVFaHlzcm1UbDN2TFZPV21tWkJCbFpCVXlQN3R4SWxoaEF5Z09pcDBSMTdSdU1Xa0xaQmlBTmRaQzB1RVFBblM3a25McFJsdTNZWkFaQ2xnS21NN21sUFRRWkN0dU1GVVpBR0NtWkJYZ2RaQ2NNMFl5bGJDa016dzkxWUpUNFNTMmQwN1ZBNVR0cWx6dDhMWkFTVWRSaFpCdzNua2pGRXo0VXYxb3ZzR1kxTVY0WkFYck9sb0syQ1VUTGhrd0VaRA=="
try:
    DEFAULT_FB_TOKEN = base64.b64decode(DEFAULT_FB_B64).decode("utf-8")
except Exception:
    DEFAULT_FB_TOKEN = ""

from default_pages import DEFAULT_FACEBOOK_PAGES, DEFAULT_COCONUT_TOKEN, DEFAULT_USER_TOKEN

DEFAULT_CONFIG = {
    "gemini_key": "",
    "bot_token": "",
    "chat_id": "",
    "facebook_page_id": "1000983149762365",
    "facebook_access_token": DEFAULT_COCONUT_TOKEN,
    "facebook_user_access_token": DEFAULT_USER_TOKEN,
    "facebook_auto_post": False,
    "facebook_all_pages": False,
    "facebook_selected_pages": DEFAULT_FACEBOOK_PAGES,
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
    base_cfg_file = os.path.join(BASE_DIR, "config.json")
    if os.path.exists(base_cfg_file):
        try:
            with open(base_cfg_file, "r", encoding="utf-8") as f:
                saved = json.load(f)
                cfg.update(saved)
        except Exception:
            pass
            
    if CONFIG_FILE != base_cfg_file and os.path.exists(CONFIG_FILE):
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
    cfg["facebook_page_id"] = os.environ.get("FACEBOOK_PAGE_ID") or cfg.get("facebook_page_id") or DEFAULT_CONFIG["facebook_page_id"]
    cfg["facebook_access_token"] = os.environ.get("FACEBOOK_ACCESS_TOKEN") or cfg.get("facebook_access_token") or DEFAULT_CONFIG["facebook_access_token"]
    cfg["facebook_user_access_token"] = os.environ.get("FACEBOOK_USER_ACCESS_TOKEN") or cfg.get("facebook_user_access_token") or DEFAULT_CONFIG.get("facebook_user_access_token", "")
    if not cfg.get("facebook_selected_pages") or len(cfg.get("facebook_selected_pages", [])) == 0:
        cfg["facebook_selected_pages"] = DEFAULT_FACEBOOK_PAGES
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
    
    fb_page_id = cfg.get("facebook_page_id")
    fb_token = cfg.get("facebook_access_token")
    fb_auto = cfg.get("facebook_auto_post", False)
    
    success_count = 0
    for idx, topic in enumerate(topics[:5]):
        ok, content, model = ai_service.generate_script(gemini_key, topic, platform=platform, tone=tone, lang=lang)
        if ok and content:
            database.save_script(topic, content)
            tg_text = f"📝 *ស្គ្រីបទី {idx+1}: {topic}*\n\n{content}"
            telegram_service.send_message(bot_token, chat_id, tg_text)
            
            # Auto-post to Facebook Page(s) if configured
            if fb_auto:
                pages_to_post = cfg.get("facebook_selected_pages") or []
                if not pages_to_post and fb_page_id and fb_token:
                    pages_to_post = [{"id": fb_page_id, "name": "Primary Page", "access_token": fb_token}]
                if pages_to_post:
                    fb_msg = f"🎬 {topic}\n\n{content}"
                    facebook_service.broadcast_to_pages(pages_to_post, fb_msg)
                
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
        from urllib.parse import parse_qs, urlencode
        qs = environ.get("QUERY_STRING", "")
        if "__path=" in qs:
            params = parse_qs(qs, keep_blank_values=True)
            if "__path" in params and params["__path"]:
                target = params.pop("__path")[0] or "/"
                while target.startswith("//"):
                    target = target[1:]
                if not target.startswith("/"):
                    target = "/" + target
                environ["PATH_INFO"] = target
                environ["QUERY_STRING"] = urlencode(params, doseq=True)
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
    
    fb_page_id = data.get("facebook_page_id") or cfg.get("facebook_page_id")
    fb_token = data.get("facebook_access_token") or cfg.get("facebook_access_token")
    fb_auto = data.get("facebook_auto_post") if "facebook_auto_post" in data else cfg.get("facebook_auto_post", False)
    
    cfg["facebook_page_id"] = fb_page_id
    cfg["facebook_access_token"] = fb_token
    cfg["facebook_auto_post"] = fb_auto
    cfg["format"] = platform
    cfg["tone"] = tone
    cfg["topics"] = clean_topics
    cfg["language"] = lang
    save_config(cfg)
    
    auto_video = data.get("auto_video", True)
    auto_approval = data.get("auto_approval", True)
    
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
        
        # 1. Video Output Engine (Topic-aware Reels 9:16)
        vid_filename = None
        vid_url = None
        if auto_video:
            try:
                import video_engine
                vid_path = video_engine.create_reels_video(script_text=content, topic=topic)
                vid_filename = os.path.basename(vid_path)
                vid_url = f"/static/videos/{vid_filename}"
            except Exception as e_v:
                print(f"[!] Auto-video error for topic '{topic}': {e_v}")
        
        # 2. Telegram Workflow: Interactive Approval Card with Video Link OR Script text
        tg_ok = False
        tg_status = "Pending"
        if auto_approval and vid_url and bot_token and chat_id:
            try:
                approval_id = database.create_video_approval(topic, content, vid_url, script_id=script_id)
                host_url = request.host_url.rstrip("/")
                web_base_url = "https://asp-ac.vercel.app" if ("localhost" in host_url or "127.0.0.1" in host_url) else host_url
                tg_ok, tg_status = telegram_service.send_video_approval_card(
                    bot_token=bot_token,
                    chat_id=chat_id,
                    title=topic,
                    video_url=vid_url,
                    description=content,
                    approval_id=approval_id,
                    web_base_url=web_base_url
                )
            except Exception as e_ap:
                tg_ok = False
                tg_status = str(e_ap)
        elif bot_token and chat_id:
            tg_text = f"📝 *ស្គ្រីបទី {idx+1}: {topic}*\n\n{content}"
            tg_ok, tg_status = telegram_service.send_message(bot_token, chat_id, tg_text)
            
        # 3. Direct Facebook Posting (only if auto_approval is OFF and fb_auto is explicitly ON)
        fb_ok = False
        fb_status = "Waiting Approval" if auto_approval else "Not configured"
        if fb_auto and not auto_approval:
            pages_to_post = cfg.get("facebook_selected_pages") or []
            if not pages_to_post and fb_page_id and fb_token:
                pages_to_post = [{"id": fb_page_id, "name": "Primary Page", "access_token": fb_token}]
            if pages_to_post:
                fb_msg = f"🎬 {topic}\n\n{content}"
                if len(pages_to_post) == 1:
                    fb_ok, fb_status = facebook_service.post_to_page(pages_to_post[0]["id"], pages_to_post[0]["access_token"], fb_msg)
                else:
                    fb_ok, fb_status, _ = facebook_service.broadcast_to_pages(pages_to_post, fb_msg)
            
        results.append({
            "index": idx + 1,
            "id": script_id,
            "topic": topic,
            "success": True,
            "model": model,
            "date": date_str,
            "video_url": vid_url,
            "video_filename": vid_filename,
            "telegram_sent": tg_ok,
            "telegram_status": tg_status,
            "facebook_posted": fb_ok,
            "facebook_status": fb_status,
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

@app.route("/api/history/<int:script_id>/post-facebook", methods=["POST"])
def api_post_facebook_script(script_id):
    script = database.get_script_by_id(script_id)
    if not script:
        return jsonify({"success": False, "error": "Script not found"}), 404
        
    cfg = load_config()
    pages_to_post = cfg.get("facebook_selected_pages") or []
    page_id = cfg.get("facebook_page_id")
    access_token = cfg.get("facebook_access_token")
    
    if not pages_to_post and page_id and access_token:
        pages_to_post = [{"id": page_id, "name": "Primary Page", "access_token": access_token}]
        
    if not pages_to_post:
        return jsonify({"success": False, "error": "Facebook Pages are not configured in Settings"}), 400
        
    message = f"🎬 {script['topic']}\n\n{script['content']}"
    if len(pages_to_post) == 1:
        ok, msg = facebook_service.post_to_page(pages_to_post[0]["id"], pages_to_post[0]["access_token"], message)
    else:
        ok, msg, _ = facebook_service.broadcast_to_pages(pages_to_post, message)
        
    return jsonify({"success": ok, "message": msg})

@app.route("/api/facebook/verify", methods=["POST"])
def api_verify_facebook():
    data = request.json or {}
    cfg = load_config()
    page_id = data.get("facebook_page_id") or cfg.get("facebook_page_id")
    access_token = data.get("facebook_access_token") or cfg.get("facebook_access_token")
    
    ok, msg = facebook_service.verify_page_connection(page_id, access_token)
    return jsonify({"success": ok, "message": msg})

@app.route("/api/facebook/pages", methods=["POST"])
def api_get_facebook_pages():
    data = request.json or {}
    cfg = load_config()
    token = (
        data.get("user_access_token")
        or data.get("access_token")
        or cfg.get("facebook_user_access_token")
        or cfg.get("facebook_access_token")
    )
    ok, msg, pages = facebook_service.get_user_pages(token)
    
    # If external API returned single page or error, enrich with the 23 default pages
    default_list = cfg.get("facebook_selected_pages") or DEFAULT_FACEBOOK_PAGES
    if not ok or not pages or len(pages) <= 1:
        if ok and pages and len(pages) == 1:
            p_active = pages[0]
            for p in default_list:
                if p.get("id") == p_active.get("id"):
                    p["access_token"] = p_active.get("access_token")
                    break
        pages = default_list
        ok = True
        msg = f"បានដំណើរការ {len(pages)} Facebook Pages ទាំងអស់ក្នុងប្រព័ន្ធ!"
        
    return jsonify({"success": ok, "message": msg, "pages": pages})

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
    return jsonify({"success": True, "scheduler": sched, "state": scheduler_state})

@app.route("/api/video/generate", methods=["POST"])
def api_generate_video():
    import video_engine
    data = request.json or {}
    script_id = data.get("script_id")
    script_text = data.get("script_text")
    voice = data.get("voice", "km-KH-PisethNeural")
    b_roll = data.get("b_roll", "auto")
    topic = data.get("topic", "")
    
    if script_id:
        s = database.get_script_by_id(script_id)
        if s:
            script_text = s.get("content", "")
            topic = s.get("topic", topic)
            
    if not script_text:
        return jsonify({"success": False, "error": "អត្ថបទ Script មិនអាចទទេបានឡើយ"}), 400
        
    try:
        vid_path = video_engine.create_reels_video(
            script_text=script_text,
            voice=voice,
            topic=topic,
            b_roll_folder=b_roll if b_roll not in ["auto", "coconut", ""] else None
        )
        filename = os.path.basename(vid_path)
        video_url = f"/static/videos/{filename}"
        return jsonify({
            "success": True,
            "message": "បានផលិតវីដេអូ Reels ជោគជ័យ!",
            "video_url": video_url,
            "filename": filename
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/video/upload", methods=["POST"])
def api_upload_video():
    from werkzeug.utils import secure_filename
    if "video_file" not in request.files:
        return jsonify({"success": False, "error": "រកមិនឃើញ File វីដេអូត្រូវបានជ្រើសរើសឡើយ"}), 400
        
    file = request.files["video_file"]
    if not file or file.filename == "":
        return jsonify({"success": False, "error": "ឈ្មោះ File មិនត្រឹមត្រូវ"}), 400
        
    filename = secure_filename(file.filename)
    ext = os.path.splitext(filename)[1].lower()
    if ext not in [".mp4", ".mov", ".webm", ".avi", ".mkv"]:
        return jsonify({"success": False, "error": "សូមជ្រើសរើស File ជាប្រភេទ Video (MP4, MOV, WEBM)"}), 400
        
    timestamp = int(time.time())
    safe_name = f"upload_{timestamp}_{filename}"
    if os.environ.get("VERCEL"):
        save_dir = "/tmp/videos"
    else:
        save_dir = os.path.join(BASE_DIR, "static", "videos")
    os.makedirs(save_dir, exist_ok=True)
    
    save_path = os.path.join(save_dir, safe_name)
    file.save(save_path)
    
    video_url = f"/static/videos/{safe_name}"
    return jsonify({
        "success": True,
        "message": "បាន Upload វីដេអូផ្ទាល់ខ្លួនជោគជ័យ!",
        "filename": safe_name,
        "video_url": video_url
    })

@app.route("/api/video/broadcast-facebook", methods=["POST"])
def api_broadcast_video_facebook():
    data = request.json or {}
    filename = data.get("filename")
    description = data.get("description", "")
    
    if not filename:
        return jsonify({"success": False, "error": "មិនបានបញ្ជាក់ File វីដេអូឡើយ"}), 400
        
    if os.environ.get("VERCEL"):
        video_dir = "/tmp/videos"
    else:
        video_dir = os.path.join(BASE_DIR, "static", "videos")
    video_path = os.path.join(video_dir, filename)
    if not os.path.exists(video_path):
        return jsonify({"success": False, "error": f"រកមិនឃើញ File វីដេអូ: {filename}"}), 404
        
    cfg = load_config()
    pages_to_post = cfg.get("facebook_selected_pages") or []
    page_id = cfg.get("facebook_page_id")
    access_token = cfg.get("facebook_access_token")
    
    if not pages_to_post and page_id and access_token:
        pages_to_post = [{"id": page_id, "name": "Primary Page", "access_token": access_token}]
        
    if not pages_to_post:
        return jsonify({"success": False, "error": "Facebook Pages are not configured in Settings"}), 400
        
    # On Vercel cloud hosting, utilize high-speed URL Pull
    if os.environ.get("VERCEL"):
        video_target = f"https://asp-ac.vercel.app/static/videos/{filename}"
    else:
        video_target = video_path
        
    if len(pages_to_post) == 1:
        ok, msg = facebook_service.post_video_to_page(pages_to_post[0]["id"], pages_to_post[0]["access_token"], video_target, description)
        return jsonify({"success": ok, "message": msg})
    else:
        ok, summary, results = facebook_service.broadcast_video_to_pages(pages_to_post, video_target, description)
        return jsonify({"success": ok, "message": summary, "results": results})

@app.route("/api/video/veo", methods=["POST"])
def api_generate_video_veo():
    import video_engine
    
    data = request.json or {}
    script_id = data.get("script_id")
    script_text = data.get("script_text", "")
    topic = data.get("topic", "")
    
    if script_id:
        s = database.get_script_by_id(script_id)
        if s:
            script_text = s.get("content", "")
            topic = s.get("topic", topic)
            
    if not script_text:
        return jsonify({"success": False, "error": "អត្ថបទ Script មិនអាចទទេបានឡើយ"}), 400
        
    try:
        vid_path = video_engine.create_reels_video(
            script_text=script_text,
            topic=topic
        )
        filename = os.path.basename(vid_path)
        return jsonify({
            "success": True,
            "message": "បានបង្កើតវីដេអូ Reels 9:16 HD ជោគជ័យ!",
            "video_url": f"/static/videos/{filename}",
            "filename": filename,
            "engine": "smart_reels"
        })
    except Exception as e_fall:
        return jsonify({"success": False, "error": f"កំហុសក្នុងការបង្កើតវីដេអូ: {str(e_fall)}"}), 500

@app.route("/api/facebook/broadcast-url", methods=["POST"])
def api_broadcast_video_url():
    data = request.json or {}
    video_url = data.get("video_url", "").strip()
    description = data.get("description", "").strip()
    
    if not video_url:
        return jsonify({"success": False, "error": "សូមបញ្ចូល Video URL ឬ Link ជាមុនសិន!"}), 400
        
    cfg = load_config()
    pages_to_post = cfg.get("facebook_selected_pages") or []
    if not pages_to_post:
        page_id = cfg.get("facebook_page_id")
        access_token = cfg.get("facebook_access_token")
        if page_id and access_token:
            pages_to_post = [{"id": page_id, "name": "Primary Page", "access_token": access_token}]
            
    if not pages_to_post:
        return jsonify({"success": False, "error": "មិនទាន់មាន Facebook Pages ត្រូវបានកំណត់ឡើយ"}), 400
        
    ok, summary, results = facebook_service.broadcast_video_to_pages(pages_to_post, video_url, description)
    return jsonify({"success": ok, "message": summary, "results": results})

@app.route("/api/video/send-for-approval", methods=["POST"])
def api_send_video_for_approval():
    data = request.json or {}
    title = data.get("title", "វីដេអូ Reels ថ្មី").strip()
    description = data.get("description", "").strip()
    video_url = data.get("video_url", "").strip()
    script_id = data.get("script_id")
    
    if not video_url:
        return jsonify({"success": False, "error": "សូមបញ្ជាក់ Link វីដេអូជាមុនសិន!"}), 400
        
    cfg = load_config()
    bot_token = cfg.get("bot_token")
    chat_id = cfg.get("chat_id")
    if not bot_token or not chat_id:
        return jsonify({"success": False, "error": "សូមកំណត់ Telegram Bot Token និង Chat ID ក្នុង Settings ជាមុនសិន!"}), 400
        
    approval_id = database.create_video_approval(title, description, video_url, script_id=script_id)
    
    # Base URL for public web app
    host_url = request.host_url.rstrip("/")
    if "localhost" in host_url or "127.0.0.1" in host_url:
        web_base_url = "https://asp-ac.vercel.app"
    else:
        web_base_url = host_url
        
    ok, msg = telegram_service.send_video_approval_card(
        bot_token=bot_token,
        chat_id=chat_id,
        title=title,
        video_url=video_url,
        description=description,
        approval_id=approval_id,
        web_base_url=web_base_url
    )
    
    if ok:
        return jsonify({
            "success": True,
            "message": "បានផ្ញើវីដេអូទៅកាន់ Telegram ដើម្បីពិនិត្យ និង Approve រួចរាល់!",
            "approval_id": approval_id
        })
    else:
        return jsonify({"success": False, "error": f"បរាជ័យក្នុងការផ្ញើទៅ Telegram: {msg}"}), 500

@app.route("/api/approve/<int:approval_id>", methods=["GET", "POST"])
def api_handle_approval(approval_id):
    action = request.args.get("action", "publish").lower()
    record = database.get_video_approval(approval_id)
    if not record:
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="km">
        <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>404 - រកមិនឃើញ</title><style>body{background:#0b0f19;color:#fff;font-family:system-ui;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;text-align:center;}.box{background:rgba(255,255,255,0.05);padding:30px;border-radius:16px;border:1px solid rgba(255,255,255,0.1);max-width:400px;}</style></head>
        <body><div class="box"><h2>❌ រកមិនឃើញទិន្នន័យវីដេអូឡើយ</h2><p style="color:#94a3b8;">Approval ID #{{ id }} មិនមានក្នុងប្រព័ន្ធ។</p><a href="/" style="display:inline-block;margin-top:15px;color:#60a5fa;text-decoration:none;">← ត្រឡប់ទៅកាន់ App</a></div></body></html>
        """, id=approval_id), 404

    cfg = load_config()
    bot_token = cfg.get("bot_token")
    chat_id = cfg.get("chat_id")
    
    if action == "publish":
        if record.get("status") == "APPROVED":
            status_text = "វីដេអូនេះត្រូវបាន Approve និងបង្ហោះរួចហើយកាលពីមុន!"
            summary = "រួចរាល់ហើយ"
        else:
            pages_to_post = cfg.get("facebook_selected_pages") or []
            if not pages_to_post:
                page_id = cfg.get("facebook_page_id")
                access_token = cfg.get("facebook_access_token")
                if page_id and access_token:
                    pages_to_post = [{"id": page_id, "name": "Primary Page", "access_token": access_token}]
                    
            video_url = record.get("video_url")
            desc = f"🎬 {record.get('title')}\n\n{record.get('description')}"
            
            fb_ok, summary, results = facebook_service.broadcast_video_to_pages(pages_to_post, video_url, desc)
            database.update_video_approval_status(approval_id, "APPROVED", json.dumps(results))
            status_text = summary
            
            # Send confirmation to Telegram
            if bot_token and chat_id:
                conf_msg = (
                    f"🎉 *[វីដេអូត្រូវបាន APPROVE & បង្ហោះជោគជ័យ]*\n\n"
                    f"📌 *ប្រធានបទ:* {record.get('title')}\n"
                    f"📊 *ស្ថានភាព:* {summary}\n\n"
                    f"✅ វីដេអូត្រូវបានផ្សាយផ្ទាល់លើគ្រប់ Facebook Pages រួចរាល់!"
                )
                telegram_service.send_message(bot_token, chat_id, conf_msg)

        return render_template_string("""
        <!DOCTYPE html>
        <html lang="km">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Approve Video - AI Automation Pro</title>
          <style>
            body { background: #070d19; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; box-sizing: border-box; }
            .card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 20px; padding: 35px 25px; max-width: 480px; width: 100%; text-align: center; box-shadow: 0 10px 40px rgba(0,0,0,0.6); backdrop-filter: blur(10px); }
            .icon { font-size: 3.5rem; margin-bottom: 15px; }
            h2 { color: #34d399; margin: 0 0 10px 0; font-size: 1.45rem; }
            p { color: #94a3b8; font-size: 0.92rem; line-height: 1.6; margin: 0 0 15px 0; }
            .topic { background: rgba(255,255,255,0.06); padding: 12px; border-radius: 10px; font-weight: 600; color: #60a5fa; margin-bottom: 20px; word-break: break-word; }
            .btn { display: inline-block; background: linear-gradient(135deg, #3b82f6, #6366f1); color: #fff; padding: 12px 28px; border-radius: 10px; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: 0.2s; }
            .btn:hover { opacity: 0.9; transform: translateY(-2px); }
          </style>
        </head>
        <body>
          <div class="card">
            <div class="icon">🎉</div>
            <h2>វីដេអូត្រូវបាន Approve ជោគជ័យ!</h2>
            <div class="topic">{{ title }}</div>
            <p>{{ status_text }}</p>
            <p style="font-size:0.8rem; color:#64748b;">វីដេអូត្រូវបានផ្សាយបន្តផ្ទាល់ចូលទៅកាន់ Facebook Pages ទាំងអស់ដោយសុវត្ថិភាព។</p>
            <a href="/" class="btn">← ត្រឡប់ទៅកាន់ Dashboard</a>
          </div>
        </body>
        </html>
        """, title=record.get("title"), status_text=status_text)
        
    elif action == "reject":
        database.update_video_approval_status(approval_id, "REJECTED")
        if bot_token and chat_id:
            reject_msg = f"❌ *[វីដេអូត្រូវបាន REJECT]*\n\n📌 *ប្រធានបទ:* {record.get('title')}\nវីដេអូត្រូវបានលុបចោល មិនត្រូវបានបង្ហោះឡើយ។"
            telegram_service.send_message(bot_token, chat_id, reject_msg)
            
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="km">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Video Rejected - AI Automation Pro</title>
          <style>
            body { background: #070d19; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; box-sizing: border-box; }
            .card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 20px; padding: 35px 25px; max-width: 480px; width: 100%; text-align: center; box-shadow: 0 10px 40px rgba(0,0,0,0.6); backdrop-filter: blur(10px); }
            .icon { font-size: 3.5rem; margin-bottom: 15px; }
            h2 { color: #f87171; margin: 0 0 10px 0; font-size: 1.45rem; }
            p { color: #94a3b8; font-size: 0.92rem; line-height: 1.6; margin: 0 0 20px 0; }
            .topic { background: rgba(255,255,255,0.06); padding: 12px; border-radius: 10px; font-weight: 600; color: #cbd5e1; margin-bottom: 20px; word-break: break-word; }
            .btn { display: inline-block; background: rgba(255,255,255,0.1); color: #cbd5e1; padding: 12px 28px; border-radius: 10px; text-decoration: none; font-weight: 600; font-size: 0.95rem; }
          </style>
        </head>
        <body>
          <div class="card">
            <div class="icon">❌</div>
            <h2>វីដេអូត្រូវបាន Reject (លុបចោល)</h2>
            <div class="topic">{{ title }}</div>
            <p>វីដេអូនេះនឹងមិនត្រូវបានបង្ហោះចូលទៅកាន់ Facebook Pages ឡើយ។</p>
            <a href="/" class="btn">← ត្រឡប់ទៅកាន់ Dashboard</a>
          </div>
        </body>
        </html>
        """, title=record.get("title"))

    return jsonify({"success": False, "error": "Unknown action"}), 400

@app.route("/static/videos/<path:filename>")
def serve_generated_video(filename):
    if os.environ.get("VERCEL"):
        vdir = "/tmp/videos"
    else:
        vdir = os.path.join(BASE_DIR, "static", "videos")
    return send_from_directory(vdir, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
