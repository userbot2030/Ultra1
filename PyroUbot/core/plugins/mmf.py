import asyncio
import os

from PyroUbot import *


async def memify_cmd(client, message):
    if not message.reply_to_message:
        return await message.reply("ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ꜰᴏᴛᴏ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ!")
    reply_message = message.reply_to_message
    if not reply_message.media:
        return await message.reply("ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ꜰᴏᴛᴏ ᴀᴛᴀᴜ sᴛɪᴄᴋᴇʀ")
    file = await client.download_media(reply_message)
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5215484787325676090"
    Tm = await message.reply(f"<emoji id={proses}>🔍</emoji> ᴘʀᴏᴄᴇssɪɴɢ ɴɪʜ ʙʀᴇᴇ . . .")
    text = get_arg(message)
    if len(text) < 1:
        return await Tm.edit(f"ʜᴀʀᴀᴘ ᴋᴇᴛɪᴋ {PREFIX[0]}mmf ᴛᴇxᴛ")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        Tm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=message.id,
        ),
    )
    os.remove(meme)
