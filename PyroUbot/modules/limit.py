from .. import *

__MODULE__ = "ʟɪᴍɪᴛ"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟɪᴍɪᴛ 』

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}limit</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴄᴇᴋ sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴀᴘᴀᴋᴀʜ ᴛᴇʀᴋᴇɴᴀʟ ʟɪᴍɪᴛ ᴀᴛᴀᴜ ᴛɪᴅᴀᴋ
"""


@PY.UBOT("limit")
async def _(client, message):
    await limit_cmd(client, message)

