import re
import os
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


SESSION = environ.get('SESSION', 'dreamxbotz_search')   # Session name for the bot
API_ID = int(environ.get('API_ID', '15671595')) # API ID from my.telegram.org
API_HASH = environ.get('API_HASH', 'bb8f36f9c39a24c7f8b2acbc7ea8c60a')  # API Hash from my.telegram.org
BOT_TOKEN = environ.get('BOT_TOKEN', "")    # Bot token from @BotFather


CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://files.catbox.moe/eyuzub.jpg https://files.catbox.moe/gnsert.jpg https://files.catbox.moe/aiqmz9.jpg https://files.catbox.moe/9udnl8.jpg https://files.catbox.moe/u50gq9.jpg https://files.catbox.moe/zpd5jb.jpg https://files.catbox.moe/o7amv3.jpg https://files.catbox.moe/gcrw97.jpg https://files.catbox.moe/3a94m9.jpg')).split()  # Sample pic
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://graph.org/file/56b5deb73f3b132e2bb73.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/242b7f1b52743938d81f1.jpg'))
FSUB_IMG = (environ.get('FSUB_IMG', 'https://files.catbox.moe/gnsert.jpg')).split()  # Fsub pic

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7253187871 6566268406').split()] # Replace with the actual admin ID(s) to add
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002447436146 -1002515386092 -1002082701021 -1001603505179 -1002578416876 -1002273978945').split()] 
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002210651858'))  # Log channel id (make sure bot is admin)
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002210651858'))  # Bin channel id (make sure bot is admin)
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002312299520'))  
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002238159500'))  # Premium logs channel id
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-100').split()] #(make sure bot is admin)
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001629003283')  # Support group id (make sure bot is admin)
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002170171844')  # Request channel id (make sure bot is admin)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/hari_moviez')  # Support group link (make sure bot is admin)
UPDATE_CHANNEL_LNK = environ.get('UPDATE_CHANNEL_LNK', 'https://t.me/hari_moviez')

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://anikush8310_db_user:pWxFAyxQ3UTlsR1X@cluster0.cmkbiq2.mongodb.net/?appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'SilentXBotz_files')

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "True"), True) # Type True For Turn On MULTIPLE DB FUNTION 
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://anikush8310_db_user:mIE1xcFcYComgN04@cluster0.32kt1j6.mongodb.net/?appName=Cluster0")
DB_CHANGE_LIMIT = int(environ.get('DB_CHANGE_LIMIT', "432")) 

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+nOdVKAzF-mQyYTU1') # Group link for the bot
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/harikushal') # Owner link for the bot
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/+jgLqztoklls5MjRl') # Update channel link for the bot

AUTH_CHANNEL = environ.get("AUTH_CHANNEL", "-1002283516790") # add multiple channels here, separated by single space
AUTH_REQ_CHANNEL = environ.get('AUTH_REQ_CHANNEL', '-1002283516790')

IS_VERIFY = is_enabled('IS_VERIFY', True)  # Verification On (True) / Off (False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002238159500')) #Verification Channel Id 
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002238159500')) #If Anyone Set Your Bot In Any Group And Set Shortner In That Group Then In This Channel The All Details Come
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/Brand_moviess/6")   # Tutorial link for verification
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/Brand_moviess/6")   # Second tutorial link for verification
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/Brand_moviess/6")   # Third tutorial link for verification

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "45b6928d65d1c1dfc2d52d052d879b9b02dd7fe3") # Shortener API key
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "arolinks.com") # Shortener website

SHORTENER_API2 = environ.get("SHORTENER_API2", "45b6928d65d1c1dfc2d52d052d879b9b02dd7fe3")  # Shortener API key for second website
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "arolinks.com") # Shortener website for second website

SHORTENER_API3 = environ.get("SHORTENER_API3", "45b6928d65d1c1dfc2d52d052d879b9b02dd7fe3")  
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "arolinks.com") # Shortener website for third website

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200")) # Time gap for two-step verification in seconds (default: 20 minutes)
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))    

MOVIE_UPDATE_NOTIFICATION = bool(environ.get("MOVIE_UPDATE_NOTIFICATION", True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8089")
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/hari_moviez') 
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "300"))  
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "True")), True)
IS_LANDSCAPE_POSTER = is_enabled((environ.get('IS_LANDSCAPE_POSTER', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PM_SEARCH = bool(environ.get('PM_SEARCH', True)) 
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False)) 
PAID_STREAM = bool(environ.get('PAID_STREAM', True)) 
STREAM_MODE = bool(environ.get('STREAM_MODE', True))
MAINTENANCE_MODE = bool(environ.get('MAINTENANCE_MODE', False)) 

IGNORE_WORDS = (list(os.environ.get("IGNORE_WORDS").split(",")) if os.environ.get("IGNORE_WORDS") else []) #Remove Words While Searching Files
IGNORE_WORDS= ["movies", "Movies", ",", "episode", "Episode", "episodes", "Episodes", "south indian", "south indian movie", "South Indian Movie", "south movie", "South Movie", "South Indian", "web-series", "hindi me bhejo", "gujrati", "combined", "!", "kro", "jaldi", "Audio", "audio", "movi", "language", "Language", "Hollywood", "All", "all", "bollywood", "Bollywood", "South", "south", "HD", "hd", "karo", "Karo", "fullepisode", "please", "plz", "Please", "Plz", "send", "link", "Link", "full", "Full", "dabbed", "dubbed", "season", "Season", "web", "series", "Web", "Series", "webseries", "WebSeries", "upload", "HD", "Hd", "bhejo", "ful", "Send", "Bhejo"]

BAD_WORDS = ["Hdhub4u", "cinevood", "skymoviedHD"] #Remove Words From File_Name

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
SEASONS = ["Season 1", "Season 2", "Season 3", "Season 4", "Season 5", "Season 6", "Season 7", "Season 8", "Season 9", "Season 10"]


NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'SilentXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'SilentX'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)


REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

STAR_PREMIUM_PLANS = {
    1: "7day",
    30: "15day",    
    60: "1month", 
    120: "2month",   
}

Bot_cmds = {
    "start": "ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
    "trendlist": "ɢᴇᴛ ᴛᴏᴘ ꜱᴇᴀʀᴄʜ ʟɪꜱᴛ",
    "myplan" : "ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ",
    "plan" :"ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴘʀɪᴄᴇ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "group_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "admin_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "details": "ꜱᴇᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ",
    "reset_group": "ʀᴇꜱᴇᴛ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ", 
    "stats": "ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ.",
    "delete": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ."
}

#Don't Change Anything Here

if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2

AUTH_CHANNEL = [int(ch) for ch in AUTH_CHANNEL.strip().split()] if AUTH_CHANNEL else []
AUTH_REQ_CHANNEL = [int(ch) for ch in AUTH_REQ_CHANNEL.strip().split()] if AUTH_REQ_CHANNEL else []
