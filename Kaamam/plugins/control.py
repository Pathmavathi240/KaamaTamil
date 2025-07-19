from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import GroupCallNotFoundError
from Kaamam.__main__ import call

@Client.on_message(filters.command("pause"))
async def pause_command(client, message):
    try:
        await call.pause_stream(message.chat.id)
        await message.reply_text("⏸️ Music Paused")
    except GroupCallNotFoundError:
        await message.reply_text("❌ VC Not Active")

@Client.on_message(filters.command("resume"))
async def resume_command(client, message):
    try:
        await call.resume_stream(message.chat.id)
        await message.reply_text("▶️ Music Resumed")
    except GroupCallNotFoundError:
        await message.reply_text("❌ VC Not Active")

@Client.on_message(filters.command("leave"))
async def leave_command(client, message):
    try:
        await call.leave_group_call(message.chat.id)
        await message.reply_text("👋 Left VC")
    except GroupCallNotFoundError:
        await message.reply_text("❌ Not in VC")

@Client.on_message(filters.command("skip"))
async def skip_command(client, message):
    await message.reply_text("⏭️ Skip not implemented yet.")
