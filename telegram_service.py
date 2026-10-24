import requests
import time

def split_message(text, max_len=3800):
    if not text or len(text) <= max_len:
        return [text] if text else []
    
    chunks = []
    paragraphs = text.split("\n\n")
    current_chunk = ""
    
    for p in paragraphs:
        if len(current_chunk) + len(p) + 2 <= max_len:
            current_chunk = (current_chunk + "\n\n" + p) if current_chunk else p
        else:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = ""
            if len(p) > max_len:
                lines = p.split("\n")
                for line in lines:
                    if len(current_chunk) + len(line) + 1 <= max_len:
                        current_chunk = (current_chunk + "\n" + line) if current_chunk else line
                    else:
                        if current_chunk:
                            chunks.append(current_chunk)
                        while len(line) > max_len:
                            chunks.append(line[:max_len])
                            line = line[max_len:]
                        current_chunk = line
            else:
                current_chunk = p
                
    if current_chunk:
        chunks.append(current_chunk)
        
    return chunks

def _send_single_chunk(bot_token, chat_id, chunk_text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": chunk_text,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=20)
        if response.status_code == 200:
            return True, "Message sent successfully"
            
        # Retry with plain text if markdown formatting failed
        if response.status_code == 400:
            payload.pop("parse_mode", None)
            retry_res = requests.post(url, json=payload, timeout=20)
            if retry_res.status_code == 200:
                return True, "Message sent successfully (plain-text)"
            return False, retry_res.json().get("description", "Telegram API Error")
            
        return False, response.json().get("description", f"HTTP {response.status_code}")
    except Exception as e:
        return False, str(e)

def send_message(bot_token, chat_id, text):
    bot_token = (bot_token or "").strip().strip("'").strip('"')
    chat_id = str(chat_id or "").strip()
    
    if not bot_token or not chat_id:
        return False, "Bot Token and Chat ID are required"
        
    chunks = split_message(text, max_len=3800)
    total = len(chunks)
    
    for i, chunk in enumerate(chunks):
        chunk_to_send = chunk
        if total > 1:
            header_prefix = f"📑 *[Part {i+1}/{total}]*\n\n"
            chunk_to_send = header_prefix + chunk
            
        ok, msg = _send_single_chunk(bot_token, chat_id, chunk_to_send)
        if not ok:
            # retry once
            time.sleep(1)
            ok, msg = _send_single_chunk(bot_token, chat_id, chunk_to_send)
            if not ok:
                return False, f"Part {i+1}/{total} error: {msg}"
                
        if i < total - 1:
            time.sleep(0.35)
            
    return True, f"Message sent successfully ({total} parts)" if total > 1 else "Message sent successfully"

def send_video_approval_card(bot_token, chat_id, title, video_url, description, approval_id, web_base_url):
    """
    Sends a video review card to Telegram with interactive inline buttons:
    - [ ✅ Approve & Broadcast to 23 Facebook Pages ]
    - [ 🎬 Watch Video Preview ]
    - [ ❌ Reject ]
    """
    import json
    import html
    bot_token = (bot_token or "").strip().strip("'").strip('"')
    chat_id = str(chat_id or "").strip()
    
    if not bot_token or not chat_id:
        return False, "Bot Token and Chat ID are required"
        
    if not video_url.startswith("http://") and not video_url.startswith("https://"):
        full_video_url = f"{web_base_url}{video_url if video_url.startswith('/') else '/' + video_url}"
    else:
        full_video_url = video_url

    publish_url = f"{web_base_url}/api/approve/{approval_id}?action=publish"
    reject_url = f"{web_base_url}/api/approve/{approval_id}?action=reject"
    
    safe_title = html.escape(str(title or "Reels Video"))
    raw_desc = str(description or "")[:350]
    if len(str(description or "")) > 350:
        raw_desc += "..."
    safe_desc = html.escape(raw_desc)
    safe_video_url = html.escape(full_video_url)
        
    text = (
        f"🎬 <b>[វីដេអូថ្មីរួចរាល់សម្រាប់ពិនិត្យ & APPROVE]</b>\n\n"
        f"📌 <b>ប្រធានបទ:</b> {safe_title}\n"
        f"⏱ <b>ទម្រង់:</b> Reels / TikTok / Shorts (9:16 Vertical HD)\n\n"
        f"📝 <b>Caption:</b>\n{safe_desc}\n\n"
        f"🔗 <b>មើលវីដេអូ:</b> <a href=\"{safe_video_url}\">{safe_video_url}</a>\n\n"
        f"👇 <b>សូមពិនិត្យមើលវីដេអូរួចចុចប៊ូតុងខាងក្រោមដើម្បីសម្រេចចិត្ត៖</b>"
    )
    
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "✅ Approve & បង្ហោះចូល Facebook ២៣ Pages", "url": publish_url}
            ],
            [
                {"text": "🎬 Watch Video Preview", "url": full_video_url},
                {"text": "❌ Reject (កុំបង្ហោះ)", "url": reject_url}
            ]
        ]
    }
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": reply_markup
    }
    
    try:
        res = requests.post(url, json=payload, timeout=20)
        if res.status_code == 200:
            return True, "Approval card sent to Telegram successfully"
        # fallback without parse_mode if error
        payload.pop("parse_mode", None)
        payload["text"] = f"[វីដេអូថ្មី] {title}\nមើលវីដេអូ: {full_video_url}\n{raw_desc}"
        retry_res = requests.post(url, json=payload, timeout=20)
        if retry_res.status_code == 200:
            return True, "Approval card sent to Telegram (plain-text)"
        return False, retry_res.json().get("description", f"HTTP {res.status_code}")
    except Exception as e:
        return False, str(e)

