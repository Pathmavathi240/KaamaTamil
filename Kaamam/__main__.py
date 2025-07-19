import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from Kaamam.config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, MONGO_URL
from Kaamam.utils.mongo import connect_mongo
from Kaamam import call

from Kaamam import plugins  # make sure plugins is loaded
from pyrogram import idle

# 🔹 Bot Client
bot = Client(
    name="KaamamBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Kaamam/plugins")
)

# 🔹 Userbot Client (via String Session)
user = Client(
    name="KaamamUser",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# 🔹 Voice Call Client (PyTgCalls)
call = PyTgCalls(user)


async def main():
    print("🔁 Starting Clients...")

    # ✅ Start all clients
    await bot.start()
    await user.start()
    await call.start()

    print("✅ Bot and Userbot Started")
    print("✅ Voice Call Client Started")

    # ✅ Connect to MongoDB
    await connect_mongo()

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
