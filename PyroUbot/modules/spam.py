from PyroUbot import *

__MODULE__ = "sᴘᴀᴍ"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴀᴍ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}spam</code> [ᴊᴜᴍʟᴀʜ_ᴘᴇsᴀɴ - ᴘᴇsᴀɴ_sᴘᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ sᴘᴀᴍ ᴘᴇsᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}dspam</code> [ᴊᴜᴍʟᴀʜ_ᴘᴇsᴀɴ - ᴊᴜᴍʟᴀʜ_ᴅᴇʟᴀʏ_ᴅᴇᴛɪᴋ - ᴘᴇsᴀɴ_sᴘᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ sᴘᴀᴍ ᴘᴇsᴀɴ ᴅᴇʟᴀʏ
"""


@PY.UBOT(["spam", "dspam"])
async def _(client, message):
    await spam_cmd(client, message)
