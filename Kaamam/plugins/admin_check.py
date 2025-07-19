from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

async def is_admin(client: Client, message: Message):
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    except:
        return False
