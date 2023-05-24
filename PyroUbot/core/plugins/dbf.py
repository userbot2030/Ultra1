from datetime import datetime, timedelta

from pytz import timezone

from PyroUbot import *

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    if message.from_user.id not in await get_seles():
        return await message.reply("ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀɴᴅᴀ ʜᴀʀᴜs ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ")
    user_id = await extract_user(message)
    Tm = await message.reply("<b>Processing . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>Balas pesan pengguna atau berikan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    premium = await get_prem()
    if user.id in premium:
        return await Tm.edit("Dia Sudah Bisa Membuat Userbot")
    added = await add_prem(user.id)
    if added:
        await Tm.edit(f"✅ {user.mention} silahkan buat userbot di @{bot.me.username}")
        await bot.send_message(
            OWNER_ID,
            f"""
• <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>
• <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a>
""",
        )
    else:
        await Tm.delete()
        await message.reply_text("Terjadi kesalahan, periksa log.")


async def unprem_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>Processing . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>Balas pesan pengguna atau berikan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delpremium = await get_prem()
    if user.id not in delpremium:
        return await message.reply_text("<b>Tidak Ditemukan</b>")
    removed = await remove_prem(user.id)
    if removed:
        await Tm.edit(f"<b> ✅ {user.mention} berhasil dihapus</b>")
    else:
        await Tm.delete()
        await message.reply_text("Terjadi kesalahan, periksa log.")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply_text("Tidak Ada Pengguna Yang Ditemukan")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blaclist(client, message):
    Tm = await message.reply("<b>Processing . . .</b>")
    chat_id = message.chat.id
    blacklist = await get_chat()
    if chat_id in blacklist:
        return await Tm.edit("group ini sudah ada dalam blacklist")
    add_blacklist = await add_chat(chat_id)
    if add_blacklist:
        await Tm.edit(f"{message.chat.title} berhasil di ditambahkan ke daftar hitam")
    else:
        await Tm.edit("terjadi kesalahan yang tidak diketahui")


async def del_blacklist(client, message):
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    try:
        if not get_arg(message):
            chat_id = message.chat.id
        else:
            chat_id = int(get_arg(message))
        blacklist = await get_chat()
        if chat_id not in blacklist:
            return await Tm.edit(f"{message.chat.title} tidak ada dalam daftar hitam")
        del_blacklist = await remove_chat(chat_id)
        if del_blacklist:
            await Tm.edit(f"{chat_id} berhasil dihapus dari daftar hitam")
        else:
            await Tm.edit("terjadi kesalahan yang tidak diketahui")
    except Exception as error:
        await Tm.edit(error)


async def get_blacklist(client, message):
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    msg = f"<b>• ᴛᴏᴛᴀʟ ʙʟᴀᴄᴋʟɪsᴛ {len(await get_chat())}</b>\n\n"
    for X in await get_chat():
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await Tm.delete()
    await message.reply(msg)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>Balas pesan pengguna atau berikan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await Tm.edit("Sudah menjadi reseller.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await Tm.edit(f"<b>✅ {user.mention} teleh menjadi reseller</b>")
    else:
        await Tm.delete()
        await message.reply_text("Terjadi kesalahan, periksa log.")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if not user_id:
        return await Tm.edit(
            "<b>Balas pesan pengguna atau berikan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delreseller = await get_seles()
    if user.id not in delreseller:
        return await Tm.edit("Tidak Ditemukan.")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await Tm.edit(f"{user.mention} berhasil dihapus")
    else:
        await Tm.delete()
        await message.reply_text("Terjadi kesalahan, periksa log.")


async def get_seles_user(cliebt, message):
    text = ""
    count = 0
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            user = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{user}\n"
    if not text:
        await message.reply_text("Tidak Ada Pengguna Yang Ditemukan")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    try:
        user_id = int(message.text.split()[1])
        duration = int(message.text.split()[2])
    except (IndexError, ValueError) as error:
        return await message.reply(error)
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=duration)
    await set_expired_date(user_id, expire_date)
    await message.reply(f"User {user_id} telah diaktifkan selama {duration} hari.")


async def expired_cek(client, message):
    user_id = int(message.text.split()[1])
    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"User {user_id} belum diaktifkan.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(
            f"User {user_id} aktif hingga {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. Sisa waktu aktif {remaining_days} hari."
        )
