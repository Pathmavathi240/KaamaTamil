from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped
import yt_dlp

app = Client("music_bot")
call = PyTgCalls(app)

@Client.on_message(filters.command("play"))
async def play_command(client, message):
    if len(message.command) < 2:
        await message.reply_text("❗ Usage: `/play <song name or URL>`")
        return

    query = message.text.split(None, 1)[1]
    await message.reply_text(f"🔎 Searching: `{query}`...")

    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        url = info['url']
        title = info.get('title')

    await message.reply_text(f"▶️ Playing: **{title}**")

    await call.join_group_call(
        message.chat.id,
        AudioPiped(url)
    )
