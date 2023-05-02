from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


class Button:
    def admin():
        menu_button = [
            [
                InlineKeyboardButton("ɢʟᴏʙᴀʟ", callback_data="menu_help admin_gban"),
                InlineKeyboardButton(
                    "ʀᴇsᴛʀɪᴄᴛ", callback_data="menu_help admin_restrict"
                ),
            ],
            [InlineKeyboardButton("• ᴋᴇᴍʙᴀʟɪ' •", callback_data="help_back")],
        ]
        back_button = [
            [InlineKeyboardButton("• ᴋᴇᴍʙᴀʟɪ •", callback_data="menu_help admin_back")]
        ]
        return [menu_button, back_button]

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

    def sticker():
        menu_button = [
            [
                InlineKeyboardButton("ᴋᴀɴɢ", callback_data="menu_help sticker_kang"),
                InlineKeyboardButton(
                    "ᴍᴇᴍɪꜰʏ", callback_data="menu_help sticker_memify"
                ),
            ],
            [
                InlineKeyboardButton("ᴍᴇᴍᴇs", callback_data="menu_help sticker_memes"),
                InlineKeyboardButton(
                    "ǫᴜᴏᴛʟʏ", callback_data="menu_help sticker_quotly"
                ),
            ],
            [
                InlineKeyboardButton("ᴛɪɴʏ", callback_data="menu_help sticker_tiny"),
            ],
            [InlineKeyboardButton("• ᴋᴇᴍʙᴀʟɪ •", callback_data="help_back")],
        ]
        back_button = [
            [
                InlineKeyboardButton(
                    "• ᴋᴇᴍʙᴀʟɪ •", callback_data="menu_help sticker_back"
                )
            ]
        ]
        return [menu_button, back_button]

    def start():
        button = [
            [InlineKeyboardButton("🔥 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ 🔥", callback_data="bahan")],
            [
                InlineKeyboardButton("💬 ʙᴀɴᴛᴜᴀɴ", callback_data="help_back"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ 💬", callback_data="support"),
            ],
        ]
        return button

    def translate():
        button = [
            [
                InlineKeyboardButton(
                    "• ʟᴀɴɢ_ᴄᴏᴅᴇ •", url="https://graph.org/LANG-CODE-11-26"
                )
            ],
            [
                InlineKeyboardButton("• ᴋᴇᴍʙᴀʟɪ •", callback_data="help_back"),
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
