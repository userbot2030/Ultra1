from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="🗑️ ᴛᴜᴛᴜᴘ",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def start():
        button = [
            [InlineKeyboardButton("🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥", callback_data="bahan")],
            [
                InlineKeyboardButton("💬 ʙᴀɴᴛᴜᴀɴ", callback_data="help_back"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 💬", callback_data="support"),
            ],
        ]
        return button


class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴏʀᴅᴇʀ @{bot.me.username}",
                                input_message_content=InputTextMessageContent(
                                    f"sɪʟᴀʜᴋᴀɴ ᴏʀᴅᴇʀ ᴅɪ @{bot.me.username} ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ɪɴʟɪɴᴇ ɪɴɪ"
                                ),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"ᴍᴀᴋᴀɴʏᴀ ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ @{bot.me.username} ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper


async def create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    if "|" not in m.text.split(None, 1)[1]:
        msg = []
        for X in m.text.split(None, 1)[1].split():
            keyboard.append(
                InlineKeyboardButton(X.split(":", 1)[0], url=X.split(":", 1)[1])
            )
            msg.append(X.split(":")[0])
        buttons.add(*keyboard)
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            msg_text = ""
            for Z in msg:
                msg_text += f"{Z} "
            text = msg_text
    else:
        for X in m.text.split("|", 1)[1].split():
            keyboard.append(
                InlineKeyboardButton(X.split(":", 1)[0], url=X.split(":", 1)[1])
            )
        buttons.add(*keyboard)
        text = m.text.split("|", 1)[0].split(None, 1)[1]
    return buttons, text


async def gcast_create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    for X in m.text.split("||", 1)[1].split():
        keyboard.append(
            InlineKeyboardButton(X.split(":", 1)[0], url=X.split(":", 1)[1])
        )
    buttons.add(*keyboard)
    text_button = m.text.split("||", 1)[0].split(None, 1)[1]
    return buttons, text_button


async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    for X in text.split("|", 1)[1].split():
        keyboard.append(
            InlineKeyboardButton(X.split("::", 1)[0], url=X.split(":", 1)[1])
        )
    buttons.add(*keyboard)
    text_button = text.split("|", 1)[0]
    return buttons, text_button
