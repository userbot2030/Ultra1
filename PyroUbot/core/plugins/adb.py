import asyncio
from datetime import datetime, timedelta

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pytz import timezone

from PyroUbot import *


async def need_api(client, callback_query):
    user_id = callback_query.from_user.id
    PREM_ID = await get_prem()
    if user_id not in PREM_ID:
        buttons = [[InlineKeyboardButton("✅ ᴋᴏɴꜰɪʀᴍᴀsɪ", callback_data="confirm")]]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            TEXT_PAYMENT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [
            [InlineKeyboardButton("➡️ ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="add_ubot")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            """
<b>✅ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ sɪᴀᴘᴋᴀɴ ʙᴀʜᴀɴ ʙᴇʀɪᴋᴜᴛ

    • <code>ᴀᴘɪ_ɪᴅ</code>: ᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀʀɪ my.telegram.org
    • <code>ᴀᴘɪ_ʜᴀsʜ</code>: ᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀʀɪ my.telegram.org
    • <code>ᴘʜᴏɴᴇ_ɴᴜᴍʙᴇʀ</code>: ɴᴏᴍᴇʀ ʜᴘ ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ

☑️ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴛᴇʀsᴇᴅɪᴀ sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏɪ ᴅɪʙᴀᴡᴀʜ</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


async def bikin_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    ID_SELES = await get_seles()
    if len(ubot._ubot) == MAX_BOT:
        buttons = [
            [InlineKeyboardButton("🗑️ Tutup 🗑️", callback_data="0_cls")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            f"""
<b>❌ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ!</b>

<b>📚 ᴋᴀʀᴇɴᴀ ᴍᴀᴋsɪᴍᴀʟ ᴜsᴇʀʙᴏᴛ ᴀᴅᴀʟᴀʜ {MAX_UBOT} ᴛᴇʟᴀʜ ᴛᴇʀᴄᴀᴘᴀɪ</b>

<b>☎️ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ: <a href=t.me/T0M1_X>ᴀᴅᴍɪɴ</a> ᴊɪᴋᴀ ᴍᴀᴜ ᴅɪʙᴜᴀᴛᴋᴀɴ ʙᴏᴛ sᴇᴘᴇʀᴛɪ sᴀʏᴀ</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    try:
        await callback_query.message.delete()
        api = await bot.ask(
            user_id,
            (
                "<b>sɪʟᴀʜᴋᴀɴ ᴍᴀsᴜᴋᴋᴀɴ ᴀᴘɪ_ɪᴅ</b>\n"
                "\n<b>ɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "ᴡᴀᴋᴛᴜ ᴛᴇʟᴀʜ ʜᴀʙɪs")
    if await is_cancel(callback_query, api.text):
        return
    api_ids = api.text
    try:
        hash = await bot.ask(
            user_id,
            (
                "<b>sɪʟᴀʜᴋᴀɴ ᴍᴀsᴜᴋᴋᴀɴ ᴀᴘɪ_ʜᴀsʜ</b>\n"
                "\n<b>ɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴘʀᴏsᴇs ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "ᴡᴀᴋᴛᴜ ᴛᴇʟᴀʜ ʜᴀʙɪs")
    if await is_cancel(callback_query, hash.text):
        return
    api_hashs = hash.text
    try:
        phone = await bot.ask(
            user_id,
            (
                "<b>sɪʟᴀʜᴋᴀɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴏᴍᴏʀ ᴛᴇʟᴇᴘᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅᴀ ᴅᴇɴɢᴀɴ ꜰᴏʀᴍᴀᴛ ᴋᴏᴅᴇ ɴᴇɢᴀʀᴀ.\nᴄᴏɴᴛᴏʜ: +628xxxxxxx</b>\n"
                "\n<b>ɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>"
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
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ</a> ʀᴇsᴍɪ",
            SentCodeType.SMS: "sᴍs ᴀɴᴅᴀ",
            SentCodeType.CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴛᴇʟᴘᴏɴ",
            SentCodeType.FLASH_CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴋɪʟᴀᴛ ᴛᴇʟᴇᴘᴏɴ",
            SentCodeType.FRAGMENT_SMS: "ꜰʀᴀɢᴍᴇɴᴛ sᴍs",
            SentCodeType.EMAIL_CODE: "ᴇᴍᴀɪʟ ᴀɴᴅᴀ",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                f"<b>sɪʟᴀᴋᴀɴ ᴘᴇʀɪᴋsᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴅᴀʀɪ {sent_code[code.type]}. ᴋɪʀɪᴍ ᴋᴏᴅᴇ ᴏᴛᴘ ᴋᴇ sɪɴɪ sᴇᴛᴇʟᴀʜ ᴍᴇᴍʙᴀᴄᴀ ꜰᴏʀᴍᴀᴛ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ.</b>\n"
                "\nᴊɪᴋᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴀᴅᴀʟᴀʜ <ᴄᴏᴅᴇ>12345</ᴄᴏᴅᴇ> ᴛᴏʟᴏɴɢ <b>[ ᴛᴀᴍʙᴀʜᴋᴀɴ sᴘᴀsɪ ]</b> ᴋɪʀɪᴍᴋᴀɴ sᴇᴘᴇʀᴛɪ ɪɴɪ <code>1 2 3 4 5</code>\ɴ"
                "\n<b>ɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "ᴡᴀᴋᴛᴜ ᴛᴇʟᴀʜ ʜᴀʙɪs")
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
                "<b>ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇɴɢᴀᴋᴛɪꜰᴋᴀɴ ᴠᴇʀɪꜰɪᴋᴀsɪ ᴅᴜᴀ ʟᴀɴɢᴋᴀʜ. sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍᴋᴀɴ ᴘᴀssᴡᴏʀᴅɴʏᴀ.\n\nɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>",
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
    text_done = f"<b>🔥 {bot.me.mention} ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ ᴅɪ ᴀᴋᴜɴ: <a href=tg://openmessage?user_id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> > <code>{new_client.me.id}</code></b> "
    await bot.send_message(
        user_id,
        text_done,
        disable_web_page_preview=True,
    )
    try:
        await new_client.join_chat("PremUbotCH")
    except UserAlreadyParticipant:
        pass
    now = datetime.now(timezone("Asia/Jakarta"))
    date = now + timedelta(days=30)
    expire = date.strftime("%d-%m-%Y")
    await set_expired_date(new_client.me.id, date)
    buttons = [
        [
            InlineKeyboardButton(
                "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                callback_data=f"cek_masa_aktif {new_client.me.id}",
            )
        ],
    ]
    await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
<b> ├ ɪᴅ:</b> <code>{new_client.me.id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ</b> <code>{expire}</code>
""",
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )
    if callback_query.from_user.id not in ID_SELES:
        await remove_prem(callback_query.from_user.id)
    await install_user_id()


async def cek_ubot(client, message):
    if not message.from_user.id == OWNER_ID:
        return
    count = 0
    for X in ubot._ubot:
        if not X.me.id == ubot.me.id:
            count += 1
            expired_date = await get_expired_date(X.me.id)
            user = f"""
<b>❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{count}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a> 
<b> ├ ɪᴅ:</b> <code>{X.me.id}</code>
<b> ╰ ᴇxᴘɪʀᴇᴅ</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""
            buttons = [
                [
                    InlineKeyboardButton(
                        "📁 ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ 📁",
                        callback_data=f"del_ubot {X.me.id}",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📁 ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ 📁",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
            await message.reply(user, reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(4)


async def cek_userbot_expired(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    now = datetime.now(timezone("Asia/Jakarta"))
    expired = await get_expired_date(user_id)
    xxxx = (expired - now).days
    return await callback_query.answer(
        f"⏳ ᴛɪɴɢɢᴀʟ {xxxx} ʜᴀʀɪ ʟᴀɢɪ",
        True,
    )


async def hapus_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"<a href=tg://user?id={get_id}>{show.first_name} {show.last_name or ''}</a>"
    except BadRequest:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"<a href=tg://user?id={get_id}>Userbot</a>"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            await X.send_message(bot.me.username, "ping")
            await X.log_out()
            ubot._ubot.remove(X)
            await rm_all(get_id)
            X._get_my_id.remove(get_id)
            await remove_ubot(get_id)
            await rem_expired_date(get_id)
            await bot.send_message(
                OWNER_ID, f"<b> ✅ {get_mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ</b>"
            )
            await msg.delete()
            return await bot.send_message(get_id, "<b>💬 ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ʙᴇʀᴀᴋʜɪʀ")


async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<b>ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs!</b>"
        )
        return True
    return False
