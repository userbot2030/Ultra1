from importlib import import_module
from platform import python_version

from pyrogram import __version__, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import bot, ubot
from PyroUbot.config import LOGS_MAKER_UBOT
from PyroUbot.core.helpers.text import HelpText
from PyroUbot.modules import loadModule

HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"PyroUbot.modules.{mod}")
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDS[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module
    print(f"[🤖 @{bot.me.username} 🤖] [🔥 TELAH BERHASIL DIAKTIFKAN! 🔥]")
    await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>📁 ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS) + len(HelpText)}</b>
<b>📘 ᴘʏᴛʜᴏɴ: {python_version()}</b>
<b>📙 ᴘʏʀᴏɢʀᴀᴍ: {__version__}</b>
<b>👤 ᴜsᴇʀʙᴏᴛ: {len(ubot._ubot)}</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 TUTUP 🗑", callback_data="0_cls")]],
        ),
    )


@bot.on_callback_query(filters.regex("0_cls"))
async def now(_, cq):
    await cq.message.delete()
