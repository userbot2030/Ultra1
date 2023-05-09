from .. import *

__MODULE__ = "sᴏsᴍᴇᴅ"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴏsᴍᴇᴅ 』

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}sosmed</code> [ʟɪɴᴋ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴅᴀʀɪ ꜰᴀᴄᴇʙᴏᴏᴋ/ᴛɪᴋᴛᴏᴋ/ɪɴsᴛᴀɢʀᴀᴍ/ᴛᴡɪᴛᴛᴇʀ/ʏᴏᴜᴛᴜʙᴇ
"""


@PY.UBOT("sosmed")
async def _(client, message):
    await sosmed_cmd(client, message)
