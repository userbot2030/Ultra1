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
        [InlineKeyboardButton("➡️ ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="add_ubot")],
    ]
    await callback_query.message.delete()
    return await bot.send_message(user_id, MSG.NEED_API())


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
            MSG.LIMIT_UBOT(MAX_UBOT),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif user_id not in PREM_ID:
        buttons = [[InlineKeyboardButton("✅ ᴋᴏɴꜰɪʀᴍᴀsɪ", callback_data="confirm")]]
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
            MSG.API_ID(),
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
            MSG.API_hASH(),
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
            MSG.PHONE_number(),
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
            MSG.OTP(send_code, code.type),
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
                MSG.PASSWOARD()
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
    await bot.send_message(
        user_id,
        MSG.ACTIVE(bot, new_client),
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
                "📁 ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ 📁",
                callback_data=f"del_ubot {new_client.me.id}",
            )
        ],
    ]
    await bot.send_message(
        LOGS_MAKER_UBOT,
        f"{MSG.ACTIVE(bot, new_client)} {MSG.DATE(date, exp)},
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )
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
        user += MSG.LIST_UBOT(count, x)
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
            await X.log_out()
            ubot._ubot.remove(X)
            await rm_all(get_id)
            get_my_id.remove(get_id)
            await remove_ubot(get_id)
            await rem_expired_date(get_id)
            await bot.send_message(
                OWNER_ID, f"<b> ✅ {get_mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ</b>"
            )
            return await bot.send_message(get_id, "<b>💬 ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ʙᴇʀᴀᴋʜɪʀ")


async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<b>ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs!</b>"
        )
        return True
    return False
