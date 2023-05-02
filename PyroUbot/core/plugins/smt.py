import asyncio
import random

from .. import *


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
        sg = await client.get_messages(-1001835552147, txt.id + 1)
        await message.reply(sg.text)
    except:
        await message.reply("❌ ᴀᴘɪ sᴇᴅᴀɴɢ ᴇʀʀᴏʀ sɪʟᴀʜᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ")
    user_info = await client.resolve_peer(bot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
