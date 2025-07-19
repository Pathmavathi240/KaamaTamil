from pyrogram import Client, idle
from Kaamam import app, call
from Kaamam.plugins import *

import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    print("✅ Kaamam Music Bot Started...")
    app.start()
    call.start()
    idle()
    app.stop()
    print("🛑 Bot Stopped.")
