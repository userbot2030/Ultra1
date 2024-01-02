from PyroUbot import *

__MODULE__ = "image"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪᴍᴀɢᴇ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}rbg</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɢᴀᴍʙᴀʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}blur</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀ ᴇꜰᴇᴋ ʙʟᴜʀ ᴋᴇ ɢᴀᴍʙᴀʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}miror</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ᴄᴇʀᴍɪɴ ᴋᴇ ɢᴀᴍʙᴀʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}negative</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪᴋᴀɴ ᴇꜰᴇᴋ ɴᴇɢᴀᴛɪᴠᴇ ᴋᴇ ɢᴀᴍʙᴀʀ
"""


@PY.UBOT("rbg", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await rbg_cmd(client, message)


@PY.UBOT("blur", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await blur_cmd(client, message)


@PY.UBOT("negative", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await negative_cmd(client, message)


@PY.UBOT("miror", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await miror_cmd(client, message)
