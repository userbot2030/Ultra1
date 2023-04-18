from datetime import datetime, timedelta

from pytz import timezone

from .. import *



# ========================== #
    # 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #



async def prem_user(client, message):
    if message.from_user.id not in await get_seles():
        return
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


async def get_prem_user(cliebt, message):
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
    # 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #
        
async def seles_user(client, message):
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
    Tm = await message.reply("<b>Processing . . .</b>")
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
     # 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼 #
# ========================== #


async def expired_adf(client, message):
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

