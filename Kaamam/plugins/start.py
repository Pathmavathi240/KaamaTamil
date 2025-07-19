from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        f"👋 வணக்கம் {message.from_user.first_name}!\n\n"
        "🎵 இந்த VC Music Bot உங்களுக்கு பாடல்கள் play செய்ய உதவும்.\n"
        "🔊 /play <song name> அல்லது /vplay <YouTube link> என பயன்படுத்துங்கள்.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📢 Support", url="https://t.me/YourSupportGroup"),
                    InlineKeyboardButton("🌐 Repo", url="https://github.com/YourUsername/MY_VC_MUSIC_BOT")
                ],
                [
                    InlineKeyboardButton("❌ Close", callback_data="close")
                ]
            ]
        )
    )
