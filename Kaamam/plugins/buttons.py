from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Client.on_callback_query()
async def handle_buttons(_, query: CallbackQuery):
    if query.data == "close":
        await query.message.delete()
