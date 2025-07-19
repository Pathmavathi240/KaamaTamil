from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped
import yt_dlp
import os

# Load global app and call if not already done in __main__.py
from DeadlineTech.__main__ import app, call

@Client.on_message(filters.command("vplay"))
async def vplay_command(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❗ Usage: /vplay <song name or YouTube URL>")

    query = message.text.split(None, 1)[1]
    await message.reply_text(f"🔍 Searching for `{query}`...")

    try:
        ydl_opts = {
            "format": "bestaudio",
            "noplaylist": True,
            "quiet": True,
            "extract_flat": False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            audio_url = info['url']
            title = info.get("title")

        await message.reply_text(f"▶️ Streaming: **{title}**")

        await call.join_group_call(
            message.chat.id,
            AudioPiped(audio_url)
        )

    except Exception as e:
        await message.reply_text(f"❌ Error: `{str(e)}`")
