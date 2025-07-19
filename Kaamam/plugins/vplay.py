from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DeadlineTech.utils.thumb import get_thumbnail

@Client.on_message(filters.command("vplay"))
async def vplay_command(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❗ Usage: /vplay <song name or YouTube URL>")

    query = message.text.split(None, 1)[1]
    await message.reply_text(f"🔍 Searching for `{query}`...")

    try:
        thumb_url, title = get_thumbnail(query)

        # Stream logic same as before...

        # Send thumbnail with buttons
        await message.reply_photo(
            photo=thumb_url,
            caption=f"▶️ Streaming: **{title}**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ Close", callback_data="close")]
            ])
        )

    except Exception as e:
        await message.reply_text(f"❌ Error: `{str(e)}`")
