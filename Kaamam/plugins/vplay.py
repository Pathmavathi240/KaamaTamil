from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls.types.input_stream import AudioPiped

from Kaamam import call
from Kaamam.utils.thumb import get_thumbnail
from Kaamam.utils.queue import add_to_queue, pop_next
from Kaamam.utils.mongo import log_song

import yt_dlp

@Client.on_message(filters.command("vplay"))
async def vplay_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❗ Usage: /vplay <song name or YouTube URL>")

    query = message.text.split(None, 1)[1]
    await message.reply_text(f"🔍 Searching for `{query}`...")

    try:
        # YouTube song details fetch
        ydl_opts = {"format": "bestaudio", "noplaylist": True, "quiet": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            audio_url = info["url"]
            title = info["title"]
            duration = info.get("duration", 0)

        # Thumbnail
        thumb_url, _ = get_thumbnail(query)

        # MongoDB log
        log_song(message.chat.id, message.from_user.id, title)

        # Already playing? => Add to queue
        current_chat = call.get_call(message.chat.id)
        if current_chat is not None:
            add_to_queue(message.chat.id, {
                "url": audio_url,
                "title": title,
                "thumb": thumb_url
            })
            return await message.reply_photo(
                photo=thumb_url,
                caption=f"✅ Queue-வில் சேர்க்கப்பட்டது:\n**{title}**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("❌ Close", callback_data="close")]
                ])
            )

        # VC-ல் direct stream
        await call.join_group_call(
            message.chat.id,
            AudioPiped(audio_url),
        )

        await message.reply_photo(
            photo=thumb_url,
            caption=f"▶️ தற்போது பிளே ஆகிறது:\n**{title}**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ Close", callback_data="close")]
            ])
        )

    except Exception as e:
        await message.reply_text(f"❌ பிழை: `{str(e)}`")
