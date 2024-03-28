from pyrogram import Client, enums, filters
from pyrogram.types import Message

from PyroUbot import *

__MODULE__ = "joinleave"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴ-ʟᴇᴀᴠᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}kickme</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}join</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴊᴏɪɴ ᴋᴇ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leaveallgc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leaveallch</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leave</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ
"""


@PY.UBOT("join")
@PY.TOP_CMD
async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    try:
        await xxnx.edit(f"ʙᴇʀʜᴀꜱɪʟ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴄʜᴀᴛ ɪᴅ `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("kickme|leave", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪʟᴀʀᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ")
    try:
        await xxnx.edit_text(f"{client.me.first_name} ᴛᴇʟᴀʜ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ɢʀᴜᴘ ɪɴɪ, ʙʏᴇ!!")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def kickmeall(client: Client, message: Message):
    Man = await message.reply("ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ɢʀᴏᴜᴘ...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴏᴜᴘ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ɢʀᴏᴜᴘ"
    )

@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def kickmeallch(client: Client, message: Message):
    Man = await message.reply("ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ᴄʜᴀɴɴᴇʟ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ᴄʜᴀɴɴᴇʟ"
    )
