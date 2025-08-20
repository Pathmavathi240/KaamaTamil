import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27650408"))
API_HASH = getenv("API_HASH", "5d43e4fce232efc21ed618ed7a147952")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8240171801:AAEcf8VMwRiXl89GzSIJwWfVdH_u3FnxOWY")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicOnes_bot")

#Get API_KEY from @DeadlineTechOwner or @DeadlineApiBot
API_BASE_URL = getenv("API_BASE_URL")
API_KEY = getenv("API_KEY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://pathmavathi975146:EZVLU6tKs3epjdnC@cluster0.m9hpxsr.mongodb.net/Musicdead?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 720))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002953476466"))

# Get this value from @Harry_RoxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7884994139"))

START_STICKER_ID = getenv("START_STICKER_ID", "CAACAgUAAxkBAAEBSyhoifhDg1JaKOD6HlSYl9J2WsM-ZQACFBAAAuVwyVYoc0EWkxXRAAEeBA")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DeadlineTech/music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+5iPB9XLKXRgwOTE1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+5iPB9XLKXRgwOTE1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 524288000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2147483648))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGl6WgAD6gtQotBlSHms42ZZjyNGgK5vJlY-s2yKXq4ZkHQmyfH7kqHaq1Oo3CbwpbOUe0LjkCCWdT11kyX8-6rlr2JDRx1gp1hZTypBE3VLXlViNrnijBMEAo_qJaiP6Dx1CSuRj_42NJUMSXvVXuy_BjuD64RyNPjcNUDtTF5KMV5Yb0sEZafx1aVl8lGNRgJBHn-b0I-1YD0A5Di3P4A1Y0fmET343kKZvP8OzvEhYXcrQywdSWuDbR9Ommxbw_FmvzJkFv__S-egpjkfjJSgC0d02bSeRDo59QRds9KVvRij5lFiRiJvq27Vz6pfXJwhBowyHJIJKW5LHB7slgRAQgTXQAAAAHV-3ZbAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/ls327t.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/mp8n9a.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/mp8n9a.jpg"
STATS_IMG_URL = "https://files.catbox.moe/s13wqb.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/mp8n9a.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/mp8n9a.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/mp8n9a.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/mp8n9a.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/mp8n9a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/mp8n9a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/mp8n9a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/mp8n9a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
