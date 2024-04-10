import asyncio
from random import shuffle
from PyroUbot import *

__MODULE__ = "tagall"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴀɢᴀʟʟ ◗</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tagall</code> [ᴛʏᴘᴇ ᴍᴇssᴀɢᴇ/ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇɴᴛɪᴏɴ sᴇᴍᴜᴀ ᴀɴɢɢᴏᴛᴀ ɢʀᴜᴘ ᴅᴇɴɢᴀɴ ᴘᴇsᴀɴ ʏᴀɴɢ ᴀɴᴅᴀ ɪɴɢɪɴᴋᴀɴ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cancel</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴍᴇᴍᴇɴᴛɪᴏɴ ᴀɴɢɢᴏᴛᴀ ɢʀᴜᴘ
"""



tagallgcid = []


@PY.UBOT("tagall")
@PY.TOP_CMD
async def tagall_cmd(client, message):
    if message.chat.id in tagallgcid:
        return
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [member.user.mention async for member in message.chat.get_members() if not (member.user.is_bot or member.user.is_deleted)]
    shuffle(users)
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if message.chat.id not in tagallgcid:
            break
        await asyncio.sleep(1.5)
        await m.reply_text("\n ".join([f"{emoji.TELEPHONE} {output[i]}" for i in range(len(output))]) + "\n\n" + text, quote=bool(message.reply_to_message))
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass




@PY.UBOT("cancel")
@PY.TOP_CMD
async def batal_cmd(client, message):
    if message.chat.id not in tagallgcid:
        return await message.reply_text("sedang tidak ada perintah: <code>tagall</code> yang digunakan")
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass
    await message.reply_text("ok tagall berhasil dibatalkan")
