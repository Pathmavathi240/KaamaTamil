from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pytgcalls.types.input_stream import AudioPiped
from Kaamam import call
from Kaamam.utils.queue import pop_next, get_queue
from .admin_check import is_admin  # Make sure this file exists!

# /pause command
@Client.on_message(filters.command("pause"))
async def pause_command(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply_text("❌ இந்த கட்டளை group admin க்கு மட்டும்!")

    await call.pause_stream(message.chat.id)
    await message.reply_text("⏸️ இசை தற்காலிகமாக நிறுத்தப்பட்டுள்ளது.")

# /resume command
@Client.on_message(filters.command("resume"))
async def resume_command(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply_text("❌ இந்த கட்டளை group admin க்கு மட்டும்!")

    await call.resume_stream(message.chat.id)
    await message.reply_text("▶️ இசை மீண்டும் தொடங்கியுள்ளது.")

# /skip command
@Client.on_message(filters.command("skip"))
async def skip_command(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply_text("❌ இந்த கட்டளை group admin க்கு மட்டும்!")

    next_song = pop_next(message.chat.id)
    if next_song:
        await call.change_stream(
            message.chat.id,
            AudioPiped(next_song["url"])
        )
        await message.reply_photo(
            photo=next_song["thumb"],
            caption=f"⏭️ அடுத்த பாடல்:\n**{next_song['title']}**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ Close", callback_data="close")]
            ])
        )
    else:
        await call.leave_group_call(message.chat.id)
        await message.reply_text("❗ Queue இல்லை. VC இல் இருந்து வெளியேறியேன்.")

# /end command
@Client.on_message(filters.command("end"))
async def end_command(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply_text("❌ இந்த கட்டளை group admin க்கு மட்டும்!")

    await call.leave_group_call(message.chat.id)
    await message.reply_text("👋 இசை நிறைவு பெற்றது, VC இல் இருந்து வெளியேறினேன்.")
