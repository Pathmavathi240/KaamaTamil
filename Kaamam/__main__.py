from pyrogram import Client
from pytgcalls import PyTgCalls
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

from DeadlineTech.plugins import *  # load all plugins

if __name__ == "__main__":
    print("✅ Bot Started!")
    app.start()
    call.start()
    print("🎵 Ready to play music!")
    idle()
