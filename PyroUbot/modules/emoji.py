from PyroUbot import *

__MODULE__ = "emoji"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴇᴛ ᴇᴍᴏᴊɪ ◗</b>

<b>❑ ᴄᴍᴅ:</b> <code>{0}setemoji - [ᴋᴀᴛᴀ ᴋᴜɴᴄɪ] [ᴇᴍᴏᴊɪ_ᴘʀᴇᴍ]</code> 
  <b>❑ ᴋᴀᴛᴀ ᴋᴜɴᴄɪ:</b>
  <b>├➧ PING1</b>
  <b>├➧ PING2</b>
  <b>├➧ PING3</b>
  <b>├➧ PROSES</b>
  <b>├➧ GAGAL</b>
  <b>╰➧ SUKSES</b>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴇᴍᴏᴊɪ ᴘᴀᴅᴀ ᴜꜱᴇʀʙᴏᴛ ᴀɴᴅᴀ ᴊɪᴋᴀ ᴀᴋᴜɴ ᴀɴᴅᴀ ᴘʀᴇᴍɪᴜᴍ.
  
"""


@PY.UBOT("setemoji")
@PY.TOP_CMD
async def _(client, message):
    await change_emot(client, message)
