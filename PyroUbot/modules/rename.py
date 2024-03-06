import os

import wget

from PyroUbot import *

__MODULE__ = "thumbnail"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʜᴜᴍʙɴᴀɪʟ ◗</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}thumb</code> [ʀᴇᴘʟʏ ᴠɪᴅɪᴏ ᴋᴀsɪʜ ʟɪɴᴋ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴇʟᴇɢʜʀᴀᴘʜ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛʜᴜᴍʙɴᴀɪʟ / ᴘʀᴏғɪʟᴇ ᴀᴡᴀʟ ᴠɪᴅɪᴏ, ᴅᴇɴɢᴀɴ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ɪɴɢɪɴ ᴀɴᴅᴀ ᴜʙᴀʜ sᴇsᴜᴀɪ ᴋᴇɪɴɢɪɴᴀɴ ᴀɴᴅᴀ

  <b>➥ ᴄᴏɴᴛᴏʜ ᴘᴇɴɢɢᴜɴᴀᴀɴ:</b> 
  ʀᴇᴘʟʏ ᴠɪᴅɪᴏ ʏᴀɴɢ ɪɴɢɪɴ ᴅɪ ᴜʙᴀʜ ᴛʜᴜᴍʙɴᴀɪʟɴʏᴀ, ʟᴀʟᴜ ᴋᴇᴛɪᴋ ᴄᴍᴅ <code>{0}thumb</code> https://telegra.ph//file/21[ʟɪɴᴋ ᴛᴇʟᴇɢʜʀᴀᴘʜ]

"""


@PY.UBOT("thumb")
@PY.TOP_CMD
async def _(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    reply = message.reply_to_message
    msg = await message.reply(f"<b><emoji id={proses}>🔄</emoji> sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs....</b>")

    if len(message.command) < 2:
        return await msg.edit(f"<b><emoji id={gagal}>❌</emoji> {message.text} ʟɪɴᴋ ᴛᴇʟᴇɢʀᴀᴘʜ</b>")

    elif not message.command[1].endswith((".jpg", ".png")):
        return await msg.edit(f"<b><emoji id={gagal}>❌</emoji> ʟɪɴᴋ ʏᴀɴɢ ᴅɪᴍᴀsᴜᴋᴋᴀɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ</b>")

    elif reply.video:
        await msg.edit(f"<b><b><emoji id={proses}>📥</emoji> sᴇʙᴇɴᴛᴀʀ ᴅɪᴅᴏᴡɴʟᴏᴀᴅ ᴅᴜʟᴜ ᴠɪᴅᴇᴏ ɴʏᴀ</b>")
        media = await client.download_media(reply)
        thumbnail = wget.download(message.command[1])

        try:
            await client.send_video(
                message.chat.id,
                video=media,
                thumb=thumbnail,
                duration=reply.video.duration,
                supports_streaming=True,
                caption=reply.caption or "",
            )
            [os.remove(file) for file in (thumbnail, media) if file and os.path.exists(file)]
            return await msg.delete()

        except Exception as error:
            return await msg.edit(str(error))

    else:
        return await msg.edit(f"<b><emoji id={gagal}>❌</emoji> ᴍᴀᴀғ, ʜᴀɴʏᴀ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪᴅᴜᴋᴜɴɢ</b>")
