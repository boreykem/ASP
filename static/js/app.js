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
    btnJumpSettings: "ការកំណត់ API",
    
    settingsTitle: "ការកំណត់ API (Settings)",
    settingsDesc: "កំណត់ API Key សម្រាប់ Gemini AI និង Telegram Bot របស់អ្នកដើម្បីដំណើរការប្រព័ន្ធ។",
    btnSaveSettings: "រក្សាទុក",
    btnSaveBottom: "រក្សាទុកការកំណត់ទាំងអស់",
    settingsSecurityTitle: "សុវត្ថិភាពទិន្នន័យ៖",
    settingsSecurityDesc: "ទិន្នន័យ API Key និង Token ទាំងអស់ត្រូវបានរក្សាទុកតែលើ Server ផ្ទាល់ខ្លួនរបស់អ្នកប៉ុណ្ណោះ គ្មាននរណាម្នាក់អាចមើលឃើញឡើយ។",
    lblGeminiKey: "Gemini API Key:",
    lblBotToken: "Telegram Bot Token:",
    lblChatId: "Telegram Chat ID:",
    
    fbSettingsTitle: "Facebook Page API (Meta Graph API)",
    fbSettingsDesc: "បង្ហោះស្គ្រីប និងអត្ថបទទៅកាន់ Facebook Page របស់អ្នកដោយស្វ័យប្រវត្តិ។",
    fbAutoTitle: "Auto-Post ឡើង Facebook Page",
    fbAutoDesc: "ពេលបង្កើតស្គ្រីបរួច នឹង Post ឡើង Page ភ្លាមៗដោយស្វ័យប្រវត្ត។",
    lblFbPageId: "Facebook Page ID (Selected Page):",
    lblFbUserToken: "🔑 Facebook User Access Token (Master Token - 2 Months):",
    descFbUserToken: "💡 Master Token មានសុពលភាព ២ ខែ (60 ថ្ងៃ) សម្រាប់គ្រប់គ្រង និងបង្ហោះទៅកាន់ Facebook Pages ទាំង ២៣ ដោយស្វ័យប្រវត្តិ។",
    btnVerifyFb: "ផ្ទៀងផ្ទាត់ Facebook Page",
    btnPostFacebook: "Post Facebook",
    btnFetchFbPages: "ទាញយក Pages របស់ខ្ញុំ",
    lblFbPageSelect: "ឬជ្រើសរើស Page ជាក់លាក់ណាមួយ (Select Single Page):",
    fbBroadcastAllTitle: "📢 បង្ហោះចូលគ្រប់ Pages ទាំងអស់ (Broadcast to All Pages)",
    fbBroadcastAllDesc: "ពេលបង្កើតស្គ្រីប វានឹងបង្ហោះចូលគ្រប់ Facebook Pages ទាំងអស់ដែលបានជ្រើសរើសក្នុងពេលតែមួយ។",
    lblPagesList: "បញ្ជី Facebook Pages របស់អ្នក:",
    btnSelectAll: "✓ ជ្រើសរើសទាំងអស់",
    btnDeselectAll: "✕ ដោះទាំងអស់",
    msgPagesLoaded: "បានទាញយក Pages ទាំងអស់ជោគជ័យ!",
    msgFbPosted: "បានបង្ហោះឡើង Facebook Page ជោគជ័យ!",
    msgFbVerified: "បានភ្ជាប់ទៅកាន់ Facebook Page ជោគជ័យ!",
    
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
    btnCreateVideo: "ផលិតវីដេអូ Reels AI",
    btnBroadcastVideoFb: "បង្ហោះវីដេអូទៅកាន់ Facebook Pages ទាំងអស់",
    btnDownloadVideo: "ទាញយក MP4",
    
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
    btnJumpSettings: "API Settings",
    
    settingsTitle: "API Settings",
    settingsDesc: "Configure your Gemini AI and Telegram Bot credentials to run the automation system.",
    btnSaveSettings: "Save",
    btnSaveBottom: "Save All Settings",
    settingsSecurityTitle: "Data Privacy & Security:",
    settingsSecurityDesc: "All API Keys and Tokens are stored locally on your own private server and are never shared.",
    lblGeminiKey: "Gemini API Key:",
    lblBotToken: "Telegram Bot Token:",
    lblChatId: "Telegram Chat ID:",
    
    fbSettingsTitle: "Facebook Page API (Meta Graph API)",
    fbSettingsDesc: "Automatically publish scripts and posts directly to your Facebook Page.",
    fbAutoTitle: "Auto-Post to Facebook Page",
    fbAutoDesc: "Automatically publish generated scripts to your Page upon generation.",
    lblFbPageId: "Facebook Page ID (Selected Page):",
    lblFbUserToken: "🔑 Facebook User Access Token (Master Token - 2 Months):",
    descFbUserToken: "💡 Master Token valid for 2 months (60 days) to auto-manage and broadcast to all 23 Facebook Pages.",
    btnVerifyFb: "Verify Facebook Page",
    btnPostFacebook: "Post to Facebook",
    btnCreateVideo: "Create AI Reels Video",
    btnBroadcastVideoFb: "Broadcast Video to All Facebook Pages",
    btnDownloadVideo: "Download MP4",
    btnFetchFbPages: "Fetch My Pages",
    lblFbPageSelect: "Or Select a Single Page:",
    fbBroadcastAllTitle: "📢 Broadcast to All Pages",
    fbBroadcastAllDesc: "When a script is generated, publish it to all selected Facebook Pages simultaneously.",
    lblPagesList: "Your Facebook Pages List:",
    btnSelectAll: "✓ Select All",
    btnDeselectAll: "✕ Deselect All",
    msgPagesLoaded: "Loaded all Facebook Pages successfully!",
    msgFbPosted: "Successfully posted to Facebook Page!",
    msgFbVerified: "Successfully connected to Facebook Page!",
    
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

