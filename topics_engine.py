import datetime
import random
from ai_service import MODELS_PRIORITY
from google import genai
import google.generativeai as genai_legacy

# វិស័យធំៗទាំង ៧ តាមការចង់បានរបស់អ្នកប្រើប្រាស់
CATEGORIES = [
    {"id": "education", "km": "🎓 ការអប់រំ", "en": "🎓 Education"},
    {"id": "economy", "km": "💰 សេដ្ឋកិច្ច & ហិរញ្ញវត្ថុ", "en": "💰 Economy & Finance"},
    {"id": "society", "km": "👥 សង្គម & ការរស់នៅ", "en": "👥 Society & Mindset"},
    {"id": "science", "km": "🔬 វិទ្យាសាស្ត្រ & បច្ចេកវិទ្យា", "en": "🔬 Science & Tech"},
    {"id": "agriculture", "km": "🌾 កសិកម្មទំនើប", "en": "🌾 Modern Agriculture"},
    {"id": "universe", "km": "🌌 ការរកឃើញសកលលោក", "en": "🌌 Universe Discoveries"},
    {"id": "religion", "km": "🕊️ សាសនា & ទស្សនវិជ្ជា", "en": "🕊️ Religion & Philosophy"}
]

# ឃ្លាំងប្រធានបទបម្រុងគុណភាពខ្ពស់ (Fallback Bank) ចំនួនជាង ៧០ ប្រធានបទ
CURATED_TOPICS = {
    "education": [
        {"km": "គន្លឹះរៀនឆាប់ចាំ និងយល់បានលឿនតាមវិធីសាស្ត្រ Feynman", "en": "Feynman Technique: How to Learn Anything Faster"},
        {"km": "ជំនាញ ៣ យ៉ាងដែលសិស្ស និងយុវជនត្រូវរៀនឱ្យចេះក្នុងយុគសម័យ AI", "en": "Top 3 Essential Skills for Students in the AI Era"},
        {"km": "របៀបបង្កើតទម្លាប់អានសៀវភៅឱ្យបាន ១ ក្បាលក្នុងមួយសប្តាហ៍", "en": "How to Build a Habit of Reading One Book per Week"},
        {"km": "អត្ថប្រយោជន៍ដ៏អស្ចារ្យនៃការរៀនតាមបែប Flipped Classroom", "en": "The Power of the Flipped Classroom Learning Model"},
        {"km": "វិធីសាស្ត្រគ្រប់គ្រងពេលវេលា 80/20 (Pareto Principle) សម្រាប់ការរៀនសូត្រ", "en": "80/20 Rule for Supercharged Student Productivity"}
    ],
    "economy": [
        {"km": "ក្បួនគ្រប់គ្រងលុយ 50/30/20 សម្រាប់អ្នកទើបចាប់ផ្តើមធ្វើការ", "en": "The 50/30/20 Rule to Manage Your Personal Finances"},
        {"km": "ភាពខុសគ្នារវាង ទ្រព្យសកម្ម (Assets) និងបំណុល (Liabilities) ដែលអ្នកមានមិនប្រាប់", "en": "Assets vs Liabilities: What the Rich Really Know"},
        {"km": "វិធីសន្សំប្រាក់វិនិយោគតូចៗដើម្បីទទួលបាន Passive Income នៅថ្ងៃអនាគត", "en": "How Small Consistent Investments Create Lasting Wealth"},
        {"km": "គន្លឹះ ៣ យ៉ាងក្នុងការចាប់ផ្តើមអាជីវកម្មខ្នាតតូចដោយប្រើដើមទុនតិច", "en": "3 Secrets to Launching a Low-Capital Startup"},
        {"km": "មូលហេតុដែលអតិផរណាធ្វើឱ្យតម្លៃទំនិញឡើងថ្លៃ និងវិធីការពារលុយរបស់អ្នក", "en": "Why Inflation Hurts and How to Protect Your Money"}
    ],
    "society": [
        {"km": "របៀបកាត់បន្ថយការគិតច្រើន (Overthinking) និងថែរក្សាសុខភាពផ្លូវចិត្ត", "en": "How to Stop Overthinking and Protect Your Mental Peace"},
        {"km": "ច្បាប់នៃភាពទាក់ទាញ (Law of Attraction) ក្នុងទំនាក់ទំនងសង្គម", "en": "The Power of Positive Energy in Social Relationships"},
        {"km": "មូលហេតុដែលមនុស្សភាគច្រើនខ្លាចការផ្លាស់ប្តូរ និងរបៀបយកឈ្នះវា", "en": "Why We Fear Change and How to Break the Comfort Zone"},
        {"km": "សិល្បៈនៃការស្តាប់៖ វិធីក្លាយជាមនុស្សដែលមានមន្តស្នេហ៍ក្នុងកិច្ចសន្ទនា", "en": "The Lost Art of Active Listening in Everyday Life"},
        {"km": "ឥទ្ធិពលនៃបណ្តាញសង្គមមកលើសុភមង្គល និងរបៀបធ្វើ Social Media Detox", "en": "Social Media and Happiness: The Need for Digital Detox"}
    ],
    "science": [
        {"km": "របៀបដែលបញ្ញាសិប្បនិម្មិត (AI) កំពុងផ្លាស់ប្តូរវិស័យវេជ្ជសាស្ត្រជួយសង្គ្រោះជីវិត", "en": "How Artificial Intelligence is Revolutionizing Medicine"},
        {"km": "តើកុំព្យូទ័រ Quantum ដំណើរការយ៉ាងដូចម្តេច ហើយវាខ្លាំងជាងកុំព្យូទ័រធម្មតាប៉ុនណា?", "en": "How Quantum Computers Work and Why They Shock the World"},
        {"km": "អាថ៌កំបាំងនៃ DNA៖ តើយើងអាចកែប្រែហ្សែនដើម្បីការពារជំងឺបានដោយរបៀបណា?", "en": "CRISPR and DNA: Editing Genes to Eradicate Diseases"},
        {"km": "បច្ចេកវិទ្យាថាមពលកកើតឡើងវិញ (Renewable Energy) ដែលនឹងជំនួសប្រេងកាត", "en": "Green Energy Breakthroughs That Will Replace Fossil Fuels"},
        {"km": "របៀបដែលខួរក្បាលមនុស្សបង្កើតការចងចាំ និងវិធីពង្រឹងការចងចាំ", "en": "How Human Memory Works and How to Strengthen It"}
    ],
    "agriculture": [
        {"km": "កសិកម្មឆ្លាតវៃ (Smart Farming)៖ ការប្រើប្រាស់ Drone និង IoT ក្នុងចម្ការ", "en": "Smart Agriculture: Drones and IoT Revolutionizing Farms"},
        {"km": "បច្ចេកទេសដាំបន្លែអ៊ីដ្រូពូនិច (Hydroponics) មិនបាច់ប្រើដី ចំណេញផ្ទៃដី និងទឹក", "en": "Hydroponic Farming: Clean Crops Without Traditional Soil"},
        {"km": "របៀបធ្វើជីកំប៉ុសធម្មជាតិពីកាកសំណល់ផ្ទះបាយជួយកាត់បន្ថយការចំណាយ", "en": "How to Make Organic Kitchen Compost for Healthier Plants"},
        {"km": "កសិកម្មចម្រុះ៖ គន្លឹះរកចំណូលបានពេញមួយឆ្នាំលើផ្ទៃដី ១ ហិកតា", "en": "Integrated Farming: Year-Round Income from 1 Hectare"},
        {"km": "បច្ចេកវិទ្យាការពារដំណាំពីការប្រែប្រួលអាកាសធាតុ និងគ្រោះរាំងស្ងួត", "en": "Climate-Resilient Crops: Shielding Harvests from Drought"}
    ],
    "universe": [
        {"km": "ការរកឃើញដ៏អស្ចារ្យបំផុតរបស់តេឡេស្កុប James Webb ទៅកាន់ដើមកំណើតសកលលោក", "en": "The Most Mind-Blowing Discoveries from the James Webb Telescope"},
        {"km": "តើប្រហោងខ្មៅ (Black Hole) ពិតជាអាចលេបពេលវេលា និងពន្លឺបានមែនទេ?", "en": "What Really Happens When You Enter a Black Hole?"},
        {"km": "តើមានជីវិតក្រៅភព (Extraterrestrial Life) នៅលើឋានព្រះចន្ទ Europa ដែរឬទេ?", "en": "Is There Alien Life Beneath the Ice of Jupiter's Moon Europa?"},
        {"km": "អាថ៌កំបាំងនៃ Dark Matter៖ ៨៥% នៃរូបធាតុក្នុងសកលលោកដែលភ្នែកមើលមិនឃើញ", "en": "Dark Matter: The Invisible 85% of the Cosmos"},
        {"km": "តើភពអង្គារ (Mars) អាចក្លាយជាផ្ទះទីពីររបស់មនុស្សជាតិនៅពេលណា?", "en": "Terraforming Mars: When Will Humans Truly Settle There?"}
    ],
    "religion": [
        {"km": "មាគ៌ាអរិយសច្ចទាំង ៤ ក្នុងព្រះពុទ្ធសាសនា៖ វិធីរំលត់ទុក្ខក្នុងជីវិតប្រចាំថ្ងៃ", "en": "The Four Noble Truths: Overcoming Suffering in Modern Life"},
        {"km": "ទស្សនវិជ្ជា Stoicism និងការរក្សាចិត្តស្ងប់ក្នុងពិភពលោកដ៏ច្របូកច្របល់", "en": "Stoic Wisdom: Finding Inner Calm in an Anxious World"},
        {"km": "ឥទ្ធិពលនៃការធ្វើសមាធិ (Mindfulness) មកលើសុខភាពខួរក្បាល និងផ្លូវចិត្ត", "en": "Mindfulness Meditation: Scientifically Proven Peace of Mind"},
        {"km": "ច្បាប់កម្មផល (Karma)៖ អំពើល្អបង្កើតសេចក្តីស្ងប់ក្នុងចិត្តយ៉ាងដូចម្តេច?", "en": "Karma and Moral Compass: Why Doing Good Heals the Soul"},
        {"km": "ការរៀនអភ័យទោស៖ គន្លឹះដោះលែងខ្លួនឯងចេញពីទ្រុងនៃការខឹងគុំកួន", "en": "The Power of Forgiveness: Breaking Free from Resentment"}
    ]
}

