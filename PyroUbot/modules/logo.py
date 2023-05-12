from PyroUbot import *

__MODULE__ = "ʟᴏɢᴏ"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}logo</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ʟᴏɢᴏ ᴅᴇɴɢᴀɴ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴀɴᴅᴏᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}blogo</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ʟᴏɢᴏ ᴅᴇɴɢᴀɴ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʜɪᴛᴀᴍ  
"""


@PY.UBOT(["blogo", "logo"])
async def _(client, message):
    await logo_cmd(client, message)
