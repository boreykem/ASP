/**
 * AI Script Automation Pro - Frontend Reactive Logic
 * Dual Language (Khmer & English with 1-Click Switch)
 * 7 Core Rotating Categories & Daily Auto-Topics
 * 4 Dedicated Tabs: Generator, History, Auto-Scheduler, Settings
 */

// ==========================================
// Translation Dictionary (Khmer ↔ English)
// ==========================================
const translations = {
  km: {
    appTitle: "AI Script Automation Pro",
    appSubtitle: "ប្រព័ន្ធបង្កើតស្គ្រីបវីដេអូ AI & ផ្ញើចូល Telegram ស្វ័យប្រវត្តិ",
    langButton: "English",
    langFlag: "🇬🇧",
    tabGenerator: "បង្កើតស្គ្រីប",
    tabHistory: "ប្រវត្តិស្គ្រីប",
    tabScheduler: "កាលវិភាគស្វ័យប្រវត្តិ",
    tabSettings: "ការកំណត់",
    
    settingsTitle: "ការកំណត់ API (Settings)",
    settingsDesc: "កំណត់ API Key សម្រាប់ Gemini AI និង Telegram Bot របស់អ្នកដើម្បីដំណើរការប្រព័ន្ធ។",
    btnSaveSettings: "រក្សាទុក",
    btnSaveBottom: "រក្សាទុកការកំណត់ទាំងអស់",
    settingsSecurityTitle: "សុវត្ថិភាពទិន្នន័យ៖",
    settingsSecurityDesc: "ទិន្នន័យ API Key និង Token ទាំងអស់ត្រូវបានរក្សាទុកតែលើ Server ផ្ទាល់ខ្លួនរបស់អ្នកប៉ុណ្ណោះ គ្មាននរណាម្នាក់អាចមើលឃើញឡើយ។",
    lblGeminiKey: "Gemini API Key:",
    lblBotToken: "Telegram Bot Token:",
    lblChatId: "Telegram Chat ID:",
    
    formatTitle: "ទម្រង់វីដេអូ និងទឹកដមសម្លេង",
    lblFormat: "ទម្រង់ (Format):",
    lblTone: "ទឹកដម (Tone):",
    
    notebooklmCardTitle: "ការកំណត់ឱ្យ NotebookLM និយាយខ្មែរ ១០០%",
    notebooklmDesc: "✨ <strong>គន្លឹះដោះស្រាយបញ្ហា NotebookLM និយាយអង់គ្លេស៖</strong> គ្រប់ស្គ្រីបទាំងអស់ត្រូវបានបង្កប់កូដបញ្ជា <strong>Strict Khmer Directive</strong> នៅខាងលើគេដោយស្វ័យប្រវត្ត។ នៅពេលអ្នកបញ្ចូលស្គ្រីបទៅក្នុង NotebookLM ដើម្បីបង្កើត Video/Audio Overview សូមចុចប៊ូតុង <strong>Customize</strong> (ក្នុង Studio) រួចបិទភ្ជាប់ (Paste) Prompt ខាងក្រោមនេះ នោះ AI Hosts នឹងនិយាយជាភាសាខ្មែរ ១០០% ជានិច្ច៖",
    btnCopyNotebooklmPrompt: "ចម្លង Prompt សម្រាប់ NotebookLM Customize",
    btnCopyNotebooklm: "ចម្លងសម្រាប់ NotebookLM",
    msgNotebooklmPromptCopied: "បានចម្លង Prompt សម្រាប់ NotebookLM Customize រួចរាល់!",
    msgNotebooklmScriptCopied: "បានចម្លងស្គ្រីបសម្រាប់ NotebookLM (និយាយខ្មែរ ១០០%)!",
    
    categoriesTitle: "វិស័យធំៗទាំង ៧ សម្រាប់បង្វិលប្រធានបទប្រចាំថ្ងៃ",
    catEducation: "ការអប់រំ",
    catEconomy: "សេដ្ឋកិច្ច & ហិរញ្ញវត្ថុ",
    catSociety: "សង្គម & ជីវិត",
    catScience: "វិទ្យាសាស្ត្រ & បច្ចេកវិទ្យា",
    catAgriculture: "កសិកម្មទំនើប",
    catUniverse: "ការរកឃើញសកលលោក",
    catReligion: "សាសនា & ទស្សនវិជ្ជា",
    
    topicsTitle: "ប្រធានបទស្គ្រីបប្រចាំថ្ងៃ (៥ ស្គ្រីប)",
    btnRefreshTopics: "ប្តូរ ៥ ប្រធានបទថ្មី",
    btnClearTopics: "សម្អាត",
    topicsSubtext: "💡 <strong>ចំណាំ៖</strong> ប្រធានបទទាំង ៥ នេះនឹងប្តូរថ្មីៗជារៀងរាល់ថ្ងៃដោយស្វ័យប្រវត្តិ។ លោកអ្នកអាចកែសម្រួល ឬវាយប្រធានបទផ្ទាល់ខ្លួនបានគ្រប់ពេល។",
    topicPlaceholder: "ប្រធានបទ (ស្វ័យប្រវត្តិ)",
    
    btnRun: "ចាប់ផ្តើមបង្កើតស្គ្រីប និងផ្ញើចូល Telegram",
    btnRunning: "🚀 កំពុងដំណើរការ...",
    
    logsTitle: "ដំណើរការ (Live Logs)",
    btnClearLogs: "សម្អាត",
    sysReady: "[ប្រព័ន្ធ] រួចរាល់សម្រាប់ដំណើរការ...",
    
    historyTitle: "ប្រវត្តិស្គ្រីបទាំងអស់ក្នុង Database",
    historySearchPlaceholder: "ស្វែងរកតាមប្រធានបទ ឬខ្លឹមសារ...",
    thDate: "កាលបរិច្ឆេទ",
    thTopic: "ប្រធានបទ",
    thAction: "សកម្មភាព",
    btnCopy: "ចម្លងស្គ្រីប",
    btnResend: "ផ្ញើចូល Telegram",
    btnDelete: "លុប",
    
    schedCardTitle: "ការកំណត់កាលវិភាគស្វ័យប្រវត្តប្រចាំថ្ងៃ",
    schedEnableTitle: "ដំណើរការស្វ័យប្រវត្តរាល់ថ្ងៃ (Daily Auto-Run)",
    schedEnableDesc: "កម្មវិធីនឹងបង្កើត និងផ្ញើស្គ្រីបទាំង ៥ ចូល Telegram ជារៀងរាល់ថ្ងៃតាមម៉ោងដែលបានកំណត់។",
    lblSchedTime: "ម៉ោងដំណើរការជារៀងរាល់ថ្ងៃ (HH:MM):",
    lblSchedAutoNiche: "បង្វិល ៥ ប្រធានបទប្លែកៗគ្នាជារៀងរាល់ថ្ងៃពី ៧ វិស័យ (អប់រំ, សេដ្ឋកិច្ច, សង្គម, វិទ្យាសាស្ត្រ, កសិកម្ម, សកលលោក, សាសនា)",
    schedInfoTitle: "ដំណើរការ ២៤ ម៉ោងលើ Cloud Hosting:",
    schedInfoDesc: "នៅពេលលោកអ្នក host កម្មវិធីនេះនៅលើ VPS, Cloud Server (Render, Railway, cPanel), កម្មវិធីនឹងដំណើរការ background scheduler ជាប្រចាំ ទោះបីជាលោកអ្នកបិទ browser ក៏ដោយ។",
    btnSaveSched: "រក្សាទុកកាលវិភាគ",
    
    msgSaved: "បានរក្សាទុកការកំណត់ជោគជ័យ!",
    msgCopied: "បានចម្លងស្គ្រីបទៅកាន់ Clipboard រួចរាល់!",
    msgResent: "បានផ្ញើស្គ្រីបចូល Telegram រួចរាល់!",
    msgDeleted: "បានលុបស្គ្រីបដោយជោគជ័យ!",
    msgConfirmDelete: "តើអ្នកពិតជាចង់លុបស្គ្រីបនេះមែនទេ?",
    msgNbEnCcCopied: "បានចម្លង Prompt (សំឡេងខ្មែរ + CC អង់គ្លេស) រួចរាល់!",
    badgeOn: "Auto-Run: បើក",
    badgeOff: "Auto-Run: បិទ"
  },
  
  en: {
    appTitle: "AI Script Automation Pro",
    appSubtitle: "AI Video Script Generator & Auto Telegram Broadcast",
    langButton: "ភាសាខ្មែរ",
    langFlag: "🇰🇭",
    tabGenerator: "Generator",
    tabHistory: "Script History",
    tabScheduler: "Auto-Scheduler",
    tabSettings: "Settings",
    
    settingsTitle: "API Settings",
    settingsDesc: "Configure your Gemini AI and Telegram Bot credentials to run the automation system.",
    btnSaveSettings: "Save",
    btnSaveBottom: "Save All Settings",
    settingsSecurityTitle: "Data Privacy & Security:",
    settingsSecurityDesc: "All API Keys and Tokens are stored locally on your own private server and are never shared.",
    lblGeminiKey: "Gemini API Key:",
    lblBotToken: "Telegram Bot Token:",
    lblChatId: "Telegram Chat ID:",
    
    formatTitle: "Video Format & Tone",
    lblFormat: "Format:",
    lblTone: "Tone:",
    
    notebooklmCardTitle: "Enforce NotebookLM to Speak 100% Khmer",
    notebooklmDesc: "✨ <strong>Fix NotebookLM Speaking English:</strong> Every script now auto-includes a <strong>Strict Khmer Directive</strong> header. When you paste this script into NotebookLM Studio to create an Audio/Video Overview, click <strong>Customize</strong> and paste this exact prompt:",
    btnCopyNotebooklmPrompt: "Copy NotebookLM Customize Prompt",
    btnCopyNotebooklm: "Copy for NotebookLM",
    msgNotebooklmPromptCopied: "NotebookLM Customize Prompt copied to clipboard!",
    msgNotebooklmScriptCopied: "Script copied for NotebookLM (Khmer Voice Mode)!",
    
    categoriesTitle: "7 Core Daily Rotating Categories",
    catEducation: "Education",
    catEconomy: "Economy & Finance",
    catSociety: "Society & Mindset",
    catScience: "Science & Tech",
    catAgriculture: "Modern Agriculture",
    catUniverse: "Universe Discoveries",
    catReligion: "Religion & Philosophy",
    
    topicsTitle: "Daily Script Topics (5 Scripts)",
    btnRefreshTopics: "Roll 5 New Topics",
    btnClearTopics: "Clear",
    topicsSubtext: "💡 <strong>Note:</strong> These 5 topics rotate daily automatically. You can edit or type custom topics anytime.",
    topicPlaceholder: "Topic (Auto-generated)",
    
    btnRun: "Start Generating & Broadcast to Telegram",
    btnRunning: "🚀 Running Batch...",
    
    logsTitle: "Live Execution Logs",
    btnClearLogs: "Clear",
    sysReady: "[System] Ready for automation...",
    
    historyTitle: "All Generated Scripts in Database",
    historySearchPlaceholder: "Search topics or content...",
    thDate: "Date",
    thTopic: "Topic",
    thAction: "Actions",
    btnCopy: "Copy Script",
    btnResend: "Send to Telegram",
    btnDelete: "Delete",
    
    schedCardTitle: "Daily Auto-Scheduler Configuration",
    schedEnableTitle: "Daily Auto-Run Automation",
    schedEnableDesc: "The app will generate and post all 5 scripts to Telegram every day at the scheduled time.",
    lblSchedTime: "Daily Trigger Time (HH:MM):",
    lblSchedAutoNiche: "Rotate 5 unique topics across the 7 fields every day (Education, Economy, Society, Science, Agriculture, Universe, Religion)",
    schedInfoTitle: "24/7 Background Engine on Cloud:",
    schedInfoDesc: "When hosting this app on a VPS or cloud server (Render, Railway, cPanel), the background scheduler runs automatically 24/7 even when your browser is closed.",
    btnSaveSched: "Save Schedule",
    
    msgSaved: "Settings saved successfully!",
    msgCopied: "Script copied to clipboard!",
    msgResent: "Script resent to Telegram!",
    msgDeleted: "Script deleted successfully!",
    msgConfirmDelete: "Are you sure you want to delete this script?",
    msgNbEnCcCopied: "Copied Prompt (Khmer Audio + English CC)!",
    badgeOn: "Auto-Run: Active",
    badgeOff: "Auto-Run: Off"
  }
};

