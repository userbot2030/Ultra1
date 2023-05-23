from PyroUbot import *

__MODULE__ = "convert"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴠᴇʀᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}toanime</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʜᴏᴛᴏ/sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}toimg</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ/ɢɪꜰᴛ ᴍᴇɴᴊᴀᴅɪ ᴘʜᴏᴛᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}tosticker</code> [ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜰᴏᴛᴏ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}togif</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ɢɪꜰ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}toaudio</code> [ʀᴇᴘʟʏ ᴛᴏ ᴠɪᴅᴇᴏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴠɪᴅᴇᴏ ᴍᴇɴᴊᴀᴅɪ ᴀᴜᴅɪᴏ ᴍᴘ3

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}efek</code> [ᴇꜰᴇᴋ_ᴄᴏᴅᴇ - ʀᴇᴘʟʏ ᴛᴏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>• ᴇꜰᴇᴋ_ᴄᴏᴅᴇ:</b>  <code>bengek</code> <code>robot</code> <code>jedug</code> <code>fast</code> <code>echo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ sᴜᴀʀᴀ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}colong</code> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ ᴛɪᴍᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴍᴇᴅɪᴀ ᴛɪᴍᴇʀ ᴅᴀɴ ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴇ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ
"""


@PY.UBOT("toanime")
async def _(client, message):
    await convert_anime(client, message)


@PY.UBOT("toimg")
async def _(client, message):
    await convert_photo(client, message)


@PY.UBOT("tosticker")
async def _(client, message):
    await convert_sticker(client, message)


@PY.UBOT("togif")
async def _(client, message):
    await convert_gif(client, message)


@PY.UBOT("toaudio")
async def _(client, message):
    await convert_audio(client, message)


@PY.UBOT("efek")
async def _(client, message):
    await convert_efek(client, message)


@PY.UBOT("colong")
async def _(client, message):
    await colong_cmn(client, message)
