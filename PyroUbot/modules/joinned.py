from pyrogram import *
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate

from PyroUbot import *

__MODULE__ = "joinleave"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴ-ʟᴇᴀᴠᴇ 』</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}kickme</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}join</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴊᴏɪɴ ᴋᴇ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leaveallgc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leaveallch</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leave</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leaveallmute</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴏᴜᴘ ɢʀᴏᴜᴘ ʏᴀɴɢ ᴅɪ ᴍᴜᴛᴇ
"""


@PY.UBOT("join")
@PY.TOP_CMD
async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    proses = await EMO.PROSES(client)
    sukses = await EMO.SUKSES(client)
    xxnx = await message.reply(f"{proses} ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ʟᴏᴀᴅɪɴɢ")
    try:
        await xxnx.edit(f"{sukses} ʙᴇʀʜᴀꜱɪʟ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴄʜᴀᴛ ɪᴅ `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("kickme|leave", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    proses = await EMO.PROSES(client)
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    xxnx = await message.reply(f"{sukses} ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ʟᴏᴀᴅɪɴɢ")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit(f"{gagal} ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪʟᴀʀᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ")
    try:
        await xxnx.edit_text(f"{sukses} {client.me.first_name} ᴛᴇʟᴀʜ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ɢʀᴜᴘ ɪɴɪ, ʙʏᴇ!!")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def kickmeall(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    Man = await message.reply(f"{proses} ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ʟᴏᴀᴅɪɴɢ")
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
        f"{sukses} ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴏᴜᴘ\n{gagal} ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ɢʀᴏᴜᴘ"
    )

@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def kickmeallch(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    Man = await message.reply(f"{proses} ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ʟᴏᴀᴅɪɴɢ")
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
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    await Man.edit(
        f"{sukses} ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ᴄʜᴀɴɴᴇʟ\n{gagal} ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ᴄʜᴀɴɴᴇʟ"
    )


@PY.UBOT("leaveallmute")
async def _(client, message):
    done = 0
    proses = await EMO.PROSES(client)
    Tk = await message.reply(f"<b>{proses} ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ʟᴏᴀᴅɪɴɢ")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat)
                    done += 1
            except Exception:
                pass
    sukses = await EMO.SUKSES(client)
    await Tk.edit(f"<b>{sukses} Succes Leave {done} Group Muted!!</b>")