// State
let currentLang = localStorage.getItem("app_language") || "km";
let historyCache = [];
let selectedScriptId = null;

// ==========================================
// Initialization
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  ensureFormatOptions();
  setupLanguageSwitcher();
  setupTabs();
  setupEyeToggles();
  setupEventListeners();
  loadInitialConfig();
  loadSchedulerStatus();
});

function ensureFormatOptions() {
  const select = document.getElementById("video-format");
  if (!select) return;
  const currentVal = select.value;
  const hasExplainer = Array.from(select.options).some(o => o.value.includes("Explainer Video"));
  if (!hasExplainer) {
    const desiredOptions = [
      { value: "NotebookLM Video Overview (Explainer Video ៥+ នាទី | សំឡេងខ្មែរ + ស្លាយ/CC អង់គ្លេស)", text: "NotebookLM Video Overview (Explainer Video ៥+ នាទី | សំឡេងខ្មែរ + ស្លាយ/CC អង់គ្លេស)" },
      { value: "NotebookLM Podcast (កិច្ចសន្ទនា ២ នាក់ - ខ្មែរ ១០០%)", text: "NotebookLM Podcast (កិច្ចសន្ទនា ២ នាក់ - ខ្មែរ ១០០%)" },
      { value: "TikTok / Reels / Shorts (ខ្លីក្រោម ៦០ វិនាទី)", text: "TikTok / Reels / Shorts (ខ្លីក្រោម ៦០ វិនាទី)" },
      { value: "YouTube Video (២-៣ នាទី - កម្រិតមធ្យម)", text: "YouTube Video (២-៣ នាទី - កម្រិតមធ្យម)" }
    ];
    select.innerHTML = "";
    desiredOptions.forEach(opt => {
      const el = document.createElement("option");
      el.value = opt.value;
      el.textContent = opt.text;
      select.appendChild(el);
    });
    if (currentVal && Array.from(select.options).some(o => o.value === currentVal)) {
      select.value = currentVal;
    }
  }
}

