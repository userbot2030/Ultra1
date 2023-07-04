from PyroUbot import *

__MODULE__ = "setting"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴛᴛɪɴɢ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}prefix - sɪᴍʙᴏʟ/ᴇᴍᴏJɪ</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʀᴇғɪx ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ
"""


@PY.UBOT("prefix")
async def _(client, message):
    await setprefix(client, message)
