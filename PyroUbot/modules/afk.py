"create by: NorSodikin.t.me"
"request by: Dhilnihnge.t.me"


from time import time

from PyroUbot import *

__MODULE__ = "afk"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀғᴋ 』</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>afk</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ 

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>unafk</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ
"""


@PY.UBOT("afk")
@PY.TOP_CMD
async def _(client, message):
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
    emot_2 = await get_vars(client.me.id, "EMOJI_REASON")
    emot_afk = emot_1 if emot_1 else "5467890025217661107"
    emot_reason = emot_2 if emot_2 else "6230829139297831733"
    if client.me.is_premium:
        msg_afk = (
            f"<b><emoji id={emot_afk}>🦇</emoji>sᴇᴅᴀɴɢ ᴀғᴋ\n<emoji id={emot_reason}>📝</emoji>ᴀʟᴀsᴀɴ: {reason}</b>"
            if reason
            else f"<b><emoji id={emot_afk}>‼️</emoji>sᴇᴅᴀɴɢ ᴀғᴋ</b>"
        )
    else:
        msg_afk = (
            f"<b>sᴇᴅᴀɴɢ ᴀғᴋ\nᴀʟᴀsᴀɴ: {reason}</b>"
            if reason
            else "<b>sᴇᴅᴀɴɢ ᴀғᴋ</b>"
        )
    await set_vars(client.me.id, "AFK", db_afk)
    await message.reply(msg_afk)
    return await message.delete()



@PY.AFK()
async def _(client, message):
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
        emot_2 = await get_vars(client.me.id, "EMOJI_REASON")
        emot_3 = await get_vars(client.me.id, "EMOJI_WAKTU")
        emot_afk = emot_1 if emot_1 else "5213205860498549992"
        emot_reason = emot_2 if emot_2 else "6230829139297831733"
        emot_waktu = emot_3 if emot_3 else "5895288113537748673"
        if client.me.is_premium:
            afk_text = (
                f"<b><emoji id={emot_afk}>🦇</emoji>sᴇᴅᴀɴɢ ᴀғᴋ\n<emoji id={emot_waktu}>⏰</emoji>ᴡᴀᴋᴛᴜ: {afk_runtime}\n<emoji id={emot_reason}>🏓</emoji>ᴀʟᴀsᴀɴ: {afk_reason}</b>"
                if afk_reason
                else f"<b><emoji id={emot_afk}>🦇</emoji>sᴇᴅᴀɴɢ ᴀғᴋ\n<emoji id={emot_waktu}>⏰</emoji>ᴡᴀᴋᴛᴜ: {afk_runtime}</b>"
            )
        else:
            afk_text = (
                f"<b>sᴇᴅᴀɴɢ ᴀғᴋ\nᴡᴀᴋᴛᴜ: {afk_runtime}\nᴀʟᴀsᴀɴ: {afk_reason}</b>"
                if afk_reason
                else f"<b>sᴇᴅᴀɴɢ ᴀғᴋ\nᴡᴀᴋᴛᴜ: {afk_runtime}</b>"
            )
        return await message.reply(afk_text)


@PY.UBOT("unafk")
@PY.TOP_CMD
async def _(client, message):
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        afk_text = f"<b>ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\nᴀғᴋ sᴇʟᴀᴍᴀ: {afk_runtime}</b>"
        await message.reply(afk_text)
        await message.delete()
        return await remove_vars(client.me.id, "AFK")
