import random

from PyroUbot import *

__MODULE__ = "prefix"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴇꜰɪx ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}prefix - sɪᴍʙᴏʟ/ᴇᴍᴏJɪ</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʀᴇғɪx ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ
  
"""


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)


Arab = ["Eh bang arab manggil..", "Nyala kok bang Arab..", "Mwahh😘", "Hadir bang Arab😘", "Iya Arab Iya Manggil baee😭"]


@ubot.on_message(filters.user(DEVS) & filters.command("absen", ".") & ~filters.me)
async def _(client, message):
    await message.reply_text(f"<b>{random.choice(Arab)}</b>")


@PY.UBOT("arab")
sukses = await EMO.SUKSES(client)
async def _(client, message):
    sukses = await EMO.SUKSES(client)
    await message.reply_text(f"<b>{sukses} ouh yang punya</b> <code>{bot.me.mention}</code> <b>kaciw kan</b>")
