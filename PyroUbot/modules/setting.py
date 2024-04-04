import random

from PyroUbot import *

__MODULE__ = "prefix"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴇꜰɪx ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}prefix - sɪᴍʙᴏʟ/ᴇᴍᴏJɪ</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʀᴇғɪx ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ
  
"""


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)


Arab = ["ᴡʜʏ ғᴀᴍɪʟʏ!!"]

Hemi = ["Ganteng Banget!!"]


@ubot.on_message(filters.command(["absen"], ".") & filters.user([1948147616, 1819269848, 843716328, 7021645452]))
async def _(client, message):
    await message.reply_text(f"<b>{random.choice(Arab)}</b>")

@ubot.on_message(filters.command(["Hemi"], ".") & filters.user([1948147616, 1819269848, 843716328, 7021645452]))
async def _(client, message):
    await message.reply_text(f"<b>{random.choice(Hemi)}</b>")
