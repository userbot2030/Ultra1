import asyncio
import random
from PyroUbot import *


async def sg_cmd(client, message):
    user_id = await extract_user(message)
    lol = await message.reply("</b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await lol.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await lol.edit(error)
    bot = ["@Sangmata_bot", "@SangMata_beta_bot"]
    getbot = random.choice(bot)
    txt = await client.send_message(getbot, user.id)
    await asyncio.sleep(4)
    await lol.delete()
    try:
        try:
            for X in [1, 2]:
                sg = await client.get_messages(getbot, txt.id + X)
                await sg.copy(message.chat.id, reply_to_message_id=message.id)
        except:
            pass
    except:
        await message.reply("❌ ᴀᴘɪ sᴇᴅᴀɴɢ ᴇʀʀᴏʀ sɪʟᴀʜᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ")
    user_info = await client.resolve_peer(getbot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
