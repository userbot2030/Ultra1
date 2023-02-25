from pyrogram.types import InlineKeyboardButton, WebAppInfo


class Button:
    def admin():
        menu_button = [
            [
                InlineKeyboardButton("GLOBAL", callback_data="menu_help admin_gban"),
                InlineKeyboardButton(
                    "RESTRICT", callback_data="menu_help admin_restrict"
                ),
            ],
            [InlineKeyboardButton("• KEMBALI •", callback_data="help_back")],
        ]
        back_button = [
            [InlineKeyboardButton("• KEMBALI •", callback_data="menu_help admin_back")]
        ]
        return [menu_button, back_button]

    def sticker():
        menu_button = [
            [
                InlineKeyboardButton("KANG", callback_data="menu_help sticker_kang"),
                InlineKeyboardButton(
                    "MEMIFY", callback_data="menu_help sticker_memify"
                ),
            ],
            [
                InlineKeyboardButton("MAMES", callback_data="menu_help sticker_memes"),
                InlineKeyboardButton(
                    "QUOTLY", callback_data="menu_help sticker_quotly"
                ),
            ],
            [
                InlineKeyboardButton("TINY", callback_data="menu_help sticker_tiny"),
            ],
            [InlineKeyboardButton("• KEMBALI •", callback_data="help_back")],
        ]
        back_button = [
            [
                InlineKeyboardButton(
                    "• KEMBALI •", callback_data="menu_help sticker_back"
                )
            ]
        ]
        return [menu_button, back_button]

    def start():
        button = [
            [InlineKeyboardButton("🔥 BUAT USERBOT 🔥", callback_data="add_ubot")],
            [
                InlineKeyboardButton(
                    text="🎁 DONATE",
                    web_app=WebAppInfo(url="https://graph.org/DONATE-02-10-2"),
                ),
                InlineKeyboardButton("SUPPORT 💬", callback_data="support"),
            ],
        ]
        return button

    def translate():
        button = [
            [
                InlineKeyboardButton("• KEMBALI", callback_data="help_back"),
                InlineKeyboardButton(
                    "LANG_CODE •",
                    url="https://graph.org/LANG-CODE-11-26",
                ),
            ]
        ]
        return button