// ==========================================
// 1-Click Language Switcher
// ==========================================
function setupLanguageSwitcher() {
  const langBtn = document.getElementById("lang-btn");
  applyLanguage(currentLang);
  
  langBtn.addEventListener("click", () => {
    currentLang = currentLang === "km" ? "en" : "km";
    localStorage.setItem("app_language", currentLang);
    applyLanguage(currentLang);
    
    // Update topics to match selected language if default/auto
    refreshDailyTopics();
    
    // Also inform backend of language preference
    fetch("/api/config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ language: currentLang })
    });
  });
}

function applyLanguage(lang) {
  const t = translations[lang] || translations.km;
  
  // Set html lang
  document.documentElement.lang = lang;
  
  // Header
  document.getElementById("app-title").textContent = t.appTitle;
  document.getElementById("app-subtitle").textContent = t.appSubtitle;
  document.getElementById("lang-label").textContent = t.langButton;
  document.getElementById("lang-flag").textContent = t.langFlag;
  
  // Tabs
  const setTxt = (id, val) => {
    const el = document.getElementById(id);
    if (el) el.textContent = val;
  };

  setTxt("tab-title-generator", t.tabGenerator);
  setTxt("tab-title-history", t.tabHistory);
  setTxt("tab-title-scheduler", t.tabScheduler);
  setTxt("tab-title-settings", t.tabSettings);
  
  // Settings
  setTxt("settings-title", t.settingsTitle);
  setTxt("settings-desc", t.settingsDesc);
  setTxt("btn-save-text", t.btnSaveSettings);
  setTxt("btn-save-text-bottom", t.btnSaveBottom);
  setTxt("settings-security-title", t.settingsSecurityTitle);
  setTxt("settings-security-desc", t.settingsSecurityDesc);
  setTxt("lbl-gemini-key", t.lblGeminiKey);
  setTxt("lbl-bot-token", t.lblBotToken);
  setTxt("lbl-chat-id", t.lblChatId);
  
  // Generator Tab
  document.getElementById("format-title").textContent = t.formatTitle;
  document.getElementById("lbl-video-format").textContent = t.lblFormat;
  document.getElementById("lbl-video-tone").textContent = t.lblTone;
  
  document.getElementById("categories-title").textContent = t.categoriesTitle;
  document.querySelectorAll(".cat-text").forEach(el => {
    const cat = el.dataset.cat;
    if (cat === "education") el.textContent = t.catEducation;
    if (cat === "economy") el.textContent = t.catEconomy;
    if (cat === "society") el.textContent = t.catSociety;
    if (cat === "science") el.textContent = t.catScience;
    if (cat === "agriculture") el.textContent = t.catAgriculture;
    if (cat === "universe") el.textContent = t.catUniverse;
    if (cat === "religion") el.textContent = t.catReligion;
  });
  
  document.getElementById("topics-title").textContent = t.topicsTitle;
  document.getElementById("btn-refresh-topics-text").textContent = t.btnRefreshTopics;
  document.getElementById("btn-clear-topics-text").textContent = t.btnClearTopics;
  document.getElementById("topics-subtext").innerHTML = t.topicsSubtext;
  for (let i = 1; i <= 5; i++) {
    const el = document.getElementById(`topic-${i}`);
    if (el) el.placeholder = `${t.topicPlaceholder} #${i}`;
  }
  document.getElementById("btn-run-text").textContent = t.btnRun;
  
  // Logs
  document.getElementById("logs-title").textContent = t.logsTitle;
  document.getElementById("clear-log-text").textContent = t.btnClearLogs;
  
  // History Tab
  document.getElementById("history-title").textContent = t.historyTitle;
  document.getElementById("history-search").placeholder = t.historySearchPlaceholder;
  document.getElementById("th-date").textContent = t.thDate;
  document.getElementById("th-topic").textContent = t.thTopic;
  document.getElementById("th-action").textContent = t.thAction;
  document.getElementById("btn-copy-text").textContent = t.btnCopy;
  document.getElementById("btn-resend-text").textContent = t.btnResend;
  document.getElementById("btn-delete-text").textContent = t.btnDelete;
  
  // NotebookLM Elements
  setTxt("notebooklm-card-title", t.notebooklmCardTitle);
  const nbDesc = document.getElementById("notebooklm-desc-text");
  if (nbDesc) nbDesc.innerHTML = t.notebooklmDesc;
  setTxt("btn-copy-notebooklm-prompt-text", t.btnCopyNotebooklmPrompt);
  setTxt("btn-copy-notebooklm-text", t.btnCopyNotebooklm);
  
  // Scheduler Tab
  document.getElementById("scheduler-card-title").textContent = t.schedCardTitle;
  document.getElementById("sched-enable-title").textContent = t.schedEnableTitle;
  document.getElementById("sched-enable-desc").textContent = t.schedEnableDesc;
  document.getElementById("lbl-sched-time").textContent = t.lblSchedTime;
  document.getElementById("lbl-sched-auto-niche").textContent = t.lblSchedAutoNiche;
  document.getElementById("sched-info-title").textContent = t.schedInfoTitle;
  document.getElementById("sched-info-desc").textContent = t.schedInfoDesc;
  document.getElementById("btn-save-sched-text").textContent = t.btnSaveSched;
}

