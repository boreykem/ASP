from google import genai
import google.generativeai as genai_legacy
import warnings

warnings.filterwarnings('ignore')

MODELS_PRIORITY = [
    'gemini-flash-lite-latest',
    'gemini-3.5-flash-lite',
    'gemini-3.5-flash',
    'gemini-flash-latest',
    'gemini-3.8-flash'
]

NOTEBOOKLM_KHMER_DIRECTIVE = (
    "======================================================================\n"
    "🎙️ NOTEBOOKLM PODCAST: STRICT KHMER DISCUSSION DIRECTIVE 🎙️\n"
    "• ភាសានិយាយ (Spoken Language): ភាសាខ្មែរ (Khmer) ១០០% ទាំងស្រុង។\n"
    "• ពិធីករ និងវាគ្មិនទាំងអស់ (All Hosts & Speakers) ត្រូវតែជជែក សន្ទនា និងអានជាភាសាខ្មែរសុទ្ធសាធ។\n"
    "• ហាមដាច់ខាតកុំនិយាយ ឬបកប្រែជាភាសាអង់គ្លេស (Strictly NO English voiceover or speech).\n"
    "• Every spoken dialogue and audio overview in NotebookLM must be in natural Khmer.\n"
    "======================================================================\n\n"
)

NOTEBOOKLM_EXPLAINER_VIDEO_DIRECTIVE = (
    "======================================================================\n"
    "🎬 GOOGLE NOTEBOOKLM: 5+ MINUTE EXPLAINER VIDEO OVERVIEW DIRECTIVE 🎬\n"
    "• FORMAT: EXPLAINER VIDEO OVERVIEW (វីដេអូបទបង្ហាញពន្យល់បែបអប់រំ និងចំណេះដឹង - មិនមែន Podcast ទេ).\n"
    "• DURATION: 5+ MINUTES (Extensive Multi-Scene Video Presentation).\n"
    "• SPOKEN NARRATION / VOICEOVER: 100% fluent Khmer language (ភាសាខ្មែរ). Single AI presenter delivering a clear, engaging explanation in Khmer.\n"
    "• ON-SCREEN TEXT, SLIDES & CLOSED CAPTIONS (CC): 100% ENGLISH (to ensure perfect visual presentation without font tofu box glitches).\n"
    "======================================================================\n\n"
)

TIKTOK_SHORTS_DIRECTIVE = (
    "======================================================================\n"
    "📱 TIKTOK / REELS / SHORTS SCRIPT (ខ្លីក្រោម ៦០ វិនាទី) 📱\n"
    "• ទម្រង់វីដេអូ៖ បញ្ឈរ 9:16 កាត់តលឿន រស់រវើក ទាក់ទាញក្នុង ៣ វិនាទីដំបូង\n"
    "• រយៈពេលសរុប៖ ៣០ ទៅ ៦០ វិនាទី\n"
    "• រចនាសម្ព័ន្ធ៖ [0-3s Hook] -> [3-45s ខ្លឹមសាររហ័ស & Visuals] -> [45-60s CTA]\n"
    "======================================================================\n\n"
)

YOUTUBE_VIDEO_DIRECTIVE = (
    "======================================================================\n"
    "📹 YOUTUBE VIDEO SCRIPT (២-៣ នាទី - កម្រិតមធ្យម) 📹\n"
    "• ទម្រង់វីដេអូ៖ ផ្តេក 16:9 ស៊ីជម្រៅ លម្អិត និងមានរចនាសម្ព័ន្ធច្បាស់លាស់\n"
    "• រយៈពេលសរុប៖ ២ ទៅ ៣ នាទី\n"
    "• រចនាសម្ព័ន្ធ៖ [Intro & Hook] -> [Body ៣ ចំណុចសំខាន់ៗ] -> [Outro & Subscribe CTA]\n"
    "======================================================================\n\n"
)

