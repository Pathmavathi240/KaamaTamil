from pyrogram.errors import UserNotParticipant

async def is_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in ["administrator", "creator"]
    except UserNotParticipant:
        return False