// ==========================================
// Tabs Navigation
// ==========================================
function setupTabs() {
  const tabs = document.querySelectorAll(".tab-btn");
  const panes = document.querySelectorAll(".tab-pane");
  
  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      tabs.forEach(t => t.classList.remove("active"));
      panes.forEach(p => p.classList.remove("active"));
      
      tab.classList.add("active");
      const target = tab.dataset.tab;
      document.getElementById(target).classList.add("active");
      
      if (target === "tab-history") {
        loadHistory();
      }
    });
  });
}

// ==========================================
// Eye Toggles for API Keys
// ==========================================
function setupEyeToggles() {
  document.querySelectorAll(".eye-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const input = document.getElementById(btn.dataset.target);
      if (input.type === "password") {
        input.type = "text";
        btn.textContent = "🔒";
      } else {
        input.type = "password";
        btn.textContent = "👁";
      }
    });
  });
}

// ==========================================
// Event Listeners
// ==========================================
function setupEventListeners() {
  const saveBtn = document.getElementById("btn-save-settings");
  if (saveBtn) saveBtn.addEventListener("click", saveSettings);
  
  const saveBtnBottom = document.getElementById("btn-save-settings-bottom");
  if (saveBtnBottom) saveBtnBottom.addEventListener("click", saveSettings);
  
  document.getElementById("btn-refresh-topics").addEventListener("click", refreshDailyTopics);
  document.getElementById("btn-clear-topics").addEventListener("click", clearTopics);
  document.getElementById("btn-run-batch").addEventListener("click", runBatchGeneration);
  document.getElementById("btn-clear-logs").addEventListener("click", clearLogs);
  
  // History tab
  document.getElementById("btn-refresh-history").addEventListener("click", loadHistory);
  document.getElementById("history-search").addEventListener("input", filterHistory);
  document.getElementById("btn-copy-script").addEventListener("click", copySelectedScript);
  
  const btnCopyNbScript = document.getElementById("btn-copy-notebooklm");
  if (btnCopyNbScript) btnCopyNbScript.addEventListener("click", copyScriptForNotebookLM);
  
  document.getElementById("btn-resend-script").addEventListener("click", resendSelectedScript);
  document.getElementById("btn-delete-script").addEventListener("click", deleteSelectedScript);
  
  // NotebookLM Banner Prompt Copy
  const btnCopyNbPrompt = document.getElementById("btn-copy-notebooklm-prompt");
  if (btnCopyNbPrompt) btnCopyNbPrompt.addEventListener("click", copyNotebookLMPrompt);
  
  const btnCopyNbEnCc = document.getElementById("btn-copy-nb-en-cc");
  if (btnCopyNbEnCc) btnCopyNbEnCc.addEventListener("click", copyNotebookLMEnCCPrompt);
  
  // Scheduler
  document.getElementById("btn-save-scheduler").addEventListener("click", saveSchedulerSettings);
  document.getElementById("sched-enabled-checkbox").addEventListener("change", updateSchedulerBadge);
}

