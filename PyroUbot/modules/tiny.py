from .. import *

__MODULE__ = "ᴛɪɴʏ"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛɪɴʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}tiny</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ᴋᴇᴄɪʟ
"""


@PY.UBOT("tiny")
async def _(client, message):
    await tiny_cmd(client, message)
