from PyroUbot import *

__MODULE__ = "showid"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sʜᴏᴡɪᴅ ◗</b>

  <b>➠ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}id</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ɪᴅ ᴅᴀʀɪ ᴜsᴇʀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ

  <b>➠ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}id</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ/ᴍᴇᴅɪᴀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ɪᴅ ᴅᴀʀɪ ᴜsᴇʀ/ᴍᴇᴅɪᴀ

  <b>➠ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}id</code> [ᴜsᴇʀɴᴀᴍᴇ ᴜsᴇʀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ɪᴅ ᴜsᴇʀ/ɢʀᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴍᴇʟᴀʟᴜɪ ᴜsᴇʀɴᴀᴍᴇ
"""


@PY.UBOT("id")
@PY.TOP_CMD
async def _(client, message):
    await id_cmd(client, message)
