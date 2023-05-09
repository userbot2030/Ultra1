from PyroUbot.config import PREFIX, bot


class HELP:
    def KANG():
        return f"""
<ʙ>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛɪᴄᴋᴇʀ ᴋᴀɴɢ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}kang</code> [ʀᴇᴘʟʏ ᴛᴏ ɪᴍᴀɢᴇ/sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴅᴀɴ ᴄᴏsᴛᴜᴍ ᴇᴍᴏᴊɪ sᴛɪᴄᴋᴇʀ ᴋᴇ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ
"""

    def MEMIFY():
        return f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛɪᴄᴋᴇʀ ᴍᴇᴍɪꜰʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}mmf</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʙᴀʟᴀs ᴋᴇ sᴛɪᴄᴋᴇʀ ᴀᴛᴀᴜ ꜰᴏᴛᴏ ᴀᴋᴀɴ ᴅɪ ᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ ᴛᴇᴋs ᴍᴇᴍᴇ ʏᴀɴɢ ᴅɪ ᴛᴇɴᴛᴜᴋᴀɴ
"""

    def MEMES():
        return f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛɪᴄᴋᴇʀ ᴍᴇᴍᴇs 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}memes</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴛɪᴋᴇʀ ᴍᴇᴍᴇs ʀᴀɴᴅᴏᴍ
"""

    def QUOTLY():
        return f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛɪᴄᴋᴇʀ ǫᴜᴏᴛʟʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}q</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ
"""

    def TINY():
        return f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛɪᴄᴋᴇʀ ᴛɪɴʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}tiny</code> [ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ sᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ᴋᴇᴄɪʟ
"""


class MSG:
    def START(message):
        return f"""
<b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

💬 @{bot.me.username} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ

👉🏻 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>
"""


HelpText = {
    "global": HELP.GBAN(),
    "restrict": HELP.RESTRICT(),
    "kang": HELP.KANG(),
    "memify": HELP.MEMIFY(),
    "memes": HELP.MEMES(),
    "quotly": HELP.QUOTLY(),
    "tiny": HELP.TINY(),
}
