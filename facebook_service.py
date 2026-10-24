"""
Meta Graph API Service for Facebook Page Automation
===================================================
- Allows posting scripts, updates, and articles to a Facebook Page via Graph API.
- Safe, official, serverless-friendly (runs 24/7 on Cloud / Vercel / VPS).
- Handles text formatting, verification, and informative error descriptions.
"""

import requests
import json

GRAPH_API_VERSION = "v19.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"

def verify_page_connection(page_id, access_token):
    """
    ផ្ទៀងផ្ទាត់ថាតើ Page ID និង Page Access Token ត្រឹមត្រូវ និងដំណើរការឬទេ
    """
    page_id = (page_id or "").strip()
    access_token = (access_token or "").strip()
    
    if not page_id or not access_token:
        return False, "Page ID និង Access Token មិនអាចទទេបានឡើយ (Required)"
        
    url = f"{GRAPH_API_BASE}/{page_id}"
    params = {
        "fields": "id,name,link,is_published",
        "access_token": access_token
    }
    
    try:
        res = requests.get(url, params=params, timeout=15)
        data = res.json()
        
        if res.status_code == 200 and "id" in data:
            page_name = data.get("name", "Facebook Page")
            return True, f"ភ្ជាប់ទៅកាន់ Page '{page_name}' (ID: {page_id}) ជោគជ័យ!"
            
        error = data.get("error", {})
        err_msg = error.get("message", f"HTTP {res.status_code}")
        return False, f"កំហុស Meta API: {err_msg}"
    except Exception as e:
        return False, f"បញ្ហាភ្ជាប់បណ្តាញ: {str(e)}"

def post_to_page(page_id, access_token, message, link=None):
    """
    បង្ហោះអត្ថបទ ឬស្គ្រីបចូលទៅកាន់ Facebook Page Feed
    """
    page_id = (page_id or "").strip()
    access_token = (access_token or "").strip()
    
    if not page_id or not access_token:
        return False, "មិនទាន់បានកំណត់ Facebook Page ID ឬ Access Token ឡើយ"
        
    if not message or not message.strip():
        return False, "អត្ថបទសារមិនអាចទទេបានឡើយ"
        
    url = f"{GRAPH_API_BASE}/{page_id}/feed"
    payload = {
        "message": message,
        "access_token": access_token
    }
    if link:
        payload["link"] = link
        
    try:
        res = requests.post(url, data=payload, timeout=25)
        data = res.json()
        
        if res.status_code == 200 and "id" in data:
            post_id = data.get("id")
            return True, f"បានបង្ហោះលើ Facebook Page ជោគជ័យ (Post ID: {post_id})"
            
        error = data.get("error", {})
        err_msg = error.get("message", f"HTTP {res.status_code}")
        err_code = error.get("code")
        
        if err_code == 190:
            return False, "Access Token ផុតកំណត់ (Expired Token)។ សូមបង្កើត Page Access Token ថ្មី។"
        elif err_code == 200:
            return False, "គណនីគ្មានសិទ្ធិបង្ហោះ (Missing pages_manage_posts permission)។"
            
        return False, f"បរាជ័យក្នុងការបង្ហោះ: {err_msg}"
    except Exception as e:
        return False, f"បញ្ហាភ្ជាប់បណ្តាញ: {str(e)}"

def get_user_pages(access_token):
    """
    ទាញយកបញ្ជី Facebook Pages ទាំងអស់ដែលគណនីនេះគ្រប់គ្រង (ព្រមទាំង Page Access Tokens ផ្ទាល់)
    """
    access_token = (access_token or "").strip()
    if not access_token:
        return False, "Access Token មិនអាចទទេបានឡើយ", []
        
    url = f"{GRAPH_API_BASE}/me/accounts"
    params = {
        "access_token": access_token,
        "limit": 100
    }
    try:
        res = requests.get(url, params=params, timeout=20)
        data = res.json()
        if res.status_code == 200 and "data" in data:
            raw_pages = data["data"]
            pages = []
            for p in raw_pages:
                pages.append({
                    "id": p.get("id"),
                    "name": p.get("name"),
                    "category": p.get("category"),
                    "access_token": p.get("access_token"),
                    "tasks": p.get("tasks", [])
                })
            return True, f"បានរកឃើញ {len(pages)} Facebook Pages!", pages
            
        err = data.get("error", {})
        return False, err.get("message", f"HTTP {res.status_code}"), []
    except Exception as e:
        return False, str(e), []
