from PyroUbot import *

__MODULE__ = "invite"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴᴠɪᴛᴇ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}invite</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ

"""


@PY.UBOT("invite")
@PY.TOP_CMD
async def _(client, message):
    await invite_cmd(client, message)


@PY.UBOT("inviteall")
@PY.TOP_CMD
async def _(client, message):
    await inviteall_cmd(client, message)


@PY.UBOT("cancel")
@PY.TOP_CMD
async def _(client, message):
    await cancel_cmd(client, message)