def generate_script(api_key, topic, platform="TikTok", tone="ទាក់ទាញ", lang="km"):
    api_key = (api_key or "").strip().strip("'").strip('"')
    if not api_key:
        return False, "API Key is required", None
        
    plat_str = str(platform).lower()
    is_video_overview = any(k in plat_str for k in ["video overview", "explainer", "៥+ នាទី", "5+ នាទី", "5 នាទី", "cc អង់គ្លេស"])
    is_podcast = any(k in plat_str for k in ["podcast", "សន្ទនា", "២ នាក់"])
    is_tiktok = any(k in plat_str for k in ["tiktok", "reels", "shorts", "៦០ វិនាទី", "60"])
    is_youtube = any(k in plat_str for k in ["youtube", "២-៣ នាទី", "2-3"])

    if lang == "en":
        prompt = (
            f"Write an engaging video script for the topic: '{topic}'\n\n"
            f"Specifications:\n"
            f"- Platform format: {platform}\n"
            f"- Tone: {tone}\n"
            f"- Clear stage directions and spoken voiceover lines."
        )
    else:
        if is_video_overview:
            prompt = (
                f"🚨 GOOGLE NOTEBOOKLM: 5+ MINUTES EXPLAINER VIDEO OVERVIEW SCRIPT 🚨\n"
                f"ចំណាំសំខាន់បំផុត៖ នេះជា 'Video Overview - Explainer Video' (មិនមែនជា Podcast ឬការសន្ទនា ២ នាក់ឡើយ)។\n"
                f"អ្នកត្រូវសរសេរស្គ្រីបសម្រាប់អ្នកធ្វើបទបង្ហាញ (AI Presenter / Narrator) ពន្យល់យ៉ាងក្បោះក្បាយ អមដោយស្លាយរូបភាព និងអក្សរបង្ហាញលើអេក្រង់។\n\n"
                f"គោលដៅ និងលក្ខខណ្ឌកំណត់៖\n"
                f"១. រយៈពេលវីដេអូ (Duration): ៥ ទៅ ៧ នាទី (ប្រវែងប្រហែល ៨០០ ទៅ ១២០០ ពាក្យ ស៊ីជម្រៅ មិនសង្ខេបកាត់ៗឡើយ)។\n"
                f"២. សំឡេងអាន (Voiceover / Narration): ភាសាខ្មែរ (Khmer) ១០០% ទាំងស្រុង ពិរោះ ច្បាស់ៗ រស់រវើក និងទាក់ទាញ។ គ្មានសំឡេងអង់គ្លេសឡើយ។\n"
                f"៣. ស្លាយ និងអក្សររត់លើអេក្រង់ (On-Screen Slides & CC): ភាសាអង់គ្លេស (English) ១០០% ដើម្បីឱ្យវីដេអូមាន Slide ស្អាត និងគ្មានបញ្ហាចេញប្រអប់ការេ (Tofu Font Box Error)។\n\n"
                f"ប្រធានបទវីដេអូ៖ '{topic}'\n"
                f"ទឹកដមសម្លេង៖ {tone}\n\n"
                f"សូមចាប់ផ្តើមដោយដាក់ Header ខាងក្រោមនេះនៅបន្ទាត់ទីមួយជានិច្ច៖\n"
                f"{NOTEBOOKLM_EXPLAINER_VIDEO_DIRECTIVE}"
                f"រចនាសម្ព័ន្ធស្គ្រីប Explainer Video ៥+ នាទី (សូមបែងចែកជា ៧ ឈុតឆាក/Scenes លម្អិត)៖\n"
                f"សម្រាប់ Scene នីមួយៗ សូមសរសេរតាមទម្រង់ស្តង់ដារនេះ៖\n\n"
                f"[Scene X: Section Title in English]\n"
                f"• On-Screen Slide (English): [ចំណងជើងស្លាយ & Bullet Points ជាភាសាអង់គ្លេសសម្រាប់បង្ហាញលើវីដេអូ]\n"
                f"• Voiceover (ភាសាខ្មែរ): [ខ្លឹមសារអាន និងពន្យល់ជាភាសាខ្មែរយ៉ាងពិស្តារ លម្អិត លើកឧទាហរណ៍ជាក់ស្តែង]\n"
                f"• [English CC]: [អត្ថបទបកប្រែជាភាសាអង់គ្លេសសម្រាប់ Closed Captions]\n\n"
                f"សូមរៀបចំឈុតឆាកទាំង ៧ ដូចខាងក្រោម៖\n"
                f"- Scene 1: Introduction & Hook (សេចក្តីផ្តើមទាក់ទាញ & បញ្ហាចម្បង)\n"
                f"- Scene 2: Background & Core Concept (ប្រវត្តិ និងគោលគំនិតស្នូល)\n"
                f"- Scene 3: In-Depth Analysis - Key Pillar 1 (ការវិភាគស៊ីជម្រៅ ចំណុចទី ១)\n"
                f"- Scene 4: In-Depth Analysis - Key Pillar 2 (ការវិភាគស៊ីជម្រៅ ចំណុចទី ២)\n"
                f"- Scene 5: Real-World Case Study & Examples (ករណីសិក្សា និងឧទាហរណ៍ជាក់ស្តែង)\n"
                f"- Scene 6: Practical Implementation & Actionable Steps (វិធីសាស្ត្រអនុវត្តជាក់ស្តែង)\n"
                f"- Scene 7: Final Takeaways & Conclusion (សេចក្តីសន្និដ្ឋាន និងពាក្យផ្តាំផ្ញើបញ្ចប់)"
            )
        elif is_podcast:
            prompt = (
                f"🚨 សេចក្តីណែនាំដាច់ខាតសម្រាប់ GOOGLE NOTEBOOKLM PODCAST 🚨\n"
                f"អ្នកប្រើប្រាស់នឹងចម្លងស្គ្រីបនេះទៅបង្កើត Podcast កិច្ចសន្ទនា ២ នាក់ក្នុង NotebookLM។\n"
                f"ដើម្បីធានាថា NotebookLM AI Hosts និយាយជាភាសាខ្មែរ ១០០% ជានិច្ច ដោយមិនលាយភាសាអង់គ្លេសឡើយ៖\n"
                f"១. ត្រូវសរសេរខ្លឹមសារទាំងមូលជាភាសាខ្មែរសុទ្ធសាធ (Khmer Language 100%)។\n"
                f"២. ហាមប្រើពាក្យអង់គ្លេសក្នុងស្លាក Heading ទាំងអស់។ សូមប្រើ៖ ពិធីករ ទី១, ពិធីការិនី ទី២។\n"
                f"៣. បង្កើតជាទម្រង់កិច្ចសន្ទនា ជជែកវែកញែកស៊ីជម្រៅរវាង ពិធីករ ទី១ និង ពិធីការិនី ទី២ យ៉ាងរស់រវើក ជក់ចិត្ត និងពោរពេញដោយចំណេះដឹង។\n\n"
                f"ប្រធានបទ៖ '{topic}'\n"
                f"ទឹកដមសម្លេង៖ {tone}\n\n"
                f"សូមចាប់ផ្តើមស្គ្រីបដោយដាក់ Header ខាងក្រោមនេះនៅបន្ទាត់ទីមួយជានិច្ច៖\n"
                f"{NOTEBOOKLM_KHMER_DIRECTIVE}"
                f"បន្ទាប់មកសរសេរកិច្ចពិភាក្សាជាភាសាខ្មែរពេញលេញរវាង ពិធីករ ទី១ និង ពិធីការិនី ទី២។"
            )
        elif is_tiktok:
            prompt = (
                f"🚨 ស្គ្រីបវីដេអូខ្លី TIKTOK / REELS / SHORTS (ខ្លីក្រោម ៦០ វិនាទី) 🚨\n"
                f"អ្នកត្រូវសរសេរស្គ្រីបវីដេអូខ្លីបញ្ឈរ (9:16) មួយជាភាសាខ្មែរយ៉ាងរស់រវើក និងទាក់ទាញបំផុតសម្រាប់ប្រធានបទ៖ '{topic}'\n\n"
                f"លក្ខខណ្ឌកំណត់៖\n"
                f"១. រយៈពេលសរុប (Duration): ក្រោម ៦០ វិនាទី (ប្រហែល ១០០ ទៅ ១៥០ ពាក្យ កាត់តលឿន មិនវែងអន្លាយឡើយ)។\n"
                f"២. ភាសា (Language): ភាសាខ្មែរ (Khmer) ១០០% ទឹកដមសម្លេង៖ {tone}។\n\n"
                f"សូមចាប់ផ្តើមដោយដាក់ Header ខាងក្រោមនេះនៅបន្ទាត់ទីមួយជានិច្ច៖\n"
                f"{TIKTOK_SHORTS_DIRECTIVE}"
                f"រចនាសម្ព័ន្ធស្គ្រីប TikTok / Shorts (សូមប្រើតែភាសាខ្មែរ)៖\n"
                f"• [00:00 - 00:03] HOOK (បើកឆាកទាក់ទាញខ្លាំងភ្លាមៗ ធ្វើឱ្យគេឈប់អូសរំលង)៖\n"
                f"  - សំឡេងអាន (Voiceover): ...\n"
                f"  - អក្សររត់លើអេក្រង់ (On-Screen Text): ...\n"
                f"  - ប្លង់រូបភាព/សកម្មភាព (Visual Cue): ...\n\n"
                f"• [00:03 - 00:45] CORE VALUE (ខ្លឹមសារស្នូលរហ័ស ៣ ចំណុចខ្លី ខ្លឹម)៖\n"
                f"  - ចំណុចទី ១: [សំឡេងអាន & ប្លង់រូបភាព]\n"
                f"  - ចំណុចទី ២: [សំឡេងអាន & ប្លង់រូបភាព]\n"
                f"  - ចំណុចទី ៣: [សំឡេងអាន & ប្លង់រូបភាព]\n\n"
                f"• [00:45 - 00:60] CALL TO ACTION (CTA ដាស់តឿនបញ្ចប់)៖\n"
                f"  - សំឡេងអាន (Voiceover): [អំពាវនាវឱ្យចុច Like, Follow និងបញ្ចេញមតិយោបល់]\n"
                f"  - អក្សររត់លើអេក្រង់: [ចុច Follow & Share]"
            )
        elif is_youtube:
            prompt = (
                f"🚨 ស្គ្រីបវីដេអូ YOUTUBE VIDEO (២-៣ នាទី - កម្រិតមធ្យម) 🚨\n"
                f"អ្នកត្រូវសរសេរស្គ្រីបវីដេអូ YouTube កម្រិតមធ្យមមួយជាភាសាខ្មែរយ៉ាងស៊ីជម្រៅសម្រាប់ប្រធានបទ៖ '{topic}'\n\n"
                f"លក្ខខណ្ឌកំណត់៖\n"
                f"១. រយៈពេលសរុប (Duration): ២ ទៅ ៣ នាទី (ប្រហែល ៤០០ ទៅ ៦០០ ពាក្យ មានព័ត៌មានលម្អិត និងឧទាហរណ៍)។\n"
                f"២. ភាសា (Language): ភាសាខ្មែរ (Khmer) ១០០% ទឹកដមសម្លេង៖ {tone}។\n\n"
                f"សូមចាប់ផ្តើមដោយដាក់ Header ខាងក្រោមនេះនៅបន្ទាត់ទីមួយជានិច្ច៖\n"
                f"{YOUTUBE_VIDEO_DIRECTIVE}"
                f"រចនាសម្ព័ន្ធស្គ្រីប YouTube Video ២-៣ នាទី (សូមប្រើតែភាសាខ្មែរ)៖\n"
                f"• [00:00 - 00:20] INTRO & HOOK (សេចក្តីផ្តើម & បញ្ហាស្នូល)៖\n"
                f"  - សំឡេងអាន: [សេចក្តីផ្តើមទាក់ទាញ និងប្រាប់ពីអត្ថប្រយោជន៍ដែលទស្សនិកជននឹងទទួលបាន]\n"
                f"  - Visual Cue / B-Roll: [ការណែនាំរូបភាពឬវីដេអូប្លង់កាត់]\n\n"
                f"• [00:20 - 02:00] BODY CONTENT (ខ្លឹមសារស៊ីជម្រៅ ៣ ចំណុចធំៗ)៖\n"
                f"  - ចំណុចទី ១: [ការពន្យល់លម្អិត + B-Roll Cue]\n"
                f"  - ចំណុចទី ២: [ការពន្យល់លម្អិត + ឧទាហរណ៍ជាក់ស្តែង + B-Roll Cue]\n"
                f"  - ចំណុចទី ៣: [ការពន្យល់លម្អិត + គន្លឹះអនុវត្ត + B-Roll Cue]\n\n"
                f"• [02:00 - 02:30] OUTRO & CTA (សេចក្តីសន្និដ្ឋាន & ដាស់តឿនបញ្ចប់)៖\n"
                f"  - សេចក្តីសង្ខេបចំណុចសំខាន់ៗ\n"
                f"  - សំណួរជំរុញឱ្យទស្សនិកជន Comment\n"
                f"  - អំពាវនាវឱ្យចុច Subscribe, Like និងចែករំលែក"
            )
        else:
            prompt = (
                f"សូមសរសេរស្គ្រីបវីដេអូទាក់ទាញមួយជាភាសាខ្មែរសម្រាប់ប្រធានបទ៖ '{topic}'\n\n"
                f"ការកំណត់លម្អិត៖\n"
                f"- ទម្រង់មាតិកា (Format): {platform}\n"
                f"- ទឹកដមសម្លេង (Tone): {tone}\n"
                f"- រចនាសម្ព័ន្ធស្គ្រីប (សូមប្រើតែភាសាខ្មែរ)៖\n"
                f"  ១. [វគ្គទី ១៖ បើកឆាកទាក់ទាញខ្លាំង (៣ វិនាទីដំបូង)]\n"
                f"  ២. [វគ្គទី ២៖ ខ្លឹមសារស្នូលលម្អិត (ងាយយល់ និងមានប្រយោជន៍)]\n"
                f"  ៣. [វគ្គទី ៣៖ សេចក្តីសន្និដ្ឋាន & អំពាវនាវបញ្ចប់]\n"
            )
        
    def _attach_directive(text):
        cleaned = text.strip()
        if is_video_overview and "NOTEBOOKLM" not in cleaned.upper():
            return NOTEBOOKLM_EXPLAINER_VIDEO_DIRECTIVE + cleaned
        elif is_podcast and "NOTEBOOKLM" not in cleaned.upper():
            return NOTEBOOKLM_KHMER_DIRECTIVE + cleaned
        elif is_tiktok and "TIKTOK" not in cleaned.upper():
            return TIKTOK_SHORTS_DIRECTIVE + cleaned
        elif is_youtube and "YOUTUBE" not in cleaned.upper():
            return YOUTUBE_VIDEO_DIRECTIVE + cleaned
        return cleaned

    last_error = None
    
    # 1. Modern google.genai
    try:
        client = genai.Client(api_key=api_key)
        for model_id in MODELS_PRIORITY:
            try:
                res = client.models.generate_content(model=model_id, contents=prompt)
                if res and res.text:
                    return True, _attach_directive(res.text), model_id
            except Exception as err:
                last_error = err
                err_str = str(err)
                if 'API_KEY_INVALID' in err_str or 'API key not valid' in err_str:
                    return False, f"Invalid API Key: {err_str}", None
                continue
    except Exception as e:
        last_error = e

    # 2. Legacy fallback
    try:
        genai_legacy.configure(api_key=api_key)
        for model_id in MODELS_PRIORITY:
            try:
                model = genai_legacy.GenerativeModel(model_id)
                res = model.generate_content(prompt)
                if res and res.text:
                    return True, _attach_directive(res.text), model_id
            except Exception as err:
                last_error = err
                continue
        return False, f"Model error: {str(last_error)}", None
    except Exception as e:
        return False, str(e), None