// ==========================================
// Format Guidance & Prompts Data
// ==========================================
const FORMAT_DATA = {
  video_overview: {
    icon: "🎬",
    titleKm: "ការកំណត់ NotebookLM Video Overview (Explainer Video ៥+ នាទី)",
    titleEn: "NotebookLM Video Overview (5+ Min Explainer Video)",
    descKm: "🎬 <strong>គន្លឹះបង្កើត Video Overview (Explainer Video ៥+ នាទី) & គ្មានអក្សរការេៗ៖</strong> ដើម្បីបង្កើតវីដេអូបែប Explainer Video (មាន AI Presenter ធ្វើបទបង្ហាញ និងមានស្លាយ Slide លើអេក្រង់ ៥ នាទីឡើងទៅ) សូមចម្លង Prompt ខាងក្រោមទៅដាក់ក្នុង NotebookLM <strong>Customize</strong>៖",
    descEn: "🎬 <strong>5+ Min Explainer Video Overview (Zero Tofu Font Glitches):</strong> Copy this prompt into NotebookLM <strong>Customize</strong> to generate a 5+ minute multi-scene explainer video with spoken Khmer voiceover and on-screen slides/CC in clean English:",
    prompt: "Please generate an EXTENSIVE 5+ MINUTE EXPLAINER VIDEO OVERVIEW (not a podcast discussion). The AI presenter/narrator must deliver the voiceover 100% exclusively in fluent Khmer language (ភាសាខ្មែរ) with zero English voiceover. All on-screen slides, visual bullet points, and closed captions (CC) must be displayed in clean ENGLISH to ensure perfect font rendering. Thoroughly unpack each scene with comprehensive explanations.",
    btnKm: "ចម្លង Prompt (Video Overview ៥+ នាទី)",
    btnEn: "Copy Video Overview Prompt",
    shortKm: "Video Overview (៥+ នាទី)",
    shortEn: "Video Overview (5+ Min)"
  },
  podcast: {
    icon: "🎙️",
    titleKm: "ការកំណត់ NotebookLM Podcast (កិច្ចសន្ទនា ២ នាក់ - ខ្មែរ ១០០%)",
    titleEn: "NotebookLM Podcast (2-Host Discussion - 100% Khmer)",
    descKm: "🎙️ <strong>គន្លឹះបង្កើត Podcast កិច្ចសន្ទនា ២ នាក់ជាភាសាខ្មែរ ១០០%៖</strong> ដើម្បីឱ្យ AI Hosts ទាំង ២ នាក់ជជែកវែកញែកស៊ីជម្រៅជាភាសាខ្មែរសុទ្ធសាធ (គ្មានពាក្យអង់គ្លេសលាយ) សូមចម្លង Prompt ខាងក្រោមទៅដាក់ក្នុង NotebookLM <strong>Customize</strong>៖",
    descEn: "🎙️ <strong>100% Khmer Podcast Discussion Guide:</strong> To ensure both AI hosts converse, banter, and debate exclusively in fluent Khmer with zero English, copy this prompt into NotebookLM <strong>Customize</strong>:",
    prompt: "Please generate the entire deep-dive podcast discussion 100% exclusively in fluent Khmer language (ភាសាខ្មែរ). Both hosts (Host 1 & Host 2) must converse, banter, debate, and explain naturally and engagingly in natural Khmer. Absolutely DO NOT speak, summarize, or translate into English.",
    btnKm: "ចម្លង Prompt (Podcast ខ្មែរ ១០០%)",
    btnEn: "Copy Podcast Prompt",
    shortKm: "Podcast (ខ្មែរ ១០០%)",
    shortEn: "Podcast (100% Khmer)"
  },
  tiktok: {
    icon: "📱",
    titleKm: "ការណែនាំស្គ្រីប TikTok / Reels / Shorts (ខ្លីក្រោម ៦០ វិនាទី)",
    titleEn: "TikTok / Reels / Shorts Script Guide (< 60 Seconds)",
    descKm: "📱 <strong>ទម្រង់ស្គ្រីបវីដេអូខ្លីបញ្ឈរ (Viral Short-Form):</strong> ស្គ្រីបត្រូវបានរៀបចំឡើងជា ៣ វគ្គច្បាស់លាស់ ផ្តោតលើការទាក់ចិត្តអ្នកមើលក្នុង ៣ វិនាទីដំបូង (High Retention Hook) និងអំពាវនាវឱ្យចុច Follow/Share/Like នៅចុងបញ្ចប់។ អាចចម្លងទៅបញ្ចូលក្នុង CapCut, HeyGen, ឬ AI Voiceover បានភ្លាមៗ។",
    descEn: "📱 <strong>Viral Short-Form Script Guide:</strong> Specially structured for high retention on TikTok & Reels: 0-3s high-curiosity Hook, 3-45s fast-paced core value with visual cues, and 45-60s strong Call-to-Action.",
    prompt: "ទម្រង់ស្គ្រីប TikTok / Shorts:\n• [00:00 - 00:03] HOOK (ទាក់ទាញខ្លាំងមិនឱ្យអូសរំលង) [សំឡេង + អក្សររត់ + Visual Cue]\n• [00:03 - 00:45] CORE VALUE (ខ្លឹមសារ ៣ ចំណុចខ្លី ខ្លឹម កាត់តលឿន)\n• [00:45 - 00:60] CTA (ដាស់តឿនឱ្យចុច Like, Follow និង Share)",
    btnKm: "ចម្លងទម្រង់ TikTok Prompt",
    btnEn: "Copy TikTok Format Prompt",
    shortKm: "TikTok / Reels / Shorts",
    shortEn: "TikTok / Reels / Shorts"
  },
  youtube: {
    icon: "📹",
    titleKm: "ការណែនាំស្គ្រីប YouTube Video (២-៣ នាទី - កម្រិតមធ្យម)",
    titleEn: "YouTube Video Script Guide (2-3 Minutes - Standard)",
    descKm: "📹 <strong>ទម្រង់ស្គ្រីប YouTube Video ស្តង់ដារ៖</strong> រៀបចំឡើងសម្រាប់មាតិកា YouTube កម្រិតមធ្យម មានសេចក្តីផ្តើមទាក់ទាញ (Intro & Hook), ការបកស្រាយស៊ីជម្រៅ ៣ ចំណុចសំខាន់ៗ (Body), និងសេចក្តីសន្និដ្ឋានអំពាវនាវឱ្យចុច Subscribe & Comment (Outro & CTA)។",
    descEn: "📹 <strong>Standard YouTube Video Script Guide:</strong> Designed for standard 2-3 minute YouTube videos with an engaging Intro & Hook, 3 structured key points with visual/B-roll cues, and an engaging Outro with Subscribe CTA.",
    prompt: "ទម្រង់ស្គ្រីប YouTube Video:\n• [00:00 - 00:20] INTRO & HOOK (សេចក្តីផ្តើម & បញ្ហាស្នូល)\n• [00:20 - 02:00] BODY CONTENT (៣ ចំណុចស៊ីជម្រៅ + B-Roll / Visual Cues)\n• [02:00 - 02:30] OUTRO & CTA (សេចក្តីសន្និដ្ឋាន & ចុច Subscribe)",
    btnKm: "ចម្លងទម្រង់ YouTube Prompt",
    btnEn: "Copy YouTube Format Prompt",
    shortKm: "YouTube Video (២-៣ នាទី)",
    shortEn: "YouTube Video (2-3 Min)"
  }
};

