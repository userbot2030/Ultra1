from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


class Button:
    def admin():
        menu_button = [
            [
                InlineKeyboardButton("Global", callback_data="menu_help admin_gban"),
                InlineKeyboardButton(
                    "Restrict", callback_data="menu_help admin_restrict"
                ),
            ],
            [InlineKeyboardButton("• Kembali •", callback_data="help_back")],
        ]
        back_button = [
            [InlineKeyboardButton("• Kembali •", callback_data="menu_help admin_back")]
        ]
        return [menu_button, back_button]

    def sticker():
        menu_button = [
            [
                InlineKeyboardButton("Kang", callback_data="menu_help sticker_kang"),
                InlineKeyboardButton(
                    "Memify", callback_data="menu_help sticker_memify"
                ),
            ],
            [
                InlineKeyboardButton("Memes", callback_data="menu_help sticker_memes"),
                InlineKeyboardButton(
                    "Quotly", callback_data="menu_help sticker_quotly"
                ),
            ],
            [
                InlineKeyboardButton("Tiny", callback_data="menu_help sticker_tiny"),
            ],
            [InlineKeyboardButton("• Kembali •", callback_data="help_back")],
        ]
        back_button = [
            [
                InlineKeyboardButton(
                    "• Kembali •", callback_data="menu_help sticker_back"
                )
            ]
        ]
        return [menu_button, back_button]

    def start():
        button = [
            [InlineKeyboardButton("🔥 BUAT USERBOT 🔥", callback_data="bahan")],
            [
                InlineKeyboardButton("💬 BANTUAN", callback_data="help_back"),
                InlineKeyboardButton("SUPPORT 💬", callback_data="support"),
            ],
        ]
        return button

    def translate():
        button = [
            [
                InlineKeyboardButton(
                    "• LANG_CODE •", url="https://graph.org/LANG-CODE-11-26"
                )
            ],
            [
                InlineKeyboardButton("• KEMBALI •", callback_data="help_back"),
            ],
        ]
        return button


class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = client._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"Anda belum order @{bot.me.username}",
                                input_message_content=InputTextMessageContent(
                                    f"Silahkan Order Di @{bot.me.username} Dulu Biar Bisa Menggunakan Inline Ini"
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
            users = client._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"Makanya Order Userbot @{bot.me.username} Dulu Biar Bisa Klik Tombol Ini",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper
