import requests

def send_message(bot_token, chat_id, text):
    bot_token = (bot_token or "").strip().strip("'").strip('"')
    chat_id = str(chat_id or "").strip()
    
    if not bot_token or not chat_id:
        return False, "Bot Token and Chat ID are required"
        
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        if response.status_code == 200:
            return True, "Message sent successfully"
            
        # Retry with plain text if markdown parsing failed (HTTP 400)
        if response.status_code == 400:
            payload.pop("parse_mode", None)
            retry_res = requests.post(url, json=payload, timeout=15)
            if retry_res.status_code == 200:
                return True, "Message sent successfully (plain-text)"
            return False, retry_res.json().get("description", "Telegram API Error")
            
        return False, response.json().get("description", f"HTTP {response.status_code}")
    except Exception as e:
        return False, str(e)
