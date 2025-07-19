from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        f"👋 வணக்கம் {message.from_user.first_name}!\n\n"
        "🎶 நான் ஒரு Voice Chat Music Bot.\n"
        "📥 /play <song name or YouTube link> என உபயோகிக்கவும்."
    )
)
