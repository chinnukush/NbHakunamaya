import re
import io
import aiohttp
import hashlib
from info import *
from utils import *
from utils import clean_filename
from logging_helper import LOGGER
from typing import Dict
from datetime import datetime
from pyrogram import Client, filters
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode

CAPTION_LANGUAGES = [
    "Bhojpuri", "Hindi", "Bengali", "Tamil", "English", "Bangla", "Telugu",
    "Malayalam", "Kannada", "Marathi", "Punjabi", "Bengoli", "Gujrati",
    "Korean", "Gujarati", "Spanish", "French", "German", "Chinese", "Arabic",
    "Portuguese", "Russian", "Japanese", "Odia", "Assamese", "Urdu"
]

DEFAULT_IMAGE_URL = "https://te.legra.ph/file/88d845b4f8a024a71465d.jpg"

# Caption template with deep links for each quality
SILENTX_PREMIUM_UPDATE = """
🎬 Title : {}
📆 Year : {}
🔊 Audio : {}
💿 Quality : {}

🔗 <a href='https://telegram.me/{}/?start=getfile-{}-480p'>480p File ({})</a>
🔗 <a href='https://telegram.me/{}/?start=getfile-{}-720p'>720p File ({})</a>
🔗 <a href='https://telegram.me/{}/?start=getfile-{}-1080p'>1080p File ({})</a>

〽️ Powered By @{}
"""

notified_movies = set()
media_filter = filters.document | filters.video | filters.audio

@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return
    media.file_type = file_type
    media.caption = message.caption
    success, silentxbotz = await save_file(media)
    try:  
        if success and silentxbotz == 1 and await get_status(bot.me.id):            
            await send_movie_update(bot, file_name=media.file_name, caption=media.caption, size=media.file_size)
    except Exception as e:
        LOGGER.error(f"Error In Movie Update - {e}")
        pass

async def send_movie_update(bot, file_name, caption, size):
    try:
        file_name = clean_filename(file_name)
        caption = clean_filename(caption)
        year_match = re.search(r"\b(19|20)\d{2}\b", caption)
        year = year_match.group(0) if year_match else None      
        quality = await get_qualities(caption) or "HDRip"
        language = await get_languages(caption) or "Multi-Audio"      
        if file_name in notified_movies:
            return 
        notified_movies.add(file_name)      
        tmdb_data = await fetch_tmdb_data(file_name, year)
        if not tmdb_data:
            return 

        title = escape_html(tmdb_data["title"])
        release_year = escape_html(tmdb_data["release_date"] or "TBA")

        # Split file size for demo purposes (you can map actual files later)
        size_480 = format_size(size // 4)
        size_720 = format_size(size // 2)
        size_1080 = format_size(size)

        search_movie = file_name.replace(" ", "-")

        full_caption = SILENTX_PREMIUM_UPDATE.format(
            title,
            release_year,
            escape_html(language),
            "1080p, 720p, 480p",
            temp.U_NAME, search_movie, size_480,
            temp.U_NAME, search_movie, size_720,
            temp.U_NAME, search_movie, size_1080,
            temp.U_NAME
        )        
        await send_with_visual(bot, full_caption, tmdb_data)        
    except Exception as e:
        LOGGER.error(f"Error In Movie Update: {e}")

def escape_html(text: str) -> str:
    if not text:
        return ""
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def format_size(size_bytes: int) -> str:
    if size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.2f}KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes/(1024*1024):.2f}MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.2f}GB"

def get_trailer_button(tmdb_data: Dict) -> list:
    videos = tmdb_data.get("videos", [])
    yt_videos = [v for v in videos if "youtube" in v.get("url", "").lower()]    
    if yt_videos:
        return [InlineKeyboardButton("▶️ Watch Trailer", url=yt_videos[0]["url"])]
    return []

async def send_with_visual(bot, caption: str, tmdb_data: Dict):
    try:
        visual_url = await get_best_visual(tmdb_data)
        trailer_btn = get_trailer_button(tmdb_data)
        keyboard = InlineKeyboardMarkup([trailer_btn]) if trailer_btn else None
        
        if visual_url:
            async with aiohttp.ClientSession() as session:
                async with session.get(visual_url, timeout=aiohttp.ClientTimeout(total=20)) as img_resp:
                    if img_resp.status == 200:
                        img_bytes = await img_resp.read()
                        photo_file = io.BytesIO(img_bytes)
                        photo_file.name = await generate_premium_filename(tmdb_data["title"])
                        
                        await bot.send_photo(
                            chat_id=MOVIE_UPDATE_CHANNEL, 
                            photo=photo_file, 
                            caption=caption,
                            parse_mode=ParseMode.HTML,
                            reply_markup=keyboard
                        )
                        return       
        await bot.send_photo(
            chat_id=MOVIE_UPDATE_CHANNEL,
            photo=DEFAULT_IMAGE_URL,
            caption=caption,
            parse_mode=ParseMode.HTML,
            reply_markup=keyboard
        )       
    except Exception as e:
        LOGGER.error(f"Visual Send Error: {e}")

async def generate_premium_filename(title: str, extension=".jpg") -> str:
    clean_title = re.sub(r'[^\w\s-]', '', title)[:20].strip()
    timestamp = datetime.now().strftime("%y%m%d%H%M")
    unique_id = hashlib.md5(title.encode()).hexdigest()[:6]
    return f"silentx_{clean_title}_{timestamp}_{unique_id}{extension}"

async def get_languages(text: str) -> str:
    found_langs = [lang for lang in CAPTION_LANGUAGES if lang.lower().replace(" ", "") in text.lower().replace(" ", "")]
    return ", ".join(found_langs[:2]) if found_langs else "Multi-Audio"

async def get_qualities(text): 
    qualities = ["ORG", "hdcam", "HDCAM", "HQ", "HDRip", "camrip", "WEB-DL", "CAMRip", "hdtc", "predvd", "DVDscr", "dvdscr", "dvdrip", "HDTC", "dvdscreen", "HDTS", "hdts"]
    return ", ".join([q for q in qualities if q.lower() in text.lower()])

async def get_pixels(caption):
    pixels = ["480p", "480p HEVC", "720p", "720p HEVC", "1080p", "1080p HEVC", "2160p", "2K", "4K"]
    return ", ".join([p for p in pixels if p.lower() in caption.lower()])
    