// ==========================================
// Load Initial Config & Daily Topics
// ==========================================
const DEFAULT_GEMINI_KEY = "";
const DEFAULT_BOT_TOKEN = "";
const DEFAULT_CHAT_ID = "";

async function loadInitialConfig() {
  try {
    const res = await fetch("/api/config");
    const data = await res.json();
    if (data.success && data.config) {
      const c = data.config;
      document.getElementById("gemini-key").value = c.gemini_key || DEFAULT_GEMINI_KEY;
      document.getElementById("bot-token").value = c.bot_token || DEFAULT_BOT_TOKEN;
      document.getElementById("chat-id").value = c.chat_id || DEFAULT_CHAT_ID;
      
      if (c.format) document.getElementById("video-format").value = c.format;
      if (c.tone) document.getElementById("video-tone").value = c.tone;
      
      // If user had custom saved topics, load them. Otherwise load daily fresh rotating topics
      if (c.topics && Array.isArray(c.topics) && c.topics.length > 0) {
        c.topics.forEach((t, i) => {
          const el = document.getElementById(`topic-${i+1}`);
          if (el) el.value = t;
        });
      } else {
        refreshDailyTopics();
      }
    } else {
      // Fallback defaults
      document.getElementById("gemini-key").value = DEFAULT_GEMINI_KEY;
      document.getElementById("bot-token").value = DEFAULT_BOT_TOKEN;
      document.getElementById("chat-id").value = DEFAULT_CHAT_ID;
      refreshDailyTopics();
    }
  } catch (err) {
    console.error("Error loading config:", err);
    document.getElementById("gemini-key").value = DEFAULT_GEMINI_KEY;
    document.getElementById("bot-token").value = DEFAULT_BOT_TOKEN;
    document.getElementById("chat-id").value = DEFAULT_CHAT_ID;
  }
}

