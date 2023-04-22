import asyncio
from gc import get_objects

from pyrogram.enums import MessagesFilter
from pyrogram.errors import FloodWait
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from .. import *


async def copy_bot_msg(client, message):
    msg = message.reply_to_message or message
    Tm = await message.reply("Tunggu sebentar")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [link_konten_telegram]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
            await get.copy(message.chat.id, reply_to_message_id=msg.id)
            await Tm.delete()
        except Exception as error:
            await Tm.edit(error)
    else:
        await Tm.edit("masukkin link yang valid")


async def copy_ubot_msg(client, message):
    msg = message.reply_to_message or message
    Tm = await message.reply("Tunggu sebentar")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [link_konten_telegram]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
            await get.copy(message.chat.id, reply_to_message_id=msg.id)
            await Tm.delete()
        except Exception:
            try:
                text = f"get_msg {id(message)}"
                x = await client.get_inline_bot_results(bot.me.username, text)
                await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception:
                await client.send_message(
                    message.chat.id,
                    f"<b>🔒 Konten Yang Mau Diambil Bersifat Restricted\n\n👉🏻 <a href=https://t.me/{bot.me.username}?start=copyMsg_{id(message)}>Klik Disini</a> Untuk Membuka Konten Restricted</b>",
                    reply_to_message_id=msg.id,
                )
            await Tm.delete()
    else:
        await Tm.edit("masukkin link yang valid")


async def copy_inline_msg(client, inline_query):
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get message!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="🔐 Buka Konten Restricted 🔐",
                                    callback_data=f"copymsg_{int(inline_query.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        "<b>🔒 Konten Yang Mau Diambil Bersifat Restricted\n\n✅ Klik Tombol Dibawah Untuk Membuka Konten Restricted</b>"
                    ),
                )
            )
        ],
    )


async def copy_callback_msg(client, callback_query):
    try:
        q = int(callback_query.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        if not callback_query.from_user.id == m.from_user.id:
            return await callback_query.answer(
                f"❌ TOMBOL INI BUKAN UNTUK MU {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
                True,
            )
        else:
            await m._client.unblock_user(bot.me.username)
            await callback_query.edit_message_text("<b>Tunggu sebentar")
            copy = await m._client.send_message(
                bot.me.username, f"/copy {m.text.split()[1]}"
            )
            await asyncio.sleep(1.5)
            await copy.delete()
            async for get in m._client.search_messages(bot.me.username, limit=1):
                await m._client.copy_message(m.chat.id, bot.me.username, get.id)
                await callback_query.edit_message_text(
                    "<b>✅ Copy Message Berhasil Dilakukan"
                )
                await get.delete()
    except Exception as error:
        await callback_query.edit_message_text(f"<b>❌ ERROR:</b> <code>{error}</code>")


async def take_msg_cmd(client, message):
    results = {
        "photo": MessagesFilter.PHOTO,
        "audio": MessagesFilter.AUDIO,
        "video": MessagesFilter.VIDEO,
        "dokumen": MessagesFilter.DOCUMENT,
    }
    TM = await message.reply("Tunggu Sebentar")
    if len(message.command) < 5:
        return await TM.edit(
            f"<code><b>{message.text} from_chat msg_filter msg_limit to_chat</code></b>"
        )
    else:
        if message.command[2] in results:
            msg_ = results[message.command[2]]
        else:
            return await TM.edit(
                f"❌ msg_filter {message.command[2]} tidak bisa diproses\n\n✅ msg_filter yang tersedia adalah: <code>dokumen</code> <code>photo</code> <code>audio</code> <code>video</code>"
            )
    await TM.edit("Sedang Memproses")
    done = 0
    async for msg in client.search_messages(
        message.command[1], filter=msg_, limit=int(message.command[3])
    ):
        try:
            await msg.copy(message.command[4])
            done += 1
            await asyncio.sleep(0.3)
        except FloodWait as flood:
            await asyncio.sleep(flood.value)
    await TM.delete()
    return await message.reply(f"✅ {done} {message.command[2]} telah berhasil diambil")
