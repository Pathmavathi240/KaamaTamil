from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls.types.input_stream import AudioPiped
from Kaamam import call
from Kaamam.utils.thumb import get_thumbnail
from Kaamam.utils.queue import add_to_queue
from Kaamam.utils.mongo import log_song
import yt_dlp

@Client.on_message(filters.command("vplay"))
async def vplay_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❗ Usage: /vplay <song name or YouTube URL>")

    query = message.text.split(None, 1)[1]
    loading_msg = await message.reply_text(f"🔍 `{query}` என்பதை தேடுகிறது...")

    try:
        # ✅ yt-dlp Options with cookie support
        ydl_opts = {
            "format": "bestaudio",
            "noplaylist": True,
            "quiet": True,
            "cookiefile": "Kaamam/resources/cookies.txt"  # <-- cookies path
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            audio_url = info["url"]
            title = info["title"]
            duration = info.get("duration", 0)

        # ✅ Thumbnail
        thumb_url, _ = get_thumbnail(query)

        # ✅ Log song to MongoDB
        log_song(message.chat.id, message.from_user.id, title)

        # ✅ If playing already → Add to queue
        current_call = call.get_call(message.chat.id)
        if current_call is not None:
            add_to_queue(message.chat.id, {
                "url": audio_url,
                "title": title,
                "thumb": thumb_url
            })
            return await loading_msg.edit_media(
                media=thumb_url,
                caption=f"➕ Queue-க்கு சேர்க்கப்பட்டது:\n**{title}**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("❌ Close", callback_data="close")]
                ])
            )

        # ✅ Else, play directly
        await call.join_group_call(
            message.chat.id,
            AudioPiped(audio_url)
        )

        await loading_msg.delete()
        await message.reply_photo(
            photo=thumb_url,
            caption=f"▶️ இப்போது ப்ளே ஆகிறது:\n**{title}**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ Close", callback_data="close")]
            ])
        )

    except Exception as e:
        await loading_msg.edit_text(f"❌ பிழை: `{str(e)}`")
