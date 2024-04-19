import asyncio

from pyrogram.enums import ChatType
from pyrogram.types import ChatPermissions

from PyroUbot import *


__MODULE__ = "staff"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴛᴀꜰꜰ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}kick</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}mute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unmute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙʟᴏᴋɪʀᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙɪsᴜᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}staff</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴅᴀꜰᴛᴀʀ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ᴅɪᴅᴀʟᴀᴍ ɢʀᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}invite</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}staff</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> 
"""



@PY.UBOT("kick", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_kick(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"{gagal} ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"{gagal} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} ᴅɪᴛᴇɴᴅᴀɴɢ:</b> {mention}\n<b>{admin} ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("ban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_ban(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"{gagal}ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"{gagal} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"{gagal} ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} ᴅɪʙᴀɴɴᴇᴅ:</b> {mention}\n<b>{admin} ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("mute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_mute(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"{gagal} ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"{gagal} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} ᴍᴇᴍʙɪsᴜᴋᴀɴ:</b> {mention}\n<b>{admin} ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unmute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unmute(client, message):
    gagal = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    try:
        sukses = await EMO.SUKSES(client)
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b>{sukses} {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴄʜᴀᴛ ʟᴀɢɪ</b>")
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unban(client, message):
    gagal = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    try:
        sukses = await EMO.SUKSES(client)
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b>{sukses} {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴊᴏɪɴ ʟᴀɢɪ</b>")
    except Exception as error:
        await message.reply(error)



@PY.UBOT("staff")
@PY.TOP_CMD
async def staff_cmd(client, message):
    chat_title = message.chat.title
    creator = []
    co_founder = []
    admin = []
    async for x in message.chat.get_members():
        mention = f"<a href=tg://user?id={x.user.id}>{x.user.first_name} {x.user.last_name or ''}</a>"
        if x.status.value == "administrator" and x.privileges and x.privileges.can_promote_members:
            if x.custom_title:
                co_founder.append(f" ┣ {mention} - {x.custom_title}")
            else:
                co_founder.append(f" ┣ {mention}")
        elif x.status.value == "administrator":
            if x.custom_title:
                admin.append(f" ┣ {mention} - {x.custom_title}")
            else:
                admin.append(f" ┣ {mention}")
        elif x.status.value == "owner":
            if x.custom_title:
                creator.append(f" ┗ {mention} - {x.custom_title}")
            else:
                creator.append(f" ┗ {mention}")
    if not co_founder and not admin:
        result = f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}</b>"""
    elif not co_founder:
        adm = admin[-1].replace("┣", "┗")
        admin.pop(-1)
        admin.append(adm)
        result = f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}

👮 ᴀᴅᴍɪɴ:</b>
""" + "\n".join(
            admin
        )
    elif not admin:
        cof = co_founder[-1].replace(" ┣", " ┗")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}

👮 ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ:</b>
""" + "\n".join(
            co_founder
        )
    else:
        adm = admin[-1].replace(" ┣", " ┗")
        admin.pop(-1)
        admin.append(adm)
        cof = co_founder[-1].replace(" ┣", " ┗")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = (
            (
                f"""
<b>sᴛᴀꜰꜰ ɢʀᴜᴘ
{chat_title}

👑 ᴏᴡɴᴇʀ:
{creator[0]}

👮 ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ:</b>
"""
                + "\n".join(co_founder)
                + """

<b>👮 ᴀᴅᴍɪɴ:</b>
"""
            )
            + "\n".join(admin)
        )

    await message.reply(result)
