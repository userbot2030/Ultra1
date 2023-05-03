from .. import *

__MODULE__ = "ADZAN"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴢᴀɴ 』

  <b>• ᴘᴇʀɪɴᴛᴀʜ:<b/> <code>{PREFIX[0]}adzan</code> [ɴᴀᴍᴀ ᴋᴏᴛᴀ]y
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴊᴀᴅᴡᴀʟ ᴀᴅᴢᴀɴ ᴅɪ ʟᴏᴋᴀsɪ ᴀɴᴅᴀ
"""


@PY.UBOT("adzan")
async def _(client, message):
    await jadwal_adzan(client, message)