// ==========================================
// Refresh 5 Daily Rotating Topics
// ==========================================
async function refreshDailyTopics() {
  const btn = document.getElementById("btn-refresh-topics");
  btn.disabled = true;
  
  try {
    const res = await fetch(`/api/daily-topics?lang=${currentLang}`);
    const data = await res.json();
    if (data.success && data.topics) {
      data.topics.forEach((t, i) => {
        const el = document.getElementById(`topic-${i+1}`);
        if (el) el.value = t;
      });
      appendLog(`[Topics] 🎲 ${currentLang === 'km' ? 'បានបង្វិល ៥ ប្រធានបទថ្មីៗពី ៧ វិស័យ' : 'Rotated 5 fresh daily topics from the 7 categories'}: (${data.source || 'Auto'})`, "info");
      showToast(currentLang === 'km' ? "បានបង្វិល ៥ ប្រធានបទថ្មីៗ!" : "Loaded 5 fresh topics!", "success");
    }
  } catch (err) {
    console.error("Error fetching daily topics:", err);
  } finally {
    btn.disabled = false;
  }
}

function clearTopics() {
  for (let i = 1; i <= 5; i++) {
    const el = document.getElementById(`topic-${i}`);
    if (el) el.value = "";
  }
  showToast(currentLang === 'km' ? "បានសម្អាតប្រអប់ប្រធានបទ!" : "Topics cleared! Type your custom topics.", "info");
}

// ==========================================
// Save Settings
// ==========================================
async function saveSettings() {
  const payload = {
    gemini_key: document.getElementById("gemini-key").value.trim(),
    bot_token: document.getElementById("bot-token").value.trim(),
    chat_id: document.getElementById("chat-id").value.trim(),
    format: document.getElementById("video-format").value,
    tone: document.getElementById("video-tone").value,
    topics: getTopicValues()
  };
  
  try {
    const res = await fetch("/api/config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (data.success) {
      showToast(translations[currentLang].msgSaved, "success");
    }
  } catch (err) {
    showToast("Error saving settings", "error");
  }
}

function getTopicValues() {
  const topics = [];
  for (let i = 1; i <= 5; i++) {
    const val = document.getElementById(`topic-${i}`).value.trim();
    if (val) topics.push(val);
  }
  return topics;
}

// ==========================================
// Batch Generation & Telegram Broadcast
// ==========================================
async function runBatchGeneration() {
  const geminiKey = document.getElementById("gemini-key").value.trim() || DEFAULT_GEMINI_KEY;
  const botToken = document.getElementById("bot-token").value.trim() || DEFAULT_BOT_TOKEN;
  const chatId = document.getElementById("chat-id").value.trim() || DEFAULT_CHAT_ID;
  const format = document.getElementById("video-format").value;
  const tone = document.getElementById("video-tone").value;
  let topics = getTopicValues();
  const btnRun = document.getElementById("btn-run-batch");
  const t = translations[currentLang];
  
  // Make sure fields reflect active credentials
  document.getElementById("gemini-key").value = geminiKey;
  document.getElementById("bot-token").value = botToken;
  document.getElementById("chat-id").value = chatId;
  
  btnRun.disabled = true;
  document.getElementById("btn-run-text").textContent = t.btnRunning;
  
  const progContainer = document.getElementById("progress-container");
  const progFill = document.getElementById("progress-fill");
  const progStatus = document.getElementById("progress-status-text");
  const progPercent = document.getElementById("progress-percent-text");
  
  progContainer.classList.remove("hidden");
  progFill.style.width = "10%";
  progStatus.textContent = currentLang === "km" ? "កំពុងចាប់ផ្តើម..." : "Starting automation...";
  progPercent.textContent = "10%";
  
  appendLog(`[${new Date().toLocaleTimeString()}] ${currentLang === 'km' ? 'ចាប់ផ្តើមដំណើរការបង្កើតស្គ្រីប...' : 'Starting script automation...'}`, "system");
  appendLog(`[Format] ${format} | [Tone] ${tone}`, "info");
  
  try {
    const res = await fetch("/api/generate-batch", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        gemini_key: geminiKey,
        bot_token: botToken,
        chat_id: chatId,
        format: format,
        tone: tone,
        topics: topics,
        lang: currentLang
      })
    });
    
    const data = await res.json();
    if (data.success && data.results) {
      const results = data.results;
      const total = results.length;
      let successCount = 0;
      
      // If auto topics were generated, update the inputs so user sees them
      if (data.topics_used && Array.isArray(data.topics_used)) {
        data.topics_used.forEach((tp, i) => {
          const el = document.getElementById(`topic-${i+1}`);
          if (el) el.value = tp;
        });
      }
      
      results.forEach((r, idx) => {
        if (r.success) {
          successCount++;
          appendLog(`[Script ${r.index}] 📝 ${r.topic}`, "info");
          if (r.model) appendLog(`   (Model: ${r.model})`, "model");
          if (r.telegram_sent) {
            appendLog(`   ✅ ${currentLang === 'km' ? 'បានរក្សាទុក និងផ្ញើចូល Telegram ជោគជ័យ' : 'Saved & sent to Telegram successfully'}`, "success");
          } else {
            appendLog(`   ⚠️ ${currentLang === 'km' ? 'រក្សាទុកជោគជ័យ ប៉ុន្តែផ្ញើ Telegram បរាជ័យ' : 'Saved, but Telegram delivery failed'}: ${r.telegram_status}`, "error");
          }
        } else {
          appendLog(`[Script ${r.index}] ❌ ${r.topic} - ${r.error}`, "error");
        }
      });
      
      progFill.style.width = "100%";
      progPercent.textContent = "100%";
      progStatus.textContent = currentLang === "km" ? `បញ្ចប់ជោគជ័យ (${successCount}/${total})` : `Finished (${successCount}/${total})`;
      
      appendLog(`[${new Date().toLocaleTimeString()}] 🎉 ${currentLang === 'km' ? 'បញ្ចប់ការងារទាំងស្រុង! សូមពិនិត្យ Telegram។' : 'Batch finished! Check Telegram.'}`, "success");
      showToast(currentLang === 'km' ? `បានបញ្ចប់! ផ្ញើបាន ${successCount}/${total} ស្គ្រីប` : `Finished! Sent ${successCount}/${total} scripts`, "success");
    }
  } catch (err) {
    appendLog(`[Error] ${err.message}`, "error");
    showToast("Automation failed: " + err.message, "error");
  } finally {
    btnRun.disabled = false;
    document.getElementById("btn-run-text").textContent = t.btnRun;
  }
}

