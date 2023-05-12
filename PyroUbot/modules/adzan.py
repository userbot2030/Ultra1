from PyroUbot import *

__MODULE__ = "ᴀᴅᴢᴀɴ"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴢᴀɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:<b/> <code>{PREFIX[0]}adzan</code> [ɴᴀᴍᴀ ᴋᴏᴛᴀ]y
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴊᴀᴅᴡᴀʟ ᴀᴅᴢᴀɴ ᴅɪ ʟᴏᴋᴀsɪ ᴀɴᴅᴀ
"""


@PY.UBOT("adzan")
async def _(client, message):
    await jadwal_adzan(client, message)
