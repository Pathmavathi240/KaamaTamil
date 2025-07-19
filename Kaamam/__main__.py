import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls

from Kaamam.config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from Kaamam.utils.mongo import connect_mongo

# 🔹 Bot Client
bot = Client(
    name="KaamamBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Kaamam/plugins")
)

# 🔹 Userbot Client
user = Client(
    name="KaamamUser",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# 🔹 Voice Call Client
call = PyTgCalls(user)


async def main():
    print("🔁 Starting Clients...")

    await bot.start()
    await user.start()
    await call.start()

    print("✅ Bot and Userbot Started")
    print("✅ Voice Call Client Started")

    db = connect_mongo()  # ✅ NO await needed here
    print("📦 Connected to MongoDB")
    print("🤖 Bot is now running...")

    await idle()

    # Stop all clients when idle ends
    await bot.stop()
    await user.stop()
    await call.stop()

    print("❌ Bot stopped.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("⚠️ Force Stopped!")
