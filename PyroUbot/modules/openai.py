from PyroUbot import *

__MODULE__ = "ai"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɪ ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ai</code></code>  [ǫᴜᴇʀʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴊᴜᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴇ ᴄʜᴀᴛɢᴘᴛ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}dalle</code></code> [ǫᴜᴇʀʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ᴘʜᴏᴛᴏ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}stt</code> [ʀᴇᴘʟʏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘᴇsᴀɴ sᴜᴀʀᴀ ᴋᴇ ᴛᴇxᴛ
"""


@PY.UBOT("ai")
@PY.TOP_CMD
async def _(client, message):
    await ai_cmd(client, message)


@PY.UBOT("dalle")
@PY.TOP_CMD
async def _(client, message):
    await dalle_cmd(client, message)


@PY.UBOT("stt")
@PY.TOP_CMD
async def _(client, message):
    await stt_cmd(client, message)
