from PyroUbot import *

__MODULE__ = "copy"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏᴘʏ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}copy</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘᴇsᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴍᴇʀᴇᴋᴀ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}thumb</code> [ʀᴇᴘʟʏ ᴠɪᴅɪᴏ ᴋᴀsɪʜ ʟɪɴᴋ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴇʟᴇɢʜʀᴀᴘʜ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛʜᴜᴍʙɴᴀɪʟ / ᴘʀᴏғɪʟᴇ ᴀᴡᴀʟ ᴠɪᴅɪᴏ, ᴅᴇɴɢᴀɴ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴀɴᴅᴀ ᴜʙᴀʜ sᴇsᴜᴀɪ ᴋᴇɪɴɢɪɴᴀɴ ᴀɴᴅᴀ

  <b>➥ ᴄᴏɴᴛᴏʜ ᴘᴇɴɢɢᴜɴᴀᴀɴ:</b> 
  ʀᴇᴘʟʏ ᴠɪᴅɪᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪ ᴜʙᴀʜ ᴛʜᴜᴍʙɴᴀɪʟɴʏᴀ, ʟᴀʟᴜ ᴋᴇᴛɪᴋ ᴄᴍᴅ <code>{0}thumb</code> https://telegra.ph//file/21[ʟɪɴᴋ ᴛᴇʟᴇɢʜʀᴀᴘʜ]
  """


@PY.BOT("copy")
async def _(client, message):
    await copy_bot_msg(client, message)


@PY.UBOT("copy")
@PY.TOP_CMD
async def _(client, message):
    await copy_ubot_msg(client, message)


@PY.INLINE("^get_msg")
@INLINE.QUERY
async def _(client, inline_query):
    await copy_inline_msg(client, inline_query)


@PY.CALLBACK("^copymsg")
@INLINE.DATA
async def _(client, callback_query):
    await copy_callback_msg(client, callback_query)
