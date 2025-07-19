import yt_dlp
import requests

def get_thumbnail(query):
    try:
        ydl_opts = {
            "format": "bestaudio",
            "noplaylist": True,
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            thumb_url = info.get("thumbnail")
            title = info.get("title")
            return thumb_url, title
    except Exception as e:
        return None, None
