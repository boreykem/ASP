"""
Automated Video Engine for Khmer Social Media (Reels & TikTok)
============================================================
Features:
- Natural Khmer Neural Voiceover (Piseth / Sreymom via Edge-TTS)
- 3-Second Visual Hook Rule: B-Roll video/image montage
- Hardware-accelerated / Static FFmpeg via imageio-ffmpeg
- Dynamic serverless /tmp & local static path resolution
"""

import os
import re
import sys
import json
import time
import asyncio
import subprocess
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
B_ROLL_DIR = BASE_DIR / "assets" / "b_roll"

if os.environ.get("VERCEL"):
    OUTPUT_DIR = Path("/tmp/videos")
else:
    OUTPUT_DIR = BASE_DIR / "static" / "videos"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_MALE_VOICE = "km-KH-PisethNeural"
DEFAULT_FEMALE_VOICE = "km-KH-SreymomNeural"

def get_ffmpeg_binary():
    """
    ស្វែងរក FFmpeg binary ដែលអាចដំណើរការបានទាំងលើ Local PC និង Serverless Cloud (Vercel)
    """
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"

def clean_script_for_tts(text: str) -> str:
    """
    សម្អាតអត្ថបទមុននឹងបញ្ជូនទៅកាន់ TTS:
    - ដក Emojis
    - ដក Markdown Formatting (*, #, _, -)
    - ដកពាក្យស្លាកសញ្ញាដូចជា [Hook], [CTA], [Scene 1]
    """
    if not text:
        return ""
    cleaned = re.sub(r"\[.*?\]|\(.*?\)", " ", text)
    cleaned = re.sub(r"[#*_~`>-]", " ", cleaned)
    cleaned = re.sub(r"https?://\S+", " ", cleaned)
    cleaned = re.sub(r"#\w+", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned

async def generate_speech_async(text: str, voice: str = DEFAULT_MALE_VOICE, rate: str = "+10%", output_audio: str = "voice.mp3", output_sub: str = "sub.srt"):
    """
    បង្កើតសំឡេងអានជាភាសាខ្មែរតាម Edge-TTS
    """
    import edge_tts
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    submaker = edge_tts.SubMaker()
    
    with open(output_audio, "wb") as f_audio:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f_audio.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
                
    try:
        with open(output_sub, "w", encoding="utf-8") as f_sub:
            f_sub.write(submaker.get_srt())
    except Exception:
        pass
        
    return output_audio, output_sub

def generate_voiceover(text: str, voice: str = DEFAULT_MALE_VOICE, rate: str = "+10%", output_prefix: str = "temp_voice"):
    """
    Synchronous wrapper សម្រាប់បង្កើតសំឡេង
    """
    cleaned = clean_script_for_tts(text)
    if not cleaned:
        raise ValueError("Script is empty after cleaning")
        
    out_audio = str(OUTPUT_DIR / f"{output_prefix}.mp3")
    out_sub = str(OUTPUT_DIR / f"{output_prefix}.srt")
    
    asyncio.run(generate_speech_async(cleaned, voice=voice, rate=rate, output_audio=out_audio, output_sub=out_sub))
    return out_audio, out_sub

def get_media_duration(file_path: str) -> float:
    """
    វាស់ប្រវែង Audio ជាវិនាទីតាម FFmpeg (មិនពឹងលើ ffprobe ឡើយ)
    """
    ff_bin = get_ffmpeg_binary()
    cmd = [ff_bin, "-i", str(file_path)]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", res.stderr)
    if match:
        h, m, s = match.groups()
        return int(h) * 3600 + int(m) * 60 + float(s)
    return 10.0

def detect_b_roll_topic(script_text: str = "", topic: str = "") -> str:
    """
    វិភាគស្វែងរក Topic ឱ្យត្រូវនឹង Folder B-Roll ដោយស្វ័យប្រវត្តិ:
    - sanitation: បូមលូ, បង្គន់ស្ទះ, លាងសម្អាត, អនាម័យ, លូស្អុយ, បូមកាកសំណល់
    - coconut: ដូង, កសិកម្ម, ចម្ការដូង, ដំណាំ, ផ្លែដូង
    - general: ទូទៅ, បច្ចេកវិទ្យា, អប់រំ, អាជីវកម្ម, ផ្សេងៗ
    """
    combined = f"{topic} {script_text}".lower()
    
    sanitation_keywords = [
        "លូ", "បង្គន់", "បូម", "ស្ទះ", "លាងសម្អាត", "កាកសំណល់", "អនាម័យ",
        "sewer", "sanitation", "toilet", "pump", "plumbing", "drain", "pipe", "cleaning"
    ]
    if any(k in combined for k in sanitation_keywords):
        return "sanitation"
        
    coconut_keywords = [
        "ដូង", "កសិកម្ម", "ចម្ការ", "ដំណាំ", "ផ្លែឈើ", "កសិករ",
        "coconut", "farm", "agriculture", "harvest", "plantation", "tree"
    ]
    if any(k in combined for k in coconut_keywords):
        return "coconut"
        
    return "general"

def create_reels_video(
    script_text: str,
    voice: str = DEFAULT_MALE_VOICE,
    speed: str = "+10%",
    topic: str = "",
    b_roll_folder: str = None,
    output_filename: str = None
) -> str:
    """
    ផលិតវីដេអូបញ្ឈរ 9:16 (1080x1920) ពេញលេញដោយស្វ័យប្រវត្តិតាមប្រធានបទ
    """
    timestamp = int(time.time())
    if not output_filename:
        output_filename = f"reels_{timestamp}.mp4"
        
    out_video_path = str(OUTPUT_DIR / output_filename)
    voice_prefix = f"voice_{timestamp}"
    
    # ស្វែងរក B-Roll folder ឆ្លាតវៃតាម Topic & Script
    if not b_roll_folder or b_roll_folder in ["auto", "coconut"]:
        detected = detect_b_roll_topic(script_text, topic)
        if not b_roll_folder or b_roll_folder == "auto" or detected != "coconut":
            b_roll_folder = detected
    if not b_roll_folder:
        b_roll_folder = "general"
        
    print(f"[*] ប្រធានបទ: '{topic or 'Auto'}' ➔ ជ្រើសរើស B-Roll Folder: '{b_roll_folder}'")
    
    # ជំហានទី ១: បង្កើត Voiceover
    print(f"[*] កំពុងបង្កើតសំឡេងអានខ្មែរ Neural Voice ({voice})...")
    audio_path, sub_path = generate_voiceover(script_text, voice=voice, rate=speed, output_prefix=voice_prefix)
    
    duration = get_media_duration(audio_path)
    print(f"[+] សំឡេងអានផលិតជោគជ័យ! ប្រវែងសរុប: {duration:.2f} វិនាទី")
    
    # ជំហានទី ២: ស្វែងរក B-Roll Assets
    target_b_roll = B_ROLL_DIR / b_roll_folder
    images = []
    if target_b_roll.exists():
        images = list(target_b_roll.glob("*.jpg")) + list(target_b_roll.glob("*.png"))
        
    if not images:
        fallback_general = B_ROLL_DIR / "general"
        if fallback_general.exists():
            images = list(fallback_general.glob("*.jpg")) + list(fallback_general.glob("*.png"))
            
    if not images:
        images = list(B_ROLL_DIR.glob("**/*.jpg")) + list(B_ROLL_DIR.glob("**/*.png"))
        
    if not images:
        raise FileNotFoundError(f"រកមិនឃើញរូបភាព B-Roll នៅក្នុង {B_ROLL_DIR} ឡើយ")
        
    images.sort()
    num_images = len(images)
    time_per_image = max(3.0, duration / num_images)
    
    # ជំហានទី ៣: បង្កើត Video Montage តាម FFmpeg
    concat_list_file = OUTPUT_DIR / f"concat_{timestamp}.txt"
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for img in images:
            img_path = str(img.resolve()).replace("\\", "/")
            f.write(f"file '{img_path}'\n")
            f.write(f"duration {time_per_image:.2f}\n")
        last_img_path = str(images[-1].resolve()).replace("\\", "/")
        f.write(f"file '{last_img_path}'\n")
        
    ff_bin = get_ffmpeg_binary()
    print(f"[*] កំពុង Render វីដេអូកម្រិត 1080x1920 (9:16 Vertical HD) តាម {ff_bin}...")
    
    ffmpeg_cmd = [
        ff_bin, "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_list_file),
        "-i", audio_path,
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,format=yuv420p",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "24",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        out_video_path
    ]
    
    subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    
    try:
        concat_list_file.unlink(missing_ok=True)
    except Exception:
        pass
        
    print(f"[SUCCESS] វីដេអូ Reels ផលិតជោគជ័យ: {out_video_path}")
    return out_video_path
