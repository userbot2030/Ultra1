from PyroUbot import *

@PY.NO_CMD_UBOT("ANTI_USERS", ubot)
async def _(client, message):
    is_users = await get_list_from_vars(bot.me.id, "BL_USERS") or []
    user_id = message.from_user.id if message.from_user else message.sender_chat.id

    if user_id in is_users:
        try:
            await message.delete()
        except Exception as e:
            await message.reply("<b>sᴀʏᴀ ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ᴀᴋsᴇs ᴛᴇʀʜᴀᴅᴀᴘ ɢʀᴏᴜᴘ ɪɴɪ</b>")



@PY.BOT("dor")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "BL_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>sudah dalam daftar</code></b>
"""
        )

    try:
        await add_to_vars(client.me.id, "BL_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>dor</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("undor")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "BL_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>tidak dalam daftar dor user</code></b>
"""
        )

    try:
        await remove_from_vars(client.me.id, "BL_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>undor</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getdor")
@PY.OWNER
async def _(client, message):
    Sh = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    admin_users = await get_list_from_vars(client.me.id, "BL_USERS")

    if not admin_users:
        return await Sh.edit("<s>ᴅᴀғᴛᴀʀ ᴅᴏʀ ᴜsᴇʀ ᴋᴏsᴏɴɢ</s>")

    admin_list = []
    for user_id in admin_users:
        try:
            user = await client.get_users(int(user_id))
            admin_list.append(
                f"<b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code></b>"
            )
        except:
            continue

    if admin_list:
        response = (
            "<b>📋 ᴅᴀғᴛᴀʀ ᴅᴏʀ ᴜsᴇʀ:</b>\n\n"
            + "\n".join(admin_list)
            + f"\n\n<b>⚜️ ᴛᴏᴛᴀʟ ᴅᴏʀ ᴜsᴇʀ:</b> <code>{len(admin_list)}</code>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ</b>")