function detectFormatKey(formatVal) {
  const str = (formatVal || "").toLowerCase();
  if (str.includes("video overview") || str.includes("explainer") || str.includes("៥+ នាទី") || str.includes("5+")) {
    return "video_overview";
  }
  if (str.includes("podcast") || str.includes("សន្ទនា") || str.includes("២ នាក់")) {
    return "podcast";
  }
  if (str.includes("tiktok") || str.includes("reels") || str.includes("shorts") || str.includes("៦០ វិនាទី") || str.includes("60")) {
    return "tiktok";
  }
  if (str.includes("youtube") || str.includes("២-៣ នាទី") || str.includes("2-3")) {
    return "youtube";
  }
  return "video_overview";
}

function getToneDirective(toneVal) {
  const t = (toneVal || "").toLowerCase();
  if (t.includes("អប់រំ") || t.includes("educational")) {
    return {
      nameKm: "អប់រំ & ចំណេះដឹង",
      nameEn: "Educational",
      promptEn: "Delivery Tone: Clear, informative, authoritative, and educational (អប់រំ & ចំណេះដឹង). Unpack every concept with articulate pacing and pedagogical depth.",
      promptKm: "ទឹកដមសម្លេង៖ អប់រំ & ចំណេះដឹង (Educational) - ពិរោះ ច្បាស់ៗ មានគរុកោសល្យ និងពន្យល់ស៊ីជម្រៅងាយយល់។"
    };
  }
  if (t.includes("និទាន") || t.includes("storytelling") || t.includes("emotional")) {
    return {
      nameKm: "និទានរឿង",
      nameEn: "Storytelling",
      promptEn: "Delivery Tone: Deeply immersive, emotional storytelling and cinematic narrative (និទានរឿង & អារម្មណ៍ស៊ីជម្រៅ). Deliver with evocative pacing and heartfelt expression.",
      promptKm: "ទឹកដមសម្លេង៖ និទានរឿង (Storytelling & Emotional) - រំជួលចិត្ត ទាក់ទាញអារម្មណ៍ និងរៀបរាប់ដំណើររឿងយ៉ាងជក់ចិត្ត។"
    };
  }
  // Default: Hook & Catchy
  return {
    nameKm: "ទាក់ទាញ & រំភើប",
    nameEn: "Hook & Catchy",
    promptEn: "Delivery Tone: High-energy, exciting, and captivating (ទាក់ទាញ & រំភើប). Keep the audience thoroughly hooked with engaging enthusiasm.",
    promptKm: "ទឹកដមសម្លេង៖ ទាក់ទាញ & រំភើប (Hook & Catchy) - រស់រវើក ស្វាហាប់ ជំរុញការចង់ដឹងចង់ឃើញ និងទាក់ទាញតាំងពីដើមដល់ចប់។"
  };
}

function updateFormatHelperCard(formatVal, toneVal, animate = false) {
  const formatSelect = document.getElementById("video-format");
  const toneSelect = document.getElementById("video-tone");
  const fVal = formatVal || (formatSelect ? formatSelect.value : "");
  const tVal = toneVal || (toneSelect ? toneSelect.value : "");
  
  const key = detectFormatKey(fVal);
  const data = FORMAT_DATA[key] || FORMAT_DATA.video_overview;
  const toneData = getToneDirective(tVal);
  
  const iconEl = document.getElementById("format-helper-icon");
  const titleEl = document.getElementById("notebooklm-card-title");
  const descEl = document.getElementById("notebooklm-desc-text");
  const codeEl = document.getElementById("notebooklm-prompt-content");
  const btnTextEl = document.getElementById("btn-copy-format-prompt-text");
  const cardEl = document.getElementById("format-helper-card");
  
  if (iconEl) iconEl.textContent = data.icon;
  if (titleEl) {
    const toneBadge = currentLang === "km" ? toneData.nameKm : toneData.nameEn;
    titleEl.textContent = `${currentLang === "km" ? data.titleKm : data.titleEn} (${toneBadge})`;
  }
  if (descEl) descEl.innerHTML = currentLang === "km" ? data.descKm : data.descEn;
  
  // Combine format prompt with the active tone directive so the user sees the script change!
  let combinedPrompt = "";
  if (key === "video_overview" || key === "podcast") {
    combinedPrompt = `${data.prompt}\n\n• ${currentLang === "km" ? toneData.promptKm : toneData.promptEn}`;
  } else {
    combinedPrompt = `${data.prompt}\n• [${currentLang === "km" ? toneData.promptKm : toneData.promptEn}]`;
  }
  
  if (codeEl) codeEl.textContent = combinedPrompt;
  if (btnTextEl) btnTextEl.textContent = currentLang === "km" ? data.btnKm : data.btnEn;
  
  if (animate && cardEl) {
    cardEl.classList.remove("format-highlight");
    void cardEl.offsetWidth; // trigger reflow
    cardEl.classList.add("format-highlight");
  }
}

