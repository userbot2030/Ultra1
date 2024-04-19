from PyroUbot import *

@PY.NO_CMD_UBOT("ANTI_USERS", ubot)
async def _(client, message):
    is_users = await get_list_from_vars(bot.me.id, "BL_USERS") or []
    user_id = message.from_user.id if message.from_user else message.sender_chat.id

    if user_id in is_users:
        try:
            await message.delete()
        except Exception as e:
            await message.reply("<b>sᴀʏᴀ ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ᴀᴋsᴇs ᴛᴇʀʜᴀᴅᴀᴘ ɢʀᴏᴜᴘ ɪɴɪ</b>")
