from PyroUbot import *

__MODULE__ = "tagall"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴀɢᴀʟʟ ◗</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tagall</code> [ᴛʏᴘᴇ ᴍᴇssᴀɢᴇ/ʀᴇᴘʟʏ ᴍᴇssᴀɢᴇ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇɴᴛɪᴏɴ sᴇᴍᴜᴀ ᴀɴɢɢᴏᴛᴀ ɢʀᴜᴘ ᴅᴇɴɢᴀɴ ᴘᴇsᴀɴ ʏᴀɴɢ ᴀɴᴅᴀ ɪɴɢɪɴᴋᴀɴ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cancel</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴍᴇᴍᴇɴᴛɪᴏɴ ᴀɴɢɢᴏᴛᴀ ɢʀᴜᴘ
"""


@PY.UBOT("tagall")
@PY.TOP_CMD
async def _(client, message):
    await tagall_cmd(client, message)


@PY.UBOT("cancel")
@PY.TOP_CMD
async def _(client, message):
    await batal_cmd(client, message)