function handleFormatChange(e) {
  const val = e.target.value;
  const tVal = document.getElementById("video-tone")?.value;
  updateFormatHelperCard(val, tVal, true);
  
  const key = detectFormatKey(val);
  const data = FORMAT_DATA[key] || FORMAT_DATA.video_overview;
  const name = currentLang === "km" ? data.shortKm : data.shortEn;
  showToast(currentLang === "km" ? `បានប្តូរទៅទម្រង់៖ ${name}` : `Switched to format: ${name}`, "info");
  
  // Auto-save format to backend
  fetch("/api/config", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ format: val })
  }).catch(err => console.error("Error auto-saving format:", err));
}

function handleToneChange(e) {
  const tVal = e.target.value;
  const fVal = document.getElementById("video-format")?.value;
  updateFormatHelperCard(fVal, tVal, true);
  
  const toneData = getToneDirective(tVal);
  const toneName = currentLang === "km" ? toneData.nameKm : toneData.nameEn;
  showToast(currentLang === "km" ? `បានប្តូរទឹកដម៖ ${toneName}` : `Switched tone to: ${toneName}`, "info");
  
  // Auto-save tone to backend
  fetch("/api/config", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tone: tVal })
  }).catch(err => console.error("Error auto-saving tone:", err));
}

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
  setTxt("nav-settings-btn-label", t.tabSettings);
  setTxt("btn-jump-settings-text", t.btnJumpSettings);
  
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
  
  // Facebook Page Settings
  setTxt("fb-settings-title", t.fbSettingsTitle);
  setTxt("fb-settings-desc", t.fbSettingsDesc);
  setTxt("fb-auto-title", t.fbAutoTitle);
  setTxt("fb-auto-desc", t.fbAutoDesc);
  setTxt("lbl-fb-page-id", t.lblFbPageId);
  setTxt("lbl-fb-user-token", t.lblFbUserToken);
  setTxt("desc-fb-user-token", t.descFbUserToken);
  setTxt("lbl-fb-page-select", t.lblFbPageSelect);
  setTxt("fb-broadcast-all-title", t.fbBroadcastAllTitle);
  setTxt("fb-broadcast-all-desc", t.fbBroadcastAllDesc);
  setTxt("lbl-pages-list", t.lblPagesList);
  setTxt("btn-select-all-pages", t.btnSelectAll);
  setTxt("btn-deselect-all-pages", t.btnDeselectAll);
  setTxt("btn-fetch-fb-pages-text", t.btnFetchFbPages);
  setTxt("btn-verify-fb-text", t.btnVerifyFb);
  setTxt("btn-post-facebook-text", t.btnPostFacebook);
  setTxt("btn-create-video-text", t.btnCreateVideo);
  setTxt("btn-broadcast-video-fb-text", t.btnBroadcastVideoFb);
  setTxt("btn-download-video-text", t.btnDownloadVideo);
  
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
  
  // Dynamic Format Helper Card
  updateFormatHelperCard(document.getElementById("video-format")?.value, document.getElementById("video-tone")?.value, false);
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
function switchTab(targetId) {
  const tabs = document.querySelectorAll(".tab-btn");
  const panes = document.querySelectorAll(".tab-pane");
  const navSettingsBtn = document.getElementById("nav-settings-btn");
  
  tabs.forEach(t => {
    if (t.dataset.tab === targetId) {
      t.classList.add("active");
    } else {
      t.classList.remove("active");
    }
  });
  
  panes.forEach(p => {
    if (p.id === targetId) {
      p.classList.add("active");
    } else {
      p.classList.remove("active");
    }
  });
  
  if (navSettingsBtn) {
    if (targetId === "tab-settings") {
      navSettingsBtn.classList.add("active");
    } else {
      navSettingsBtn.classList.remove("active");
    }
  }
  
  if (targetId === "tab-history") {
    loadHistory();
  }
}

