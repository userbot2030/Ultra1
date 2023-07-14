from PyroUbot *

__MODULE__ = "google"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴏᴏɢʟᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}google [ǫᴜᴇʀʏ]</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴғᴏʀᴍᴀsɪ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ
"""

@PY.UBOT("google")
async _(client, message):
    await google_search(client, message)
