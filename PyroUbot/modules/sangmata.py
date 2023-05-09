from .. import *

__MODULE__ = "sᴀɴɢᴍᴀᴛᴀ"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴀɴɢᴍᴀᴛᴀ 』

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}sg</code> [ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋsᴀ ʜɪsᴛᴏʀɪ ɴᴀᴍᴀ/ᴜsᴇʀɴᴀᴍᴇ
"""


@PY.UBOT("sg")
async def _(client, message):
    await sg_cmd(client, message?