// ==========================================
// History Tab Operations
// ==========================================
async function loadHistory() {
  const tbody = document.getElementById("history-tbody");
  tbody.innerHTML = `<tr><td colspan="4" class="text-center">${currentLang === 'km' ? 'កំពុងទាញទិន្នន័យ...' : 'Loading history...'}</td></tr>`;
  
  try {
    const res = await fetch("/api/history");
    const data = await res.json();
    if (data.success && data.scripts) {
      historyCache = data.scripts;
      renderHistoryTable(historyCache);
    }
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="4" class="text-center" style="color: #ef4444;">Error loading history</td></tr>`;
  }
}

function renderHistoryTable(scripts) {
  const tbody = document.getElementById("history-tbody");
  if (scripts.length === 0) {
    tbody.innerHTML = `<tr><td colspan="4" class="text-center">${currentLang === 'km' ? 'មិនទាន់មានស្គ្រីបក្នុង Database ទេ' : 'No scripts in database yet'}</td></tr>`;
    return;
  }
  
  tbody.innerHTML = "";
  scripts.forEach(s => {
    const tr = document.createElement("tr");
    tr.dataset.id = s.id;
    if (selectedScriptId === s.id) tr.classList.add("selected");
    
    tr.innerHTML = `
      <td style="font-weight: 700; color: #94a3b8; text-align: center;">#${s.id}</td>
      <td style="color: #64748b; font-size: 0.85rem;">${s.date}</td>
      <td style="font-weight: 500;">${escapeHtml(s.topic)}</td>
      <td style="text-align: center;">
        <button class="btn btn-secondary btn-sm" onclick="viewScriptDetail(${s.id}, event)">👁</button>
      </td>
    `;
    tr.addEventListener("click", () => viewScriptDetail(s.id));
    tbody.appendChild(tr);
  });
}

function filterHistory() {
  const query = document.getElementById("history-search").value.toLowerCase().trim();
  if (!query) {
    renderHistoryTable(historyCache);
    return;
  }
  const filtered = historyCache.filter(s => 
    s.topic.toLowerCase().includes(query) || (s.content && s.content.toLowerCase().includes(query))
  );
  renderHistoryTable(filtered);
}

function viewScriptDetail(scriptId, event) {
  if (event) event.stopPropagation();
  selectedScriptId = scriptId;
  
  document.querySelectorAll("#history-tbody tr").forEach(tr => {
    tr.classList.toggle("selected", tr.dataset.id == scriptId);
  });
  
  const script = historyCache.find(s => s.id == scriptId);
  if (script) {
    const detailBox = document.getElementById("history-detail-card");
    detailBox.classList.remove("hidden");
    document.getElementById("preview-topic-title").textContent = `📝 #${script.id}: ${script.topic}`;
    document.getElementById("preview-content").textContent = script.content;
    detailBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
}

function copySelectedScript() {
  const content = document.getElementById("preview-content").textContent;
  if (!content) return;
  navigator.clipboard.writeText(content).then(() => {
    showToast(translations[currentLang].msgCopied, "success");
  });
}

function copyNotebookLMEnCCPrompt() {
  const codeEl = document.getElementById("notebooklm-prompt-en-cc");
  if (!codeEl) return;
  const promptText = codeEl.textContent.trim();
  navigator.clipboard.writeText(promptText).then(() => {
    showToast(translations[currentLang].msgNbEnCcCopied || "បានចម្លង Prompt (សំឡេងខ្មែរ + CC អង់គ្លេស)!", "success");
  });
}

function copyNotebookLMPrompt() {
  const codeEl = document.getElementById("notebooklm-prompt-content");
  if (!codeEl) return;
  const promptText = codeEl.textContent.trim();
  navigator.clipboard.writeText(promptText).then(() => {
    showToast(translations[currentLang].msgNotebooklmPromptCopied, "success");
  });
}

function copyScriptForNotebookLM() {
  const content = document.getElementById("preview-content").textContent;
  if (!content) return;
  
  let formatted = content;
  // If not already containing the NotebookLM directive, add it
  if (!formatted.toUpperCase().includes("NOTEBOOKLM")) {
    const directive = 
`======================================================================
🚨 NOTEBOOKLM / AI VIDEO SYSTEM DIRECTIVE: STRICT KHMER AUDIO & VIDEO 🚨
• ភាសានិយាយ (Spoken Language): ភាសាខ្មែរ (Khmer) ១០០% ទាំងស្រុង។
• ពិធីករ និងវាគ្មិនទាំងអស់ (All Hosts & Speakers) ត្រូវតែជជែក សន្ទនា និងអានជាភាសាខ្មែរសុទ្ធសាធ។
• ហាមដាច់ខាតកុំនិយាយ ឬបកប្រែជាភាសាអង់គ្លេស (Strictly NO English voiceover or speech).
• Every spoken dialogue and audio overview in NotebookLM must be in natural Khmer.
======================================================================\n\n`;
    formatted = directive + formatted;
  }
  
  navigator.clipboard.writeText(formatted).then(() => {
    showToast(translations[currentLang].msgNotebooklmScriptCopied, "success");
  });
}

async function resendSelectedScript() {
  if (!selectedScriptId) return;
  try {
    const res = await fetch(`/api/history/${selectedScriptId}/resend`, { method: "POST" });
    const data = await res.json();
    if (data.success) {
      showToast(translations[currentLang].msgResent, "success");
    } else {
      showToast(data.message || "Failed to resend", "error");
    }
  } catch (err) {
    showToast("Error: " + err.message, "error");
  }
}

async function deleteSelectedScript() {
  if (!selectedScriptId) return;
  if (!confirm(translations[currentLang].msgConfirmDelete)) return;
  
  try {
    const res = await fetch(`/api/history/${selectedScriptId}`, { method: "DELETE" });
    const data = await res.json();
    if (data.success) {
      showToast(translations[currentLang].msgDeleted, "success");
      document.getElementById("history-detail-card").classList.add("hidden");
      selectedScriptId = null;
      loadHistory();
    }
  } catch (err) {
    showToast("Delete failed", "error");
  }
}

// ==========================================
// Scheduler Operations
// ==========================================
async function loadSchedulerStatus() {
  try {
    const res = await fetch("/api/scheduler");
    const data = await res.json();
    if (data.success && data.scheduler) {
      const s = data.scheduler;
      document.getElementById("sched-enabled-checkbox").checked = !!s.enabled;
      if (s.time) document.getElementById("sched-time-input").value = s.time;
      if (s.auto_diverse_topics !== undefined) {
        document.getElementById("sched-auto-niche-checkbox").checked = !!s.auto_diverse_topics;
      }
      updateSchedulerBadge();
    }
  } catch (err) {
    console.error("Error loading scheduler:", err);
  }
}

function updateSchedulerBadge() {
  const enabled = document.getElementById("sched-enabled-checkbox").checked;
  const badge = document.getElementById("scheduler-badge");
  const badgeText = document.getElementById("badge-text");
  const t = translations[currentLang];
  
  if (enabled) {
    badge.classList.add("active");
    badgeText.textContent = t.badgeOn;
  } else {
    badge.classList.remove("active");
    badgeText.textContent = t.badgeOff;
  }
}

async function saveSchedulerSettings() {
  const enabled = document.getElementById("sched-enabled-checkbox").checked;
  const time = document.getElementById("sched-time-input").value;
  const autoDiverse = document.getElementById("sched-auto-niche-checkbox").checked;
  
  try {
    const res = await fetch("/api/scheduler", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        enabled: enabled,
        time: time,
        auto_diverse_topics: autoDiverse
      })
    });
    const data = await res.json();
    if (data.success) {
      updateSchedulerBadge();
      showToast(translations[currentLang].msgSaved, "success");
    }
  } catch (err) {
    showToast("Error saving schedule", "error");
  }
}

// ==========================================
// Helpers
// ==========================================
function appendLog(text, type = "info") {
  const terminal = document.getElementById("log-terminal");
  const entry = document.createElement("div");
  entry.className = `log-entry ${type}`;
  entry.textContent = text;
  terminal.appendChild(entry);
  terminal.scrollTop = terminal.scrollHeight;
}

function clearLogs() {
  const terminal = document.getElementById("log-terminal");
  terminal.innerHTML = "";
  appendLog(translations[currentLang].sysReady, "system");
}

function showToast(message, type = "info") {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.className = `toast show ${type}`;
  setTimeout(() => {
    toast.className = "toast";
  }, 3500);
}

function escapeHtml(str) {
  if (!str) return "";
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
