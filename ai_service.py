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
    "🚨 NOTEBOOKLM / AI VIDEO SYSTEM DIRECTIVE: STRICT KHMER AUDIO & VIDEO 🚨\n"
    "• ភាសានិយាយ (Spoken Language): ភាសាខ្មែរ (Khmer) ១០០% ទាំងស្រុង។\n"
    "• ពិធីករ និងវាគ្មិនទាំងអស់ (All Hosts & Speakers) ត្រូវតែជជែក សន្ទនា និងអានជាភាសាខ្មែរសុទ្ធសាធ។\n"
    "• ហាមដាច់ខាតកុំនិយាយ ឬបកប្រែជាភាសាអង់គ្លេស (Strictly NO English voiceover or speech).\n"
    "• Every spoken dialogue and audio overview in NotebookLM must be in natural Khmer.\n"
    "======================================================================\n\n"
)

NOTEBOOKLM_EXPLAINER_VIDEO_DIRECTIVE = (
    "======================================================================\n"
    "🚨 GOOGLE NOTEBOOKLM: 5+ MINUTE EXPLAINER VIDEO OVERVIEW DIRECTIVE 🚨\n"
    "• FORMAT: EXPLAINER VIDEO OVERVIEW (វីដេអូបទបង្ហាញពន្យល់បែបអប់រំ និងចំណេះដឹង - មិនមែន Podcast ទេ).\n"
    "• DURATION: 5+ MINUTES (Extensive Multi-Scene Video Presentation).\n"
    "• SPOKEN NARRATION / VOICEOVER: 100% fluent Khmer language (ភាសាខ្មែរ). Single AI presenter delivering a clear, engaging explanation in Khmer.\n"
    "• ON-SCREEN TEXT, SLIDES & CLOSED CAPTIONS (CC): 100% ENGLISH (to ensure perfect visual presentation without font tofu box glitches).\n"
    "======================================================================\n\n"
)

def generate_script(api_key, topic, platform="TikTok", tone="ទាក់ទាញ", lang="km"):
    api_key = (api_key or "").strip().strip("'").strip('"')
    if not api_key:
        return False, "API Key is required", None
        
    if lang == "en":
        prompt = (
            f"Write an engaging short video script for the topic: '{topic}'\n\n"
            f"Specifications:\n"
            f"- Platform format: {platform}\n"
            f"- Tone: {tone}\n"
            f"- Structure:\n"
            f"  1. [Hook] (First 3-5 seconds high curiosity grabber)\n"
            f"  2. [Core Content] (Engaging, practical insights)\n"
            f"  3. [Call to Action] (Closing prompt to comment, follow, or share)\n"
            f"Format with clear stage directions and spoken voiceover lines."
        )
    else:
        is_video_overview = any(k in str(platform).lower() for k in ["video overview", "explainer", "៥+ នាទី", "5+ នាទី", "5 នាទី", "cc អង់គ្លេស"])
        is_podcast = any(k in str(platform).lower() for k in ["podcast", "សន្ទនា"])
        
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
        else:
            prompt = (
                f"🚨 សេចក្តីណែនាំដាច់ខាតសម្រាប់ GOOGLE NOTEBOOKLM & AI VIDEO GENERATOR 🚨\n"
                f"អ្នកប្រើប្រាស់នឹងចម្លងស្គ្រីបនេះទៅបង្កើតវីដេអូ ឬសំឡេងក្នុង Google NotebookLM (Audio/Video Overview)។\n"
                f"ដើម្បីបង្ការកុំឱ្យ NotebookLM ជ្រើសរើសសំឡេងនិយាយជាភាសាអង់គ្លេស អ្នកត្រូវតែសរសេរជាភាសាខ្មែរ ១០០% ទាំងស្រុង ដោយគ្មានពាក្យអង់គ្លេសលាយឡើយ។\n\n"
                f"សូមសរសេរស្គ្រីបវីដេអូទាក់ទាញមួយជាភាសាខ្មែរសម្រាប់ប្រធានបទ៖ '{topic}'\n\n"
                f"ការកំណត់លម្អិត៖\n"
                f"- ទម្រង់មាតិកា (Format): {platform}\n"
                f"- ទឹកដមសម្លេង (Tone): {tone}\n"
                f"- រចនាសម្ព័ន្ធស្គ្រីប (សូមប្រើតែភាសាខ្មែរ)៖\n"
                f"  ១. [វគ្គទី ១៖ បើកឆាកទាក់ទាញខ្លាំង (៣ វិនាទីដំបូង)]\n"
                f"  ២. [វគ្គទី ២៖ ខ្លឹមសារស្នូលលម្អិត (ងាយយល់ និងមានប្រយោជន៍)]\n"
                f"  ៣. [វគ្គទី ៣៖ សេចក្តីសន្និដ្ឋាន & អំពាវនាវបញ្ចប់]\n\n"
                f"សូមចាប់ផ្តើមស្គ្រីបដោយដាក់ Header ខាងក្រោមនេះនៅបន្ទាត់ទីមួយជានិច្ច៖\n"
                f"{NOTEBOOKLM_KHMER_DIRECTIVE}"
            )
        
    last_error = None
    
    # 1. Modern google.genai
    try:
        client = genai.Client(api_key=api_key)
        for model_id in MODELS_PRIORITY:
            try:
                res = client.models.generate_content(model=model_id, contents=prompt)
                if res and res.text:
                    cleaned_text = res.text.strip()
                    if is_video_overview and "NOTEBOOKLM" not in cleaned_text.upper():
                        cleaned_text = NOTEBOOKLM_EXPLAINER_VIDEO_DIRECTIVE + cleaned_text
                    elif lang == "km" and "NOTEBOOKLM" not in cleaned_text.upper():
                        cleaned_text = NOTEBOOKLM_KHMER_DIRECTIVE + cleaned_text
                    return True, cleaned_text, model_id
            except Exception as err:
                last_error = err
                err_str = str(err)
                if 'API_KEY_INVALID' in err_str or 'API key not valid' in err_str:
                    return False, f"Invalid API Key: {err_str}", None
                # If model not found or quota exhausted on this model, continue to next model
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
                    cleaned_text = res.text.strip()
                    if is_video_overview and "NOTEBOOKLM" not in cleaned_text.upper():
                        cleaned_text = NOTEBOOKLM_EXPLAINER_VIDEO_DIRECTIVE + cleaned_text
                    elif lang == "km" and "NOTEBOOKLM" not in cleaned_text.upper():
                        cleaned_text = NOTEBOOKLM_KHMER_DIRECTIVE + cleaned_text
                    return True, cleaned_text, model_id
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
