"""
Google Veo Native Video Service (Gemini Video Generation)
=========================================================
- Integrates Google DeepMind's flagship Video Generation model (Google Veo).
- Uses official google-genai SDK.
- Handles aspect_ratio="9:16" for Facebook Reels & TikTok vertical video.
- Provides intelligent fallback to internal engine when API key is on Free Tier.
"""

import os
import time
import json
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if os.environ.get("VERCEL"):
    OUTPUT_DIR = Path("/tmp/videos")
else:
    OUTPUT_DIR = BASE_DIR / "static" / "videos"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("veo_service")

VEO_MODELS_PRIORITY = [
    "veo-3.1-generate-preview",
    "veo-2.0-generate-001",
    "models/veo-2.0-generate-001"
]

def generate_veo_prompt_from_script(script_text: str, topic: str = "") -> str:
    """
    បម្លែងស្គ្រីប ឬប្រធានបទទៅជា Prompt បែបភាពយន្ត 9:16 សម្រាប់បញ្ជូនទៅកាន់ Google Veo
    """
    clean_topic = topic or "Cambodian agriculture, green lush organic coconut farm"
    prompt = (
        f"Cinematic 9:16 vertical video for social media Reels. "
        f"Topic: {clean_topic}. "
        f"Vibrant colors, natural sunlight, smooth drone camera movement, 4K high resolution, hyper-realistic."
    )
    return prompt

def generate_video_with_veo(api_key: str, prompt: str, aspect_ratio: str = "9:16", duration_seconds: int = 5):
    """
    ហៅ Google Veo API ដើម្បីបង្កើតវីដេអូ AI MP4
    ត្រឡប់ (True, video_path_or_url, info) ឬ (False, error_msg, None)
    """
    api_key = (api_key or "").strip()
    if not api_key:
        return False, "Gemini API Key មិនអាចទទេបានឡើយ", None

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        
        last_error = None
        for model_name in VEO_MODELS_PRIORITY:
            try:
                logger.info(f"Connecting to Google Veo model: {model_name}...")
                config = types.GenerateVideosConfig(
                    aspect_ratio=aspect_ratio,
                    duration_seconds=duration_seconds,
                    resolution="720p"
                )
                
                # Start video generation operation
                operation = client.models.generate_videos(
                    model=model_name,
                    prompt=prompt,
                    config=config
                )
                
                # Poll operation until done
                max_wait = 120  # 2 minutes timeout
                waited = 0
                while not operation.done and waited < max_wait:
                    time.sleep(10)
                    waited += 10
                    operation = client.operations.get(operation)
                    
                if not operation.done:
                    return False, "Google Veo កំពុងរវល់ (Operation Timeout)។ សូមព្យាយាមម្តងទៀត។", None
                    
                if operation.response and operation.response.generated_videos:
                    gen_video = operation.response.generated_videos[0]
                    timestamp = int(time.time())
                    output_file = OUTPUT_DIR / f"veo_{timestamp}.mp4"
                    
                    # Save video to disk
                    client.files.download(file=gen_video.video)
                    gen_video.video.save(str(output_file))
                    
                    return True, str(output_file), f"បានបង្កើតវីដេអូ Google Veo ជោគជ័យ (Model: {model_name})"
            except Exception as e:
                last_error = e
                err_text = str(e)
                if "RESOURCE_EXHAUSTED" in err_text or "429" in err_text:
                    return False, "គណនី Gemini Free Tier មិនទាន់បើកសិទ្ធិ Google Veo ឡើយ (ត្រូវការ Google Cloud Billing)។", "free_tier_quota"
                continue
                
        return False, f"Google Veo API Status: {str(last_error)}", "model_unavailable"

    except ImportError:
        return False, "មិនទាន់បានដំឡើង google-genai library ឡើយ", None
    except Exception as e:
        return False, f"កំហុសក្នុងការបង្កើតវីដេអូ: {str(e)}", None
