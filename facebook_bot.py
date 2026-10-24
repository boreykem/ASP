"""
Facebook Page & Meta Business Suite Automation Engine
=====================================================
- Uses undetected-chromedriver (uc) to bypass Facebook Bot Detections & Checkpoints.
- Saves persistent user data and session cookies in 'fb_chrome_profile'.
- You log in manually ONCE (with 2FA / Password) and subsequent launches retain login status.
- Direct navigation to Meta Business Suite Composer & Facebook Reels Creator.
"""

import os
import sys
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

PROFILE_DIR_NAME = "fb_chrome_profile"

def get_profile_path():
    """បង្កើត ឬទាញយក Path សម្រាប់ផ្ទុក Profile និង Session Cookies របស់ Facebook"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    profile_path = os.path.join(base_dir, PROFILE_DIR_NAME)
    os.makedirs(profile_path, exist_ok=True)
    return profile_path

def setup_browser(headless=False):
    """
    រៀបចំ undetected-chromedriver ជាមួយ Settings ការពារការចាប់ Bot របស់ Facebook
    """
    print("⚙️  កំពុងកំណត់ជម្រើស (Browser Options)...")
    options = uc.ChromeOptions()
    
    # បិទផ្ទាំង Notifications/Popups និងបើកពេញអេក្រង់
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    # រក្សាទុក Login Profile របស់ Facebook
    profile_path = get_profile_path()
    options.add_argument(f"--user-data-dir={profile_path}")
    print(f"📁 Facebook Profile Directory: {profile_path}")
    
    if headless:
        options.add_argument("--headless=new")
        print("🕶️  ដំណើរការជារបៀប Headless (លាក់ផ្ទាំង Browser)")
    else:
        print("🖥️  ដំណើរការជារបៀបធម្មតា (បង្ហាញផ្ទាំង Browser)")
        
    try:
        driver = uc.Chrome(options=options, use_subprocess=True)
        return driver
    except Exception as e:
        print(f"❌ មិនអាចបើក Chrome បានទេ: {e}")
        print("💡 សូមប្រាកដថាអ្នកបានបិទផ្ទាំង Chrome ទាំងអស់ជាមុនសិន ប្រសិនបើមានប្រើ Profile ដូចគ្នា។")
        raise e

def is_fb_logged_in(driver):
    """ពិនិត្យមើលថាតើគណនី Facebook បាន Login រួចរាល់ហើយឬនៅ"""
    try:
        cookies = driver.get_cookies()
        for cookie in cookies:
            # 'c_user' គឺជា Cookie សំខាន់របស់ Facebook ដែលបញ្ជាក់ពី User ID នៅពេល Log in រួច
            if cookie.get("name") == "c_user":
                return True
        return False
    except Exception:
        return False

def open_facebook_login():
    """របៀបទី ១៖ បើក Facebook Login & រក្សាទុក Session"""
    driver = setup_browser(headless=False)
    try:
        print("\n" + "=" * 60)
        print("🚀 កំពុងចូលទៅកាន់ទំព័រ Login របស់ Facebook...")
        print("=" * 60)
        driver.get("https://www.facebook.com/login")
        
        print("\n💡 [ការណែនាំ]៖")
        print("   ១. សូមបញ្ចូល Email/Password និងកូដ 2FA លើផ្ទាំង Browser ដែលទើបនឹងបើក។")
        print("   ២. នៅពេល Facebook សួរថា 'Remember browser?' សូមជ្រើសរើស Save / Remember។")
        print("   ៣. ប្រព័ន្ធនឹងចាប់ដឹងដោយស្វ័យប្រវត្តនៅពេលអ្នក Log in រួចរាល់។\n")
        
        # តាមដានរង់ចាំរហូតដល់អ្នកប្រើប្រាស់ Login រួច (រង់ចាំអតិបរមា ៣ នាទី)
        max_wait_seconds = 180
        start_time = time.time()
        logged_in = False
        
        while time.time() - start_time < max_wait_seconds:
            if is_fb_logged_in(driver):
                logged_in = True
                print("🎉 បានរកឃើញថាអ្នកបាន Log in ចូល Facebook ជោគជ័យ!")
                break
            time.sleep(3)
            
        if not logged_in:
            print("⚠️ ផុតកំណត់រង់ចាំ (៣ នាទី)។ ប្រសិនបើអ្នក Log in រួចហើយ Cookies ត្រូវបានរក្សាទុករួចរាល់។")
            
        time.sleep(4)
    except Exception as e:
        print(f"❌ មានបញ្ហា: {e}")
    finally:
        input("\n👉 ចុច [Enter] ដើម្បីបិទ Browser...")
        driver.quit()
        print("🔒 បានបិទ Browser រួចរាល់!")

def open_meta_business_suite():
    """របៀបទី ២៖ ចូលទៅកាន់ Meta Business Suite (ទំព័របង្កើត Post របស់ Page)"""
    driver = setup_browser(headless=False)
    try:
        url = "https://business.facebook.com/latest/composer"
        print(f"\n🚀 កំពុងចូលទៅកាន់ Meta Business Suite Composer: {url}")
        driver.get(url)
        
        print("⏳ កំពុងរង់ចាំទំព័រដំណើរការ...")
        time.sleep(12)
        
        print(f"📌 ចំណងជើងទំព័រ: {driver.title}")
        print("💡 ទំព័រ Meta Business Suite ត្រូវបានបើកដោយជោគជ័យដោយប្រើ Session ដែលបានរក្សាទុក។")
    except Exception as e:
        print(f"❌ មានបញ្ហា: {e}")
    finally:
        input("\n👉 ចុច [Enter] ដើម្បីបិទ Browser...")
        driver.quit()
        print("🔒 បានបិទ Browser រួចរាល់!")

def open_meta_reels_composer():
    """របៀបទី ៣៖ ចូលទៅកាន់ Meta Business Suite Reels Creator (សម្រាប់ Upload Reels)"""
    driver = setup_browser(headless=False)
    try:
        url = "https://business.facebook.com/latest/reels_composer"
        print(f"\n🚀 កំពុងចូលទៅកាន់ Meta Reels Creator: {url}")
        driver.get(url)
        
        print("⏳ កំពុងរង់ចាំទំព័រ Reels ដំណើរការ...")
        time.sleep(12)
        
        print(f"📌 ចំណងជើងទំព័រ: {driver.title}")
    except Exception as e:
        print(f"❌ មានបញ្ហា: {e}")
    finally:
        input("\n👉 ចុច [Enter] ដើម្បីបិទ Browser...")
        driver.quit()
        print("🔒 បានបិទ Browser រួចរាល់!")

def open_facebook_page(page_url):
    """របៀបទី ៤៖ ចូលទៅកាន់ Facebook Page ផ្ទាល់"""
    driver = setup_browser(headless=False)
    try:
        print(f"\n🌐 កំពុងចូលទៅកាន់ Facebook Page: {page_url}")
        driver.get(page_url)
        time.sleep(8)
        print(f"✅ បានចូលទៅកាន់ {driver.title} ដោយជោគជ័យ!")
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
        print("📘 FACEBOOK PAGE & META BUSINESS SUITE AUTOMATION")
        print("=" * 60)
        print("1. 🔑 បើក Facebook Login (បញ្ចូលគណនី & រក្សាទុក Session)")
        print("2. 📝 បើក Meta Business Suite Post Composer (បង្កើត Post លើ Page)")
        print("3. 🎬 បើក Meta Business Suite Reels Creator (Upload Reels)")
        print("4. 📄 បើកទំព័រ Facebook Page ផ្ទាល់")
        print("5. ❌ ចាកចេញ (Exit)")
        print("=" * 60)
        
        choice = input("👉 សូមជ្រើសរើសជម្រើស (1-5): ").strip()
        
        if choice == "1":
            open_facebook_login()
        elif choice == "2":
            open_meta_business_suite()
        elif choice == "3":
            open_meta_reels_composer()
        elif choice == "4":
            page = input("🔗 សូមបញ្ចូល Link Facebook Page (ឧទាហរណ៍ https://facebook.com/yourpage): ").strip()
            if page:
                if not page.startswith("http"):
                    page = "https://" + page
                open_facebook_page(page)
        elif choice == "5":
            print("👋 សូមអរគុណ! បានចាកចេញពីកម្មវិធី។")
            break
        else:
            print("⚠️ ជម្រើសមិនត្រឹមត្រូវ សូមជ្រើសរើសម្ដងទៀត!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "login":
            open_facebook_login()
        elif arg in ["composer", "post"]:
            open_meta_business_suite()
        elif arg == "reels":
            open_meta_reels_composer()
        else:
            open_facebook_page(arg)
    else:
        main_menu()
