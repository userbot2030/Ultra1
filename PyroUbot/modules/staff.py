from .. import *

__MODULE__ = "sᴛᴀꜰꜰ"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀꜰꜰ 』

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}staff</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴅᴀꜰᴛᴀʀ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ᴅɪᴅᴀʟᴀᴍ ɢʀᴜᴘ
"""


@PY.UBOT("staff")
async def _(client, message):
    await staff_cmd(client, message)
