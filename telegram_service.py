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

