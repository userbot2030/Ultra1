import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from PyroUbot import *

__MODULE__ = "profil"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜰɪʟ 』</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}setbio</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴀɴᴅᴀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}setname</ᴄᴏᴅᴇ> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴀɴᴅᴀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}block</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unblock</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ
"""

@PY.UBOT("unblock")
@PY.TOP_CMD
async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    tex = await message.reply(f"{proses} ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if not user_id:
        return await tex.edit(f"{gagal} ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ʙʟᴏᴋɪʀ.")
    if user_id == client.me.id:
        return await tex.edit(f"{sukses} ᴏᴋ ᴅᴏɴᴇ.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"{sukses} <b>ʙᴇʀʜᴀꜱɪʟ ᴅɪʙᴇʙᴀꜱᴋᴀɴ</b> {umention}")

@PY.UBOT("block")
@PY.TOP_CMD
async def block_user_func(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    user_id = await extract_user(message)
    tex = await message.reply(f"{proses} ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if not user_id:
        return await tex.edit(f"{gagal} ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜɴᴛᴜᴋ ᴅɪʙʟᴏᴋɪʀ.")
    if user_id == client.me.id:
        return await tex.edit(f"{sukses} ᴏᴋ ᴅᴏɴᴇ.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"{sukses} <b>ʙᴇʀʜᴀꜱɪʟ ᴅɪʙʟᴏᴋɪʀ</b> {umention}")

@PY.UBOT("setname")
@PY.TOP_CMD
async def setname(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    tex = await message.reply(f"{proses} ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if len(message.command) == 1:
        return await tex.edit(f"{gagal} ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀɴᴅᴀ.")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"{sukses} <b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴍᴇɴᴊᴀᴅɪ</b> <code>{name}</code>"
            )
        except Exception as e:
            await tex.edit(f"{gagal} <b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit(f"{gagal} ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀɴᴅᴀ.")

@PY.UBOT("setbio")
@PY.TOP_CMD
async def set_bio(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    tex = await message.reply(f"{proses} ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if len(message.command) == 1:
        return await tex.edit(f"{gagal} ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"{sukses} <b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴍᴇɴᴊᴀᴅɪ</b> <code>{bio}</code>")
        except Exception as e:
            await tex.edit(f"{gagal} <b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit(f"{gagal} ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ.")
