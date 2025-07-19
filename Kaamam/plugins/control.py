from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types.input_stream import AudioPiped

from Kaamam import call
from Kaamam.utils.queue import pop_next

@Client.on_message(filters.command("pause"))
async def pause_stream(_, message: Message):
    await call.pause_stream(message.chat.id)
    await message.reply_text("⏸️ Music paused.")

@Client.on_message(filters.command("resume"))
async def resume_stream(_, message: Message):
    await call.resume_stream(message.chat.id)
    await message.reply_text("▶️ Music resumed.")

@Client.on_message(filters.command("skip"))
async def skip_stream(_, message: Message):
    next_song = pop_next(message.chat.id)
    if next_song:
        await call.change_stream(message.chat.id, AudioPiped(next_song["url"]))
        await message.reply_photo(
            photo=next_song["thumb"],
            caption=f"⏭️ Skipped to next:\n**{next_song['title']}**"
        )
    else:
        await call.leave_group_call(message.chat.id)
        await message.reply_text("❌ No more songs in queue.")

@Client.on_message(filters.command("stop"))
async def stop_stream(_, message: Message):
    await call.leave_group_call(message.chat.id)
    await message.reply_text("🛑 Music stopped and VC left.")
