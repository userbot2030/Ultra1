import re

from pyrogram.types import *

from PyroUbot import *


async def help_cmd(client, message):
    if len(message.command) < 2:
        try:
            x = await client.get_inline_bot_results(bot.me.username, "user_help")
            return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            return await message.reply(error)
    else:
        if message.command[1] in HELP_COMMANDS:
            return await message.reply(HELP_COMMANDS[message.command[1]].__HELP__)
        else:
            return await message.reply(
                f"<b>❌ ᴍᴏᴅᴜʟᴇs {message.command[1]} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>"
            )


async def menu_inline(client, inline_query):
    msg = f"<b>✣ ᴍᴇɴᴜ ɪɴʟɪɴᴇ <a href=tg://user?id={inline_query.from_user.id}>{inline_query.from_user.first_name} {inline_query.from_user.last_name or ''}</a>\n\n★ ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}</b>"
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, HELP_COMMANDS, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


async def menu_callback(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    top_text = f"<b>✣ ᴍᴇɴᴜ ɪɴʟɪɴᴇ <a href=tg://user?id={callback_query.from_user.id}>{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}</a>\n\n► ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}</b>"
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = HELP_COMMANDS[module].__HELP__
        button = [[InlineKeyboardButton("• ᴋᴇᴍʙᴀʟɪ •", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    if prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
