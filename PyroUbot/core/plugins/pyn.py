import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *

CONFIRM_PAYMENT = []


async def confirm_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    CONFIRM_PAYMENT.append(get.id)
    try:
        button = [[InlineKeyboardButton("❌ ʙᴀᴛᴀʟᴋᴀɴ", callback_data=f"home {user_id}")]]
        await callback_query.message.delete()
        pesan = await bot.ask(
            user_id,
            f"<b>💬 sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍᴋᴀɴ ʙᴜᴋᴛɪ sᴄʀᴇᴇɴsʜᴏᴛ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ: {full_name}</b>",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=300,
        )
    except asyncio.TimeoutError as out:
        if get.id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(get.id)
            return await pesan.request.edit("ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪs")
    if get.id in CONFIRM_PAYMENT:
        if not pesan.photo:
            CONFIRM_PAYMENT.remove(get.id)
            await pesan.request.edit(
                f"<b>💬 sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍᴋᴀɴ ʙᴜᴋᴛɪ sᴄʀᴇᴇɴsʜᴏᴛ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ: {full_name}</b>",
            )
            buttons = [[InlineKeyboardButton("✅ ᴋᴏɴꜰɪʀᴍᴀsɪ", callback_data="confirm")]]
            return await bot.send_message(
                user_id,
                """
<b>❌ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴅɪᴘʀᴏsᴇs</b>

<b>💬 ʜᴀʀᴀᴘ ᴋɪʀɪᴍᴋᴀɴ sᴄʀᴇᴇɴsʜᴏᴛ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ ʏᴀɴɢ ᴠᴀʟɪᴅ</b>

<b>✅ sɪʟᴀʜᴋᴀɴ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜʟᴀɴɢ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
""",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        elif pesan.photo:
            buttons = [
                [
                    InlineKeyboardButton("✅ ʏᴇs ", callback_data=f"success {user_id}"),
                    InlineKeyboardButton("ɴᴏᴛ ❌", callback_data=f"failed {user_id}"),
                ],
                [
                    InlineKeyboardButton(
                        "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏꜰɪʟ 👤", callback_data=f"profil {user_id}"
                    )
                ],
            ]
            await pesan.copy(
                OWNER_ID,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            CONFIRM_PAYMENT.remove(get.id)
            await pesan.request.edit(
                f"<b>💬 sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍᴋᴀɴ ʙᴜᴋᴛɪ sᴄʀᴇᴇɴsʜᴏᴛ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ: {full_name}</b>",
            )
            return await bot.send_message(
                user_id,
                f"""
<b>💬 ʙᴀɪᴋ {full_name} sɪʟᴀʜᴋᴀɴ ᴅɪᴛᴜɴɢɢᴜ ᴅᴀɴ ᴊᴀɴɢᴀɴ sᴘᴀᴍ ʏᴀ</b>

<b>🏦 ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴅɪᴋᴏɴꜰɪʀᴍᴀsɪ sᴇᴛᴇʟᴀʜ 1-12 ᴊᴀᴍ ᴋᴇʀᴊᴀ</b>
""",
            )


async def tambah_or_kurang(client, callback_query):
    query = callback_query.data.split()
    MONTH = 1
    buttons = [
            [
                InlineKeyboardButton("-1 ʙᴜʟᴀɴ", callback_data="kurang -1"),
                InlineKeyboardButton("+1 ʙᴜʟᴀɴ", callback_data="tambah +1"),
            ],
            [InlineKeyboardButton("✅ ᴋᴏɴꜰɪʀᴍᴀsɪ ✅", callback_data="confirm")],
        ]
    if query[0] == "kurang":
        if int(query[1]) == "-1":
            if MONTH == 12:
                MONTH = 1
            else:
                MONTH -= 1
            TOTAL = HARGA * MONTH
    elif query[0] == "tambah":
        if int(query[1]) == "+1":
            if MONTH == 1:
                MONTH = 12
            else:
                MONTH += 1
            TOTAL = HARGA * MONTH
    await callback_query.edit_message_text(TEXT_PAYMENT.format(HARGA, TOTAL, MONTH), reply_markup=InlineKeyboardMarkup(buttons))


async def success_failed_home_callback(client, callback_query):
    query = callback_query.data.split()
    get_user = await bot.get_users(query[1])
    if query[0] == "success":
        buttons = [
            [InlineKeyboardButton("🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥", callback_data="bahan")],
        ]
        await bot.send_message(
            get_user.id,
            """
<b>✅ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ ʙᴇʀʜᴀsɪʟ ᴅɪᴋᴏɴꜰɪʀᴍᴀsɪ</b>

<b>💬 sᴇᴋᴀʀᴀɴɢ ᴀɴᴅᴀ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        buttons_success = [
            [
                InlineKeyboardButton(
                    "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏꜰɪʟ 👤", callback_data=f"profil {get_user.id}"
                )
            ],
        ]
        await add_prem(get_user.id)
        return await bot.send_message(
            OWNER_ID,
            f"""
<b>✅ {get_user.first_name} {get_user.last_name or ''} ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴀɴɢɢᴏᴛᴀ ᴘʀᴇᴍɪᴜᴍ</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons_success),
        )
    if query[0] == "failed":
        buttons = [
            [InlineKeyboardButton("💳 ʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ 💳", callback_data="add_ubot")],
        ]
        await bot.send_message(
            get_user.id,
            """
<b>❌ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪᴋᴏɴꜰɪʀᴍᴀsɪ</b>

<b>💬 sɪʟᴀʜᴋᴀɴ ʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        buttons_failed = [
            [
                InlineKeyboardButton(
                    "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏꜰɪʟ 👤", callback_data=f"profil {get_user.id}"
                )
            ],
        ]
        return await bot.send_message(
            OWNER_ID,
            f"""
<b>❌ {get_user.first_name} {get_user.last_name or ''} ᴛɪᴅᴀᴋ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴀɴɢɢᴏᴛᴀ ᴘʀᴇᴍɪᴜᴍ</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons_failed),
        )
    if query[0] == "home":
        if get_user.id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(get_user.id)
            buttons_home = Button.start()
            await callback_query.message.delete()
            return await bot.send_message(
                get_user.id,
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons_home),
            )