function setupTabs() {
  const tabs = document.querySelectorAll(".tab-btn");
  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      switchTab(tab.dataset.tab);
    });
  });

  const navSettingsBtn = document.getElementById("nav-settings-btn");
  if (navSettingsBtn) {
    navSettingsBtn.addEventListener("click", () => {
      const activePane = document.querySelector(".tab-pane.active");
      if (activePane && activePane.id === "tab-settings") {
        switchTab("tab-generator");
      } else {
        switchTab("tab-settings");
      }
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
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
  
  const btnPostFb = document.getElementById("btn-post-facebook");
  if (btnPostFb) btnPostFb.addEventListener("click", postSelectedScriptToFacebook);
  
  const btnCreateVeo = document.getElementById("btn-create-veo-video");
  if (btnCreateVeo) btnCreateVeo.addEventListener("click", createVeoVideoForSelectedScript);

  const btnCreateVid = document.getElementById("btn-create-video");
  if (btnCreateVid) btnCreateVid.addEventListener("click", createReelsVideoForSelectedScript);
  
  const btnBroadcastVid = document.getElementById("btn-broadcast-video-fb");
  if (btnBroadcastVid) btnBroadcastVid.addEventListener("click", broadcastRenderedVideoToFacebook);

  const btnBroadcastUrl = document.getElementById("btn-broadcast-url-fb");
  if (btnBroadcastUrl) btnBroadcastUrl.addEventListener("click", broadcastCustomVideoUrl);
  
  const btnVerifyFb = document.getElementById("btn-verify-fb");
  if (btnVerifyFb) btnVerifyFb.addEventListener("click", verifyFacebookPage);
  
  const btnFetchFb = document.getElementById("btn-fetch-fb-pages");
  if (btnFetchFb) btnFetchFb.addEventListener("click", fetchFacebookPages);
  
  const fbSelect = document.getElementById("fb-page-select");
  if (fbSelect) fbSelect.addEventListener("change", handleFacebookPageSelect);
  
  const fbTokenInput = document.getElementById("fb-page-token");
  if (fbTokenInput) {
    fbTokenInput.addEventListener("input", (e) => {
      const curId = document.getElementById("fb-page-select")?.value;
      if (curId && fbPagesCache) {
        const p = fbPagesCache.find(item => String(item.id) === String(curId));
        if (p) p.access_token = e.target.value.trim();
      }
    });
  }
  
  document.getElementById("btn-select-all-pages")?.addEventListener("click", () => {
    document.querySelectorAll(".fb-page-cb").forEach(cb => cb.checked = true);
  });
  document.getElementById("btn-deselect-all-pages")?.addEventListener("click", () => {
    document.querySelectorAll(".fb-page-cb").forEach(cb => cb.checked = false);
  });
  
  document.getElementById("btn-delete-script").addEventListener("click", deleteSelectedScript);
  
  // Format dropdown change listener
  const formatSelect = document.getElementById("video-format");
  if (formatSelect) {
    formatSelect.addEventListener("change", handleFormatChange);
  }
  
  // Tone dropdown change listener
  const toneSelect = document.getElementById("video-tone");
  if (toneSelect) {
    toneSelect.addEventListener("change", handleToneChange);
  }
  
  // Format Guidance Prompt Copy
  const btnCopyFormat = document.getElementById("btn-copy-format-prompt");
  if (btnCopyFormat) btnCopyFormat.addEventListener("click", copyActiveFormatPrompt);

  const btnCopyNbPrompt = document.getElementById("btn-copy-notebooklm-prompt");
  if (btnCopyNbPrompt) btnCopyNbPrompt.addEventListener("click", copyActiveFormatPrompt);
  
  const btnCopyNbEnCc = document.getElementById("btn-copy-nb-en-cc");
  if (btnCopyNbEnCc) btnCopyNbEnCc.addEventListener("click", copyActiveFormatPrompt);
  
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
      
      const fbPageId = document.getElementById("fb-page-id");
      const fbUserToken = document.getElementById("fb-user-token");
      const fbPageToken = document.getElementById("fb-page-token");
      const fbAutoPost = document.getElementById("fb-auto-post-checkbox");
      const fbBroadcastAll = document.getElementById("fb-broadcast-all-checkbox");
      if (fbPageId) fbPageId.value = c.facebook_page_id || "";
      if (fbUserToken) fbUserToken.value = c.facebook_user_access_token || "";
      if (fbPageToken) fbPageToken.value = c.facebook_access_token || "";
      if (fbAutoPost) fbAutoPost.checked = !!c.facebook_auto_post;
      if (fbBroadcastAll) fbBroadcastAll.checked = !!c.facebook_all_pages;
      
      if (c.facebook_selected_pages && c.facebook_selected_pages.length > 0) {
        fbPagesCache = c.facebook_selected_pages;
        renderPagesChecklist(fbPagesCache);
        const activePageId = c.facebook_page_id || fbPagesCache[0].id;
        populatePageDropdown(fbPagesCache, activePageId);
        
        // Auto-sync page id & token if empty
        const curPage = fbPagesCache.find(p => String(p.id) === String(activePageId));
        if (curPage) {
          if (fbPageId && !fbPageId.value) fbPageId.value = curPage.id;
          if (fbPageToken && (!fbPageToken.value || fbPageToken.value.length < 20) && curPage.access_token) {
            fbPageToken.value = curPage.access_token;
          }
        }
      } else if (c.facebook_user_access_token || c.facebook_access_token) {
        fetchFacebookPages(true);
      }
      
      if (c.format) {
        document.getElementById("video-format").value = c.format;
      }
      if (c.tone) {
        document.getElementById("video-tone").value = c.tone;
      }
      updateFormatHelperCard(document.getElementById("video-format").value, document.getElementById("video-tone").value, false);
      
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
  const curPageId = document.getElementById("fb-page-select")?.value;
  const curToken = document.getElementById("fb-page-token")?.value.trim();
  if (curPageId && curToken && fbPagesCache) {
    const page = fbPagesCache.find(p => String(p.id) === String(curPageId));
    if (page) {
      page.access_token = curToken;
    }
  }

  const selectedPages = getSelectedFacebookPages();
  const checkedPageIds = Array.from(document.querySelectorAll(".fb-page-cb:checked")).map(cb => cb.dataset.id);

  const payload = {
    gemini_key: document.getElementById("gemini-key").value.trim(),
    bot_token: document.getElementById("bot-token").value.trim(),
    chat_id: document.getElementById("chat-id").value.trim(),
    facebook_page_id: document.getElementById("fb-page-id")?.value.trim() || "",
    facebook_access_token: document.getElementById("fb-page-token")?.value.trim() || "",
    facebook_user_access_token: document.getElementById("fb-user-token")?.value.trim() || "",
    facebook_auto_post: document.getElementById("fb-auto-post-checkbox")?.checked || false,
    facebook_all_pages: document.getElementById("fb-broadcast-all-checkbox")?.checked || false,
    facebook_selected_pages: fbPagesCache.length > 0 ? fbPagesCache : selectedPages,
    facebook_broadcast_page_ids: checkedPageIds,
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
          if (r.facebook_posted) {
            appendLog(`   📘 ${currentLang === 'km' ? 'បានបង្ហោះឡើង Facebook Page ជោគជ័យ' : 'Posted to Facebook Page successfully'}`, "success");
          } else if (r.facebook_status && r.facebook_status !== "Not configured") {
            appendLog(`   ⚠️ Facebook: ${r.facebook_status}`, "error");
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
      if (historyCache.length > 0 && !selectedScriptId) {
        viewScriptDetail(historyCache[0].id);
      }
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

function copyActiveFormatPrompt() {
  const codeEl = document.getElementById("notebooklm-prompt-content");
  if (!codeEl) return;
  const promptText = codeEl.textContent.trim();
  navigator.clipboard.writeText(promptText).then(() => {
    showToast(currentLang === "km" ? "បានចម្លង Prompt ទៅកាន់ Clipboard រួចរាល់!" : "Prompt copied to clipboard!", "success");
  });
}

function copyNotebookLMEnCCPrompt() {
  copyActiveFormatPrompt();
}

function copyNotebookLMPrompt() {
  copyActiveFormatPrompt();
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

async function postSelectedScriptToFacebook() {
  if (!selectedScriptId) return;
  const btn = document.getElementById("btn-post-facebook");
  if (btn) btn.disabled = true;
  showToast(currentLang === "km" ? "កំពុងបង្ហោះទៅកាន់ Facebook Page..." : "Posting to Facebook Page...", "info");
  
  try {
    const res = await fetch(`/api/history/${selectedScriptId}/post-facebook`, { method: "POST" });
    const data = await res.json();
    if (data.success) {
      showToast(translations[currentLang].msgFbPosted, "success");
    } else {
      showToast("Facebook: " + (data.error || data.message), "error");
    }
  } catch (err) {
    showToast("Network error: " + err.message, "error");
  } finally {
    if (btn) btn.disabled = false;
  }
}

let currentRenderedVideoFilename = null;

async function createReelsVideoForSelectedScript() {
  if (!selectedScriptId) {
    showToast(currentLang === "km" ? "សូមជ្រើសរើសស្គ្រីបមួយជាមុនសិន!" : "Please select a script first!", "error");
    return;
  }
  const btn = document.getElementById("btn-create-video");
  const previewBox = document.getElementById("video-preview-box");
  const player = document.getElementById("rendered-video-player");
  const statusEl = document.getElementById("video-info-status");
  const downloadBtn = document.getElementById("btn-download-video");
  
  if (btn) btn.disabled = true;
  showToast(currentLang === "km" ? "🎬 កំពុងផលិតវីដេអូ Reels (សំឡេងខ្មែរ Neural + B-Roll)..." : "Generating Reels video...", "info");
  if (statusEl) {
    statusEl.textContent = currentLang === "km" ? "⏳ កំពុងផលិតវីដេអូ Reels (សំឡេងខ្មែរ Neural + ប្លង់ B-Roll 9:16)..." : "Rendering video...";
    statusEl.style.color = "#f59e0b";
  }
  
  try {
    const res = await fetch("/api/video/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        script_id: selectedScriptId,
        b_roll: "coconut",
        voice: "km-KH-PisethNeural"
      })
    });
    const data = await res.json();
    if (data.success && data.video_url) {
      currentRenderedVideoFilename = data.filename;
      player.src = data.video_url + "?t=" + Date.now();
      downloadBtn.href = data.video_url;
      previewBox.classList.remove("hidden");
      if (statusEl) {
        statusEl.innerHTML = `✅ <strong>វីដេអូ Reels ផលិតជោគជ័យ!</strong><br>គុណភាព: 1080x1920 (9:16) ជាមួយសំឡេងខ្មែរ Neural Voice និងប្លង់ B-Roll។`;
        statusEl.style.color = "#34d399";
      }
      showToast(currentLang === "km" ? "🎬 វីដេអូ Reels ផលិតជោគជ័យ!" : "Reels video generated successfully!", "success");
      previewBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
    } else {
      showToast("កំហុសផលិតវីដេអូ: " + (data.error || "Unknown"), "error");
      if (statusEl) {
        statusEl.textContent = "❌ " + (data.error || "Failed");
        statusEl.style.color = "#ef4444";
      }
    }
  } catch (err) {
    showToast("Error: " + err.message, "error");
  } finally {
    if (btn) btn.disabled = false;
  }
}

async function broadcastRenderedVideoToFacebook() {
  if (!currentRenderedVideoFilename) {
    showToast(currentLang === "km" ? "មិនទាន់មាន File វីដេអូដែលបានផលិតឡើយ!" : "No generated video available!", "error");
    return;
  }
  const btn = document.getElementById("btn-broadcast-video-fb");
  if (btn) btn.disabled = true;
  showToast(currentLang === "km" ? "🚀 កំពុងបង្ហោះវីដេអូទៅកាន់ Facebook Pages ទាំងអស់..." : "Broadcasting video to Facebook Pages...", "info");
  
  const scriptContent = document.getElementById("preview-content")?.textContent || "";
  const topicTitle = document.getElementById("preview-topic-title")?.textContent || "Reels Video";
  const desc = `🎬 ${topicTitle}\n\n${scriptContent}`;
  
  try {
    const res = await fetch("/api/video/broadcast-facebook", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        filename: currentRenderedVideoFilename,
        description: desc
      })
    });
    const data = await res.json();
    if (data.success) {
      showToast(currentLang === "km" ? "🎉 " + data.message : "Video broadcasted successfully!", "success");
    } else {
      showToast("Facebook: " + (data.error || data.message), "error");
    }
  } catch (err) {
    showToast("Network error: " + err.message, "error");
  } finally {
    if (btn) btn.disabled = false;
  }
}

