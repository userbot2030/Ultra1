from PyroUbot import bot


class MSG:
    def START(message):
        return f"""
<b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

💬 @{bot.me.username} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ

👉🏻 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>
"""
    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ ᴅᴀɴᴀ/ɢᴏᴘᴀʏ/ᴏᴠᴏ/sᴘᴀʏ</b>
 <b>├────• <code>089525658633</code></b>
 <b>├ ǫʀɪs</b>
 <b>└────• <a href=https://api.qrcode-monkey.com/tmp/2274eaefa4ad07bab3a2578ac5c1e000.png>ᴋʟɪᴋ ᴅɪsɪɴɪ</a></b>

<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
"""

