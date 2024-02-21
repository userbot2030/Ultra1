"""
yang hapus credits pantatnya bisulan
create by: https://t.me/NorSodikin 
"""

import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from .. import *

__MODULE__ = "spamg"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴘᴀᴍ ɢᴄᴀꜱᴛ 』</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spamg</code> (ᴊᴜᴍʟᴀʜ) - ᴛᴇxᴛ/ʀᴇᴘʟʏ_ᴍsɢ
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ sᴘᴀᴍ ɢᴄᴀsᴛ sᴇᴄᴀʀᴀ ʙᴇʀsᴀᴍᴀᴀɴ sᴇᴄᴀʀᴀ ʀᴇᴀʟ-ᴛɪᴍᴇ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setdelay</code> (ᴄᴏᴜɴᴛ) 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴛᴜʀ ᴅᴇʟᴀʏ sᴇᴛɪᴀᴘ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪ ᴋɪʀɪᴍ

  <b>NB:</b> ᴊᴀɴɢᴀɴ ᴛᴇʀʟᴀʟᴜ sᴇʀɪɴɢ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴍᴏᴅᴜʟᴇ ɪɴɪ
"""


def extract_type_and_msg(message):
    args = message.text.split(None, 2)

    if len(args) < 2:
        return None, None

    type = args[1]
    msg = message.reply_to_message if message.reply_to_message else args[2] if len(args) > 2 else None
    return type, msg


async def SpamGcast(client, message, send):
    sent = 0
    blacklist = await get_chat(client.me.id)

    async def send_message(target_chat):
        await asyncio.sleep(0.8)
        if message.reply_to_message:
            await send.copy(target_chat)
        else:
            await client.send_message(target_chat, send)

    async def handle_flood_wait(exception, target_chat):
        await asyncio.sleep(exception.value)
        await send_message(target_chat)

    async for dialog in client.get_dialogs():
        if dialog.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP} and dialog.chat.id not in blacklist:
            try:
              await send_message(dialog.chat.id)
              sent = 1
           except FloodWait as e:
              await handle_flood_wait(e, dialog.chat.id)
          except Exception:
              pass


@PY.UBOT("spamg")
@PY.TOP_CMD
async def _(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113891550788324241"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6114011655253790197"
    r = await message.reply(f"<b><emoji id={proses}>⏳</emoji> ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</b>")
    count, msg = extract_type_and_msg(message)
    jumlah = 0

    try:
        count = int(count)
    except Exception as error:
      jumlah += 1
        return await r.edit(error)
        
    if not msg:
        return await r.edit(f"<b><emoji id={gagal}>❌</emoji> <code>{message.text.split()[0]}</code> ᴊᴜᴍʟᴀʜ - ᴛᴇxᴛ/ʀᴇᴘʟʏ_ᴍsɢ</b>")

    async def run_spam():
        spam_gcast = [SpamGcast(client, message, msg) for _ in range(int(count))]
        await asyncio.gather(*spam_gcast)

    await run_spam()
    return await r.edit(f"<b><emoji id={sukses}>✅</emoji> {sent} sɢᴄᴀsᴛ ᴛᴇʟᴀʜ sᴇʟᴇsᴀɪ ᴅɪʟᴀᴋᴜᴋᴀɴ jumlah putaran {jumlah}</b>")


@PY.UBOT("setdelay")
@PY.TOP_CMD
async def _(client, message):
    r = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")
    count, msg = extract_type_and_msg(message)

    if count.lower() == "none":
        await set_vars(client.me.id, "SPAM", 0)
        return await r.edit("<b>sᴘᴀᴍ ᴅᴇʟᴀʏ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ</b>")

    try:
        count = int(count)
    except Exception as error:
        return await r.edit(error)

    if not count:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> ᴄᴏᴜɴᴛ</b>")

    await set_vars(client.me.id, "SPAM", count)
    return await r.edit("<b>sᴘᴀᴍ ᴅᴇʟᴀʏ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ</b>")