async function createVeoVideoForSelectedScript() {
  if (!selectedScriptId) {
    showToast(currentLang === "km" ? "សូមជ្រើសរើសស្គ្រីបមួយជាមុនសិន!" : "Please select a script first!", "error");
    return;
  }
  const btn = document.getElementById("btn-create-veo-video");
  const previewBox = document.getElementById("video-preview-box");
  const player = document.getElementById("rendered-video-player");
  const statusEl = document.getElementById("video-info-status");
  const downloadBtn = document.getElementById("btn-download-video");
  
  if (btn) btn.disabled = true;
  showToast(currentLang === "km" ? "✨ កំពុងភ្ជាប់ទៅកាន់ Google Veo AI Video (Gemini)..." : "Connecting to Google Veo AI Video...", "info");
  if (statusEl) {
    statusEl.textContent = currentLang === "km" ? "⏳ កំពុងដំណើរការ Google Veo AI Video (9:16 Cinematic Reels)..." : "Generating Google Veo AI Video...";
    statusEl.style.color = "#60a5fa";
  }
  previewBox.classList.remove("hidden");
  previewBox.scrollIntoView({ behavior: "smooth", block: "nearest" });
  
  try {
    const res = await fetch("/api/video/veo", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        script_id: selectedScriptId
      })
    });
    const data = await res.json();
    if (data.success && data.video_url) {
      currentRenderedVideoFilename = data.filename;
      player.src = data.video_url + "?t=" + Date.now();
      downloadBtn.href = data.video_url;
      if (statusEl) {
        statusEl.innerHTML = `✅ <strong>${data.message}</strong><br>គុណភាព: 1080x1920 (9:16 Vertical) រួចរាល់សម្រាប់បង្ហោះចូល Facebook Pages!`;
        statusEl.style.color = "#34d399";
      }
      showToast(currentLang === "km" ? "🎉 វីដេអូ AI ផលិតជោគជ័យ!" : "AI video generated successfully!", "success");
    } else {
      showToast("Google Veo: " + (data.error || "Failed"), "error");
      if (statusEl) {
        statusEl.textContent = "❌ " + (data.error || "Failed");
        statusEl.style.color = "#ef4444";
      }
    }
  } catch (err) {
    showToast("Network error: " + err.message, "error");
  } finally {
    if (btn) btn.disabled = false;
  }
}

