from PyroUbot import *

__MODULE__ = "zombies"
__HELP__ = """
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴢᴏᴍʙɪᴇs ◗</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}zombies</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇʟᴜᴀʀᴋᴀɴ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴅɪɢʀᴜᴘ ᴀɴᴅᴀ.
"""


@PY.UBOT("zombies")
@PY.TOP_CMD
async def zombies_cmd(client, message):
    chat_id = message.chat.id
    deleted_users = []
    banned_users = 0
    Tm = await message.reply("<code>sᴇᴅᴀɴɢ ᴍᴇᴍᴇʀɪᴋsᴀ</code>")
    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                banned_users += 1
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
        await Tm.edit(f"<b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴇʟᴜᴀʀᴋᴀɴ {banned_users} ᴀᴋᴜɴ ʜᴀɴᴛᴜ</b>")
    else:
        await Tm.edit("<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴀᴋᴜɴ ʜᴀɴᴛᴜ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ</b>")
