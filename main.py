import os
import sys
import webbrowser
import threading
import socket
from app import app

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def open_browser(port):
    import time
    time.sleep(1.2)
    try:
        webbrowser.open(f"http://127.0.0.1:{port}")
    except Exception:
        pass

if __name__ == "__main__":
    local_ip = get_local_ip()
    port = int(os.environ.get("PORT", 5000))
    
    print("\n" + "=" * 65)
    print("🚀 AI Script Automation Pro - Web Server Started!")
    print(f"💻 Desktop / PC:       http://127.0.0.1:{port}")
    print(f"📱 Mobile Phone (Wi-Fi): http://{local_ip}:{port}")
    print("=" * 65 + "\n")
    
    # Auto open browser on local launch
    if not os.environ.get("NO_BROWSER"):
        threading.Thread(target=open_browser, args=(port,), daemon=True).start()
        
    app.run(host="0.0.0.0", port=port, debug=False)