async function broadcastCustomVideoUrl() {
  const inputEl = document.getElementById("custom-video-url-input");
  const url = inputEl?.value.trim();
  const statusEl = document.getElementById("url-broadcast-status");
  const btn = document.getElementById("btn-broadcast-url-fb");
  
  if (!url) {
    showToast(currentLang === "km" ? "សូមបញ្ចូល Link វីដេអូ (MP4 URL) ជាមុនសិន!" : "Please enter a video URL first!", "error");
    return;
  }
  
  const scriptContent = document.getElementById("preview-content")?.textContent || "";
  const topicTitle = document.getElementById("preview-topic-title")?.textContent || "Reels Video";
  const desc = scriptContent ? `🎬 ${topicTitle}\n\n${scriptContent}` : "🎬 New Video Release #Reels";
  
  if (btn) btn.disabled = true;
  if (statusEl) {
    statusEl.textContent = currentLang === "km" ? "🚀 កំពុងបញ្ជូន Link ទៅកាន់ Facebook តាម URL Pull..." : "Sending video URL to Facebook via URL Pull...";
    statusEl.style.color = "#60a5fa";
  }
  showToast(currentLang === "km" ? "🚀 កំពុងបញ្ជូន Link ទៅកាន់ Facebook Pages ទាំងអស់..." : "Broadcasting video URL to Facebook Pages...", "info");
  
  try {
    const res = await fetch("/api/facebook/broadcast-url", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        video_url: url,
        description: desc
      })
    });
    const data = await res.json();
    if (data.success) {
      if (statusEl) {
        statusEl.textContent = "✅ " + data.message;
        statusEl.style.color = "#34d399";
      }
      showToast(currentLang === "km" ? "🎉 " + data.message : "Broadcasted successfully via URL Pull!", "success");
    } else {
      if (statusEl) {
        statusEl.textContent = "❌ " + (data.error || data.message);
        statusEl.style.color = "#ef4444";
      }
      showToast("Facebook: " + (data.error || data.message), "error");
    }
  } catch (err) {
    if (statusEl) {
      statusEl.textContent = "❌ Network error: " + err.message;
      statusEl.style.color = "#ef4444";
    }
    showToast("Network error: " + err.message, "error");
  } finally {
    if (btn) btn.disabled = false;
  }
}

async function verifyFacebookPage() {
  const pageId = document.getElementById("fb-page-id")?.value.trim();
  const pageToken = document.getElementById("fb-page-token")?.value.trim();
  const userToken = document.getElementById("fb-user-token")?.value.trim();
  const token = pageToken || userToken;
  const statusEl = document.getElementById("fb-verify-status");
  const btn = document.getElementById("btn-verify-fb");
  
  if (!pageId || !token) {
    showToast(currentLang === "km" ? "សូមបញ្ចូល Facebook Page ID និង Access Token ជាមុនសិន!" : "Please enter Facebook Page ID and Access Token first!", "error");
    return;
  }
  
  if (btn) btn.disabled = true;
  if (statusEl) statusEl.textContent = currentLang === "km" ? "កំពុងផ្ទៀងផ្ទាត់..." : "Verifying...";
  
  try {
    const res = await fetch("/api/facebook/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        facebook_page_id: pageId,
        facebook_access_token: token
      })
    });
    const data = await res.json();
    if (data.success) {
      if (statusEl) {
        statusEl.textContent = "✅ " + data.message;
        statusEl.style.color = "#34d399";
      }
      showToast(translations[currentLang].msgFbVerified, "success");
    } else {
      if (statusEl) {
        statusEl.textContent = "❌ " + data.message;
        statusEl.style.color = "#ef4444";
      }
      showToast(data.message, "error");
    }
  } catch (err) {
    if (statusEl) {
      statusEl.textContent = "❌ Error: " + err.message;
      statusEl.style.color = "#ef4444";
    }
  } finally {
    if (btn) btn.disabled = false;
  }
}

let fbPagesCache = [];

function renderPagesChecklist(pages, selectedIds = []) {
  const container = document.getElementById("fb-pages-container");
  const checklist = document.getElementById("fb-pages-checklist");
  const countEl = document.getElementById("fb-pages-count");
  if (!container || !checklist) return;
  
  if (!pages || pages.length === 0) {
    container.classList.add("hidden");
    return;
  }
  
  container.classList.remove("hidden");
  if (countEl) countEl.textContent = pages.length;
  checklist.innerHTML = "";
  
  pages.forEach(p => {
    const isChecked = selectedIds.length === 0 || selectedIds.includes(p.id);
    const item = document.createElement("label");
    item.className = "page-check-item";
    item.innerHTML = `
      <input type="checkbox" class="fb-page-cb" data-id="${p.id}" ${isChecked ? "checked" : ""}>
      <span class="page-name">${p.name}</span>
      <span class="page-id-badge">ID: ${p.id}</span>
    `;
    checklist.appendChild(item);
  });
}

