from .. import *

__MODULE__ = "sᴇᴀʀᴄʜ"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴀʀᴄʜ 』

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}bing</code> or <code>{PREFIX[0]}pic</code> [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴘʜᴏᴛᴏ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}gif</code> [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ɢɪꜰᴛ/ᴀɴɪᴍᴀᴛɪᴏɴ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ
"""


@PY.UBOT(["bing", "pic"])
async def _(client, message):
    await pic_bing_cmd(client, message)
  
  
@PY.UBOT("gif")
async def _(client, message):
    await gif_cmd(client, message)
