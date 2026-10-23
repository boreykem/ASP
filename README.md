# 🚀 AI Script Automation Pro

ប្រព័ន្ធស្វ័យប្រវត្តសម្រាប់បង្កើតស្គ្រីបវីដេអូ AI (Gemini AI) និងផ្ញើចូល Telegram ដោយស្វ័យប្រវត្តិ ព្រមទាំងគាំទ្រទម្រង់ **Google NotebookLM Video Overview (Explainer Video ៥+ នាទី)**។

---

## 🌟 លក្ខណៈពិសេសចម្បង (Key Features)

* **🎬 NotebookLM Video Overview (5+ Minutes):** បង្កើតស្គ្រីប Explainer Video ៧ ឈុតឆាកលម្អិត សំឡេងអានជាភាសាខ្មែរ ១០០% និងស្លាយ/CC ជាភាសាអង់គ្លេស (ការពារបញ្ហា Font ចេញប្រអប់ការេ `▯▯▯`)។
* **🎙️ NotebookLM Podcast:** ស្គ្រីបកិច្ចសន្ទនាស៊ីជម្រៅរវាងពិធីករ ២ នាក់ជាភាសាខ្មែរសុទ្ធសាធ។
* **📱 TikTok / Reels / Shorts & YouTube:** ស្គ្រីបវីដេអូខ្លីទាក់ទាញ ៣ វិនាទីដំបូង (Hook & Catchy)។
* **🌐 7 Rotating Daily Niches:** បង្វិល ៥ ប្រធានបទប្លែកៗគ្នាប្រចាំថ្ងៃពី ៧ វិស័យ (អប់រំ, សេដ្ឋកិច្ច, សង្គម, វិទ្យាសាស្ត្រ, កសិកម្ម, សកលលោក, សាសនា)។
* **✈️ Telegram Broadcast:** ផ្ញើស្គ្រីបចូល Telegram Channel/Group ភ្លាមៗក្រោយពេលបង្កើតរួច។
* **⏰ Background Scheduler:** ប្រព័ន្ធដំណើរការកាលវិភាគស្វ័យប្រវត្តប្រចាំថ្ងៃ។
* **☁️ Deploy Ready:** គាំទ្រការដាក់លើ **Vercel**, **Render**, **Railway**, និង **Local PC**។

---

## 🚀 របៀបតម្លើង និងដំណើរការលើកុំព្យូទ័រ (Local Development)

1. **ដំឡើង Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **ដំណើរការ Server:**
   ```bash
   python main.py
   ```

3. **បើក Browser:**
   ចូលទៅកាន់ `http://127.0.0.1:5000`

---

## ☁️ របៀប Deploy ទៅកាន់ Vercel

1. **Push កូដទៅកាន់ GitHub** (មើលការណែនាំខាងក្រោម)។
2. ចូលទៅកាន់ [Vercel Dashboard](https://vercel.com/)។
3. ចុច **Add New Project** -> **Import** Repository GitHub របស់អ្នក។
4. (Optional) កំណត់ Environment Variables ក្នុង Vercel Settings៖
   * `GEMINI_API_KEY`: API Key របស់ Gemini
   * `TELEGRAM_BOT_TOKEN`: Token របស់ Telegram Bot
   * `TELEGRAM_CHAT_ID`: Chat ID របស់អ្នក
5. ចុច **Deploy** -> រួចរាល់!

---

## 🛠️ រចនាសម្ព័ន្ធ Project

```text
├── api/
│   └── index.py            # Vercel Serverless Entrypoint
├── static/
│   ├── css/style.css       # Kantumruy Pro & Glassmorphism UI
│   └── js/app.js           # Frontend Logic & Translations
├── templates/
│   └── index.html          # Responsive Web Interface
├── ai_service.py           # Google Gemini AI Integration
├── app.py                  # Flask Web Server & API Routes
├── database.py             # SQLite Script Storage
├── telegram_service.py     # Telegram Bot Messenger
├── topics_engine.py        # 7 Niches Daily Topics Rotation
├── vercel.json             # Vercel Configuration & Rewrites
├── Procfile                # Gunicorn configuration
└── requirements.txt        # Python Dependencies
```