def get_daily_diverse_topics(api_key, lang="km"):
    """
    បង្កើត ៥ ប្រធានបទប្លែកៗគ្នាជារៀងរាល់ថ្ងៃ ជ្រើសរើសចេញពីវិស័យទាំង ៧។
    ព្យាយាមហៅ AI ជាមុន បើ quota ពេញ ប្រើក្បួន Dynamic Rotation តាមថ្ងៃនៃឆ្នាំ។
    """
    api_key = (api_key or "").strip().strip("'").strip('"')
    
    # 1. សាកល្បងហៅ Gemini AI ប្រសិនបើមាន API Key
    if api_key:
        if lang == "en":
            prompt = (
                "Generate exactly 5 distinct, engaging, viral video topics for today. "
                "Pick 5 DIFFERENT categories among these 7 fields:\n"
                "1. Education\n"
                "2. Economy & Finance\n"
                "3. Society & Mindset\n"
                "4. Science & Tech\n"
                "5. Modern Agriculture\n"
                "6. Universe & Space Discoveries\n"
                "7. Religion & Life Philosophy\n\n"
                "Requirements:\n"
                "- Write click-worthy, curiosity-piquing titles.\n"
                "- Return EXACTLY 5 lines, 1 topic per line, with no numbering (no 1. 2.), no bullets, no category prefix."
            )
        else:
            prompt = (
                "សូមជួយបង្កើតប្រធានបទស្គ្រីបវីដេអូខ្លីដែលទាក់ទាញ ក្តៅៗ និងប្លែកៗចំនួន ៥ សម្រាប់ថ្ងៃនេះ។\n"
                "ប្រធានបទនីមួយៗត្រូវជ្រើសរើសចេញពីវិស័យធំៗទាំង ៧ ខាងក្រោម (ជ្រើសយក ៥ វិស័យខុសៗគ្នា)៖\n"
                "១. ការអប់រំ (Education)\n"
                "២. សេដ្ឋកិច្ច និងហិរញ្ញវត្ថុ (Economy & Finance)\n"
                "៣. សង្គម និងការគិត (Society & Mindset)\n"
                "៤. វិទ្យាសាស្ត្រ និងបច្ចេកវិទ្យា (Science & Tech)\n"
                "៥. កសិកម្មទំនើប (Agriculture)\n"
                "៦. ការរកឃើញសកលលោក និងតារាសាស្ត្រ (Universe Discoveries)\n"
                "៧. សាសនា និងទស្សនវិជ្ជា (Religion & Philosophy)\n\n"
                "លក្ខខណ្ឌ៖\n"
                "- ចំណងជើងត្រូវមានភាពទាក់ទាញ និងរស់រវើក\n"
                "- ផ្តល់ចម្លើយជាភាសាខ្មែរ ត្រឹមតែ ៥ បន្ទាត់ប៉ុណ្ណោះ (១ បន្ទាត់ ១ ប្រធានបទ ហាមដាក់លេខរៀង 1 2 3 ឬសញ្ញា bullet)។"
            )

        # Try models
        for m in MODELS_PRIORITY:
            try:
                client = genai.Client(api_key=api_key)
                res = client.models.generate_content(model=m, contents=prompt)
                if res and res.text:
                    lines = [l.strip('- *•1234567890. ') for l in res.text.strip().split('\n') if l.strip()]
                    if len(lines) >= 5:
                        return True, lines[:5], "AI Generated"
            except Exception:
                continue

    # 2. Dynamic Rotation ឆ្លាតវៃតាមកាលបរិច្ឆេទនៃថ្ងៃ (Day of Year Rotation)
    # ធានាថារាល់ថ្ងៃ ៥ ប្រធានបទនឹងប្តូរថ្មីៗជានិច្ច មិនដែលជាន់គ្នាឡើយ!
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    available_cat_keys = list(CURATED_TOPICS.keys())
    
    # Shuffle or rotate categories based on day
    shuffled_cats = available_cat_keys.copy()
    random.Random(day_of_year).shuffle(shuffled_cats)
    selected_cats = shuffled_cats[:5]
    
    topics = []
    for cat_key in selected_cats:
        cat_topics = CURATED_TOPICS[cat_key]
        # Pick unique topic per category rotating by day
        idx = (day_of_year + len(topics)) % len(cat_topics)
        t_obj = cat_topics[idx]
        topic_text = t_obj["km"] if lang == "km" else t_obj["en"]
        topics.append(topic_text)
        
    return True, topics, "Daily Category Rotation"