function populatePageDropdown(pages, selectedId = "") {
  const selectEl = document.getElementById("fb-page-select");
  const countBadge = document.getElementById("badge-page-count");
  if (!selectEl || !pages || pages.length === 0) return;
  
  if (countBadge) {
    countBadge.textContent = `${pages.length} Pages Ready`;
  }
  
  selectEl.innerHTML = `<option value="">-- ${currentLang === 'km' ? 'សូមជ្រើសរើស Page (' + pages.length + ' Pages រួចរាល់)' : 'Choose a Page (' + pages.length + ' Pages Ready)'} --</option>`;
  pages.forEach(p => {
    const opt = document.createElement("option");
    opt.value = p.id;
    opt.textContent = `${p.name} (ID: ${p.id})`;
    if (selectedId && String(p.id) === String(selectedId)) {
      opt.selected = true;
    }
    selectEl.appendChild(opt);
  });
}

function getSelectedFacebookPages() {
  const checkboxes = document.querySelectorAll(".fb-page-cb:checked");
  const selected = [];
  checkboxes.forEach(cb => {
    const id = cb.dataset.id;
    const page = fbPagesCache.find(p => p.id === id);
    if (page) {
      selected.push({
        id: page.id,
        name: page.name,
        access_token: page.access_token
      });
    }
  });
  return selected;
}

async function fetchFacebookPages(silent = false) {
  const userToken = document.getElementById("fb-user-token")?.value.trim();
  const pageToken = document.getElementById("fb-page-token")?.value.trim();
  const token = userToken || pageToken;
  const btn = document.getElementById("btn-fetch-fb-pages");
  const statusEl = document.getElementById("fb-verify-status");
  const selectEl = document.getElementById("fb-page-select");
  
  if (!token) {
    if (!silent) showToast(currentLang === "km" ? "សូមបញ្ចូល Facebook User Token ឬ Page Token ជាមុនសិន!" : "Please enter Facebook User Token or Page Token first!", "error");
    return;
  }
  
  if (btn) btn.disabled = true;
  if (statusEl) {
    statusEl.textContent = currentLang === "km" ? "កំពុងទាញយក Pages..." : "Fetching pages...";
    statusEl.style.color = "#94a3b8";
  }
  
  try {
    const res = await fetch("/api/facebook/pages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ 
        user_access_token: userToken,
        access_token: token 
      })
    });
    const data = await res.json();
    if (data.success && data.pages && data.pages.length > 0) {
      fbPagesCache = data.pages;
      renderPagesChecklist(fbPagesCache);
      
      populatePageDropdown(fbPagesCache, selectEl.value || fbPagesCache[0]?.id);
      
      // If page token is currently empty, auto-populate with the first page's token
      if (!pageToken && data.pages[0]?.access_token) {
        const pageTokenInput = document.getElementById("fb-page-token");
        const pageIdInput = document.getElementById("fb-page-id");
        if (pageTokenInput) pageTokenInput.value = data.pages[0].access_token;
        if (pageIdInput) pageIdInput.value = data.pages[0].id;
      }

      if (statusEl) {
        if (data.pages.length === 1) {
          statusEl.textContent = `✅ ${currentLang === 'km' ? 'បានភ្ជាប់ Page \'' + data.pages[0].name + '\' (ដើម្បីគ្រប់គ្រងគ្រប់ ២៣ Pages សូមប្រើ User Token ខាងលើ)' : 'Connected Page \'' + data.pages[0].name + '\' (Use User Token above for all 23 Pages)'}`;
        } else {
          statusEl.textContent = `✅ ${currentLang === 'km' ? 'បានរកឃើញ ' + data.pages.length + ' Pages តាមរយៈ User Token!' : 'Found ' + data.pages.length + ' Pages via User Token!'}`;
        }
        statusEl.style.color = "#34d399";
      }
      if (!silent) showToast(data.pages.length > 1 ? (currentLang === 'km' ? `បានរកឃើញ ${data.pages.length} Pages ជោគជ័យ!` : `Loaded ${data.pages.length} Facebook Pages!`) : (currentLang === 'km' ? 'បានភ្ជាប់ Page ' + data.pages[0].name : 'Connected Page ' + data.pages[0].name), "success");
    } else {
      const isExpired = (data.message || "").toLowerCase().includes("expired");
      if (statusEl) {
        statusEl.textContent = isExpired 
          ? (currentLang === "km" ? "⚠️ Facebook Token បានផុតកំណត់ (Expired) - សូមបង្កើត Token ថ្មីក្នុង Graph API Explorer" : "⚠️ Facebook Token expired - please generate a new token")
          : "❌ " + (data.message || "No pages found");
        statusEl.style.color = isExpired ? "#f59e0b" : "#ef4444";
      }
      if (!silent) {
        showToast(isExpired ? (currentLang === "km" ? "Facebook Token បានផុតកំណត់ សូមបង្កើត Token ថ្មី" : "Facebook Token expired") : (data.message || "Failed to load pages"), "error");
      }
    }
  } catch (err) {
    if (statusEl) {
      statusEl.textContent = "❌ Error: " + err.message;
      statusEl.style.color = "#ef4444";
    }
  } finally {
    if (btn) btn.disabled = false;
  }
}

function handleFacebookPageSelect(e) {
  const selectedId = e.target.value;
  if (!selectedId) return;
  const page = fbPagesCache.find(p => String(p.id) === String(selectedId));
  if (page) {
    const idInput = document.getElementById("fb-page-id");
    const tokenInput = document.getElementById("fb-page-token");
    const statusEl = document.getElementById("fb-verify-status");
    if (idInput) idInput.value = page.id;
    if (tokenInput) {
      tokenInput.value = page.access_token || "";
    }
    if (statusEl) {
      statusEl.textContent = `✅ បានជ្រើសរើស: ${page.name} (ID: ${page.id})`;
      statusEl.style.color = "#34d399";
    }
    showToast(currentLang === "km" ? `បានជ្រើសរើស Page៖ ${page.name}` : `Selected Page: ${page.name}`, "info");
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
      showToast(translations[currentLang]?.msgSaved || "បានរក្សាទុកការកំណត់ជោគជ័យ!", "success");
    } else {
      showToast(data.error || "Error saving schedule", "error");
    }
  } catch (err) {
    showToast("Error saving schedule: " + (err.message || err), "error");
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