def suggest_topics(api_key, niche, lang="km"):
    api_key = (api_key or "").strip().strip("'").strip('"')
    if not api_key:
        return False, "API Key is required"

    if lang == "en":
        prompt = (
            f"Suggest 5 viral, engaging short video topics (TikTok/Reels/Shorts) for the niche: '{niche}'.\n"
            f"Provide exactly 5 lines (1 topic per line, no numbering, no bullet points, no extra text)."
        )
    else:
        prompt = (
            f"សូមជួយណែនាំប្រធានបទស្គ្រីបវីដេអូខ្លី (TikTok/Reels/Shorts) ដែលកំពុងពេញនិយម និងទាក់ទាញចំនួន ៥ "
            f"ទាក់ទងនឹងវិស័យ៖ '{niche}'។\n"
            f"សូមផ្តល់ចម្លើយជាភាសាខ្មែរ ត្រឹមតែ ៥ បន្ទាត់ប៉ុណ្ណោះ (មួយបន្ទាត់ប្រធានបទមួយ ហាមដាក់លេខរៀង 1 2 3 ឬសញ្ញាពិសេស)។"
        )

    try:
        client = genai.Client(api_key=api_key)
        for m in MODELS_PRIORITY:
            try:
                res = client.models.generate_content(model=m, contents=prompt)
                if res and res.text:
                    lines = [l.strip('- *•1234567890. ') for l in res.text.strip().split('\n') if l.strip()]
                    return True, lines[:5]
            except Exception:
                continue
    except Exception:
        pass

    try:
        genai_legacy.configure(api_key=api_key)
        for m in MODELS_PRIORITY:
            try:
                model = genai_legacy.GenerativeModel(m)
                res = model.generate_content(prompt)
                if res and res.text:
                    lines = [l.strip('- *•1234567890. ') for l in res.text.strip().split('\n') if l.strip()]
                    return True, lines[:5]
            except Exception:
                continue
    except Exception as e:
        return False, str(e)

    return False, "Could not generate topics"
