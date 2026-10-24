"""
TikTok & Anti-Bot Web Automation Engine
========================================
- Uses undetected-chromedriver (uc) to bypass Cloudflare, Akamai, and TikTok Anti-Bot detections.
- Saves persistent user data and session cookies in a local profile directory.
- Supports manual first-time login (QR / credentials) with automatic session reuse.
"""

import os
import sys
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROFILE_DIR_NAME = "tiktok_chrome_profile"

def get_profile_path():
    """បង្កើត ឬទាញយក Path សម្រាប់ផ្ទុក Profile និង Session Cookies របស់ Chrome"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    profile_path = os.path.join(base_dir, PROFILE_DIR_NAME)
    os.makedirs(profile_path, exist_ok=True)
    return profile_path

def setup_browser(headless=False):
    """
    រៀបចំ undetected-chromedriver ជាមួយ Settings ការពារការចាប់ Bot
    """
    print("⚙️  កំពុងកំណត់ជម្រើស (Browser Options)...")
    options = uc.ChromeOptions()
    
    # បិទផ្ទាំង Popup និងបើកពេញអេក្រង់
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    # រក្សាទុក Login Profile
    profile_path = get_profile_path()
    options.add_argument(f"--user-data-dir={profile_path}")
    print(f"📁 Profile Directory: {profile_path}")
    
    if headless:
        options.add_argument("--headless=new")
        print("🕶️  ដំណើរការជារបៀប Headless (លាក់ផ្ទាំង Browser)")
    else:
        print("🖥️  ដំណើរការជារបៀបធម្មតា (បង្ហាញផ្ទាំង Browser)")
        
    # ចាប់ផ្តើម undetected-chromedriver
    # use_subprocess=True ការពារកុំឱ្យ Chrome crash នៅលើ Windows
    try:
        driver = uc.Chrome(options=options, use_subprocess=True)
        return driver
    except Exception as e:
        print(f"❌ មិនអាចបើក Chrome បានទេ: {e}")
        print("💡 សូមប្រាកដថាអ្នកបានបិទផ្ទាំង Chrome ទាំងអស់ជាមុនសិន ប្រសិនបើមានប្រើ Profile ដូចគ្នា។")
        raise e

def is_logged_in(driver):
    """ពិនិត្យមើលថាតើ TikTok បាន Login រួចរាល់ហើយឬនៅ"""
    try:
        # ប្រសិនបើមានប៊ូតុង Profile ឬ Avatar ឬគ្មានប៊ូតុង Login ធំ
        current_url = driver.current_url.lower()
        if "login" in current_url:
            return False
            
        # ពិនិត្យ Cookies សំខាន់ៗរបស់ TikTok (sessionid)
        cookies = driver.get_cookies()
        for cookie in cookies:
            if cookie.get("name") in ["sessionid", "sid_tt", "sessionid_ss"]:
                return True
        return False
    except Exception:
        return False

def open_tiktok_login():
    """របៀបទី ១៖ បើកទំព័រ Login និងរក្សាទុក Session"""
    driver = setup_browser(headless=False)
    try:
        print("\n" + "=" * 60)
        print("🚀 កំពុងចូលទៅកាន់ទំព័រ Login របស់ TikTok...")
        print("=" * 60)
        driver.get("https://www.tiktok.com/login")
        
        print("\n💡 [ការណែនាំ]៖")
        print("   ១. សូមស្កេន QR Code ឬបញ្ចូលគណនីរបស់អ្នកលើផ្ទាំង Browser ដែលទើបនឹងបើក។")
        print("   ២. ប្រសិនបើមាន Captcha (ផ្គុំរូបភាព) សូមដោះស្រាយវាដោយដៃ។")
        print("   ៣. នៅពេល Login ជោគជ័យ ប្រព័ន្ធនឹងរក្សាទុក Session ដោយស្វ័យប្រវត្ត។\n")
        
        # តាមដានរង់ចាំរហូតដល់អ្នកប្រើប្រាស់ Login រួច
        max_wait_seconds = 180
        start_time = time.time()
        logged_in = False
        
        while time.time() - start_time < max_wait_seconds:
            if is_logged_in(driver):
                logged_in = True
                print("🎉 បានរកឃើញថាអ្នកបាន Log in ជោគជ័យ!")
                break
            time.sleep(3)
            
        if not logged_in:
            print("⚠️ ផុតកំណត់រង់ចាំ (៣ នាទី)។ ប្រសិនបើអ្នក Log in រួចហើយ Cookies ត្រូវបានរក្សាទុករួចរាល់។")
            
        time.sleep(5)
    except Exception as e:
        print(f"❌ មានបញ្ហា: {e}")
    finally:
        input("\n👉 ចុច [Enter] ដើម្បីបិទ Browser...")
        driver.quit()
        print("🔒 បានបិទ Browser រួចរាល់!")

def open_tiktok_creator():
    """របៀបទី ២៖ ចូលទៅកាន់ Creator Center / Studio (សម្រាប់ Upload វីដេអូ)"""
    driver = setup_browser(headless=False)
    try:
        url = "https://www.tiktok.com/creator-center/upload?from=upload"
        print(f"\n🚀 កំពុងចូលទៅកាន់ TikTok Studio Upload: {url}")
        driver.get(url)
        
        print("⏳ កំពុងរង់ចាំទំព័រដំណើរការ...")
        time.sleep(10)
        
        print(f"📌 ចំណងជើងទំព័រ: {driver.title}")
        print("💡 ទំព័រ Creator Center ត្រូវបានបើកដោយជោគជ័យដោយប្រើ Session ដែលបានរក្សាទុក។")
    except Exception as e:
        print(f"❌ មានបញ្ហា: {e}")
    finally:
        input("\n👉 ចុច [Enter] ដើម្បីបិទ Browser...")
        driver.quit()
        print("🔒 បានបិទ Browser រួចរាល់!")

def open_custom_url(url):
    """របៀបទី ៣៖ បើកវិបសាយណាមួយដោយឆ្លងកាត់ Anti-Bot"""
    driver = setup_browser(headless=False)
    try:
        print(f"\n🌐 កំពុងចូលទៅកាន់: {url}")
        driver.get(url)
        time.sleep(8)
        print(f"✅ បានចូលទៅកាន់ {driver.title} ({url}) ដោយជោគជ័យ!")
    except Exception as e:
        print(f"❌ មានបញ្ហា: {e}")
    finally:
        input("\n👉 ចុច [Enter] ដើម្បីបិទ Browser...")
        driver.quit()
        print("🔒 បានបិទ Browser រួចរាល់!")

def main_menu():
    """ម៉ឺនុយបញ្ជាសម្រាប់អ្នកប្រើប្រាស់"""
    while True:
        print("\n" + "=" * 60)
        print("🤖 TIKTOK & ANTI-BOT BROWSER AUTOMATION")
        print("=" * 60)
        print("1. 🔑 បើក TikTok Login (ស្កេន QR / បញ្ចូល Password & រក្សាទុក Session)")
        print("2. 📤 បើក TikTok Creator Studio (ទំព័រ Upload វីដេអូ)")
        print("3. 🌐 បើកវិបសាយផ្សេងៗ (Bypass Cloudflare / Anti-Bot)")
        print("4. ❌ ចាកចេញ (Exit)")
        print("=" * 60)
        
        choice = input("👉 សូមជ្រើសរើសជម្រើស (1-4): ").strip()
        
        if choice == "1":
            open_tiktok_login()
        elif choice == "2":
            open_tiktok_creator()
        elif choice == "3":
            target_url = input("🔗 សូមបញ្ចូល URL (ឧទាហរណ៍ https://nowsecure.nl): ").strip()
            if target_url:
                if not target_url.startswith("http"):
                    target_url = "https://" + target_url
                open_custom_url(target_url)
        elif choice == "4":
            print("👋 សូមអរគុណ! បានចាកចេញពីកម្មវិធី។")
            break
        else:
            print("⚠️ ជម្រើសមិនត្រឹមត្រូវ សូមជ្រើសរើសម្ដងទៀត!")

if __name__ == "__main__":
    # ប្រសិនបើហៅកូដជាមួយ Argument ឧទាហរណ៍ `python tiktok_bot.py login`
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "login":
            open_tiktok_login()
        elif arg == "upload":
            open_tiktok_creator()
        else:
            open_custom_url(arg)
    else:
        main_menu()
