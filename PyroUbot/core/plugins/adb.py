import asyncio
import importlib
from datetime import datetime, timedelta
from io import BytesIO

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pytz import timezone

from .. import *


async def need_api(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [InlineKeyboardButton("➡️ Lanjutkan", callback_data="add_ubot")],
    ]
    await callback_query.message.delete()
    return await bot.send_message(
        user_id,
        """
<b>✅ Untuk Membuat UserBot Siapakah Bahan Berikut

    • <code>API_ID</code>: Dapatkan Dari my.telegram.org
    • <code>API_HASH</code>: Dapatkan Dari my.telegram.org
    • <code>PHONE_NUMBER</code>: Nomer Hp Akun Telegram

☑️ Jika Sudah Tersedia Silahkan Klik Tomboi Dibawah</b>
""",
    )


async def bikin_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    PREM_ID = await get_prem()
    ID_SELES = await get_seles()
    if len(ubot._ubot) == MAX_BOT:
        buttons = [
            [InlineKeyboardButton("🗑️ Tutup 🗑️", callback_data="0_cls")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            f"""
<b>❌ TIDAK BISA MEMBUAT USERBOT!</b>

<b>📚 KARENA MAKSIMAL USERBOT ADALAH {MAX_UBOT} TELAH TERCAPAI</b>

<b>☎️ SILAHKAN HUBUNGI: <a href=t.me/T0M1_X>ADMIN</a> JIKA MAU DIBUATKAN BOT SEPERTI SAYA</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif user_id not in PREM_ID:
        buttons = [[InlineKeyboardButton("✅ KONFIRMASI", callback_data="confirm")]]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            TEXT_PAYMENT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    try:
        await callback_query.message.delete()
        api = await bot.ask(
            user_id,
            (
                "<b>Silahkan Masukkan API_ID</b>\n"
                "\n<b>Gunakan /cancel untuk Membatalkan Proses Membuat Userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "waktu Telah Habis")
    if await is_cancel(callback_query, api.text):
        return
    api_ids = api.text
    try:
        hash = await bot.ask(
            user_id,
            (
                "<b>Silahkan Masukkan API_HASH</b>\n"
                "\n<b>Gunakan /cancel untuk Membatalkan Proses Membuat Userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "waktu Telah Habis")
    if await is_cancel(callback_query, hash.text):
        return
    api_hashs = hash.text
    try:
        phone = await bot.ask(
            user_id,
            (
                "<b>Silahkan Masukkan Nomor Telepon Telegram Anda Dengan Format Kode Negara.\nContoh: +628xxxxxxx</b>\n"
                "\n<b>Gunakan /cancel untuk Membatalkan Proses Membuat Userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "waktu Telah Habis")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=api_ids,
        api_hash=api_hashs,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "<b>Mengirim Kode OTP...</b>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    try:
        sent_code = {
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>Akun Telegram</a> Resmi",
            SentCodeType.SMS: "SMS Anda",
            SentCodeType.CALL: "Panggilan Telpon",
            SentCodeType.FLASH_CALL: "panggilan kilat telepon",
            SentCodeType.FRAGMENT_SMS: "Fragment SMS",
            SentCodeType.EMAIL_CODE: "Email Anda",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                f"<b>Silakan Periksa Kode OTP Dari {sent_code[code.type]}. Kirim Kode OTP Ke Sini Setelah Membaca Format Di Bawah Ini.</b>\n"
                "\nJika Kode OTP Adalah <code>12345</code> Tolong <b>[ TAMBAHKAN SPASI ]</b> kirimkan Seperti ini <code>1 2 3 4 5</code>\n"
                "\n<b>Gunakan /cancel Untuk Membatalkan Proses Membuat Userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "waktu Telah Habis")
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "<b>Akun anda Telah mengaktifkan Verifikasi Dua Langkah. Silahkan Kirimkan Passwordnya.\n\nGunakan /cancel untuk Membatalkan Proses Membuat Userbot</b>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "Batas waktu tercapai 5 menit.")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    await new_client.start()
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=api_ids,
        api_hash=api_hashs,
        session_string=session_string,
    )
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    text_done = f"<b>🔥 {bot.me.mention} Berhasil Diaktifkan Di Akun: <a href=tg://openmessage?user_id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> > <code>{new_client.me.id}</code></b> "
    await bot.send_message(
        user_id,
        text_done,
        disable_web_page_preview=True,
    )
    now = datetime.now(timezone("Asia/Jakarta"))
    date = now.strftime("%d-%m-%Y")
    expire_date = now + timedelta(days=30)
    await set_expired_date(new_client.me.id, expire_date)
    get_exp = await get_expired_date(new_client.me.id)
    exp = get_exp.strftime("%d-%m-%Y")
    buttons = [
        [
            InlineKeyboardButton(
                "🧑‍💻 Pembuat Userbot 🧑‍💻",
                url=f"tg://openmessage?user_id={callback_query.from_user.id}",
            )
        ],
        [
            InlineKeyboardButton(
                "📁 Hapus Dari Database 📁",
                callback_data=f"del_ubot {new_client.me.id}",
            )
        ],
    ]
    await bot.send_message(
        LOGS_MAKER_UBOT,
        f"{text_done}\n<b>🗓️ Mulai: {date}</b>\n<b>🗓️ Akhir: {exp}</b>",
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )
    try:
        await new_client.join_chat("SaikiSupport")
    except UserAlreadyParticipant:
        pass
    if callback_query.from_user.id in ID_SELES:
        return
    else:
        await remove_prem(callback_query.from_user.id)


async def cek_ubot(client, message):
    if not message.from_user.id == OWNER_ID:
        return
    count = 0
    user = ""
    for X in ubot._ubot:
        count += 1
        user += f"""
❏ USERBOT KE {count}
 ├ AKUN: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a> 
 ╰ ID: <code>{X.me.id}</code>
"""
    if int(len(str(user))) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "userbot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")


async def hapus_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"<a href=tg://user?id={get_id}>{show.first_name} {show.last_name or ''}</a>"
    except BadRequest:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"<a href=tg://user?id={get_id}>Userbot</a>"
    for X in ubot._ubot:
        if get_id == X.me.id:
            ubot._ubot.remove(X)
            get_my_id.remove(get_id)
            await X.log_out()
            await rm_all(get_id)
            await remove_ubot(get_id)
            await rem_expired_date(get_id)
            await bot.send_message(
                OWNER_ID, f"<b> ✅ {get_mention} Berhasil Dihapus Dari Database</b>"
            )
            return await bot.send_message(get_id, "<b>💬 MASA AKTIF ANDA TELAH BERAKHIR")


async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<b>Membatalkan Proses!</b>"
        )
        return True
    return False
