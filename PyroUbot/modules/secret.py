from .. import *

__MODULE__ = "sᴇᴄʀᴇᴛ"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴄʀᴇᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}msg</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ - ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sᴇᴄᴀʀᴀ ʀᴀʜᴀsɪᴀ
"""


@PY.UBOT("msg")
async def _(client, message):
    await msg_cmd(client, message)


@PY.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
