import io
import os
import asyncio

import openai
from aiohttp import ClientSession
from PyroUbot import *


def get_text(message):
    if message.reply_to_message:
        if len(message.command) < 2:
            text = message.reply_to_message.text or message.reply_to_message.caption
        else:
            text = (
                (message.reply_to_message.text or message.reply_to_message.caption)
                + "\n\n"
                + message.text.split(None, 1)[1]
            )
    else:
        if len(message.command) < 2:
            text = ""
        else:
            text = message.text.split(None, 1)[1]
    return text


async def ai_cmd(client, message):
    Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs...</code>", quote=True)
    args = get_text(message)
    if not args:
        return await Tm.edit(f"<b><code>{message.text}</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]</b>")
    answer = ""
    openai.aiosession.set(ClientSession())
    openai.api_key = random.choice(OPENAI_KEY)
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": args}],
            temperature=0.7,
            stream=True,
        )
        async for chunk in response:
            try:
                if not chunk.choices[0].delta or chunk.choices[0].delta.get("role"):
                    continue
                answer += chunk.choices[0].delta.content
                await Tm.edit(answer + ",,", parse_mode=ParseMode.MARKDOWN)
                await asyncio.sleep(1.5)
            except FloodWait as error:
                await Tm.edit(f"Tunggu {error.x} detik")
                await asyncio.sleep(error.x)
        await Tm.edit(answer + ".", parse_mode=ParseMode.MARKDOWN)
    except Exception as err:
        await Tm.edit(f"ERROR:\n{str(err)}")
    await openai.aiosession.get().close()


async def dalle_cmd(client, message):
    Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b><code>{message.text}</code> [ǫᴜᴇʀʏ]</b>")
    try:
        response = await OpenAi.ImageDalle(message.text.split(None, 1)[1])
        msg = message.reply_to_message or message
        await client.send_photo(message.chat.id, response, reply_to_message_id=msg.id)
        return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()


async def stt_cmd(client, message):
    Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs...</code>")
    reply = message.reply_to_message
    if reply:
        if reply.voice or reply.audio or reply.video:
            file = await client.download_media(
                message=message.reply_to_message,
                file_name=f"sst_{message.reply_to_message.id}",
            )
            audio_file = f"{file}.mp3"
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {audio_file}"
            await run_cmd(cmd)
            os.remove(file)
            try:
                response = await OpenAi.SpeechToText(audio_file)
            except Exception as error:
                await message.reply(error)
                return await Tm.delete()
            if int(len(str(response))) > 4096:
                with io.BytesIO(str.encode(str(response))) as out_file:
                    out_file.name = "openAi.txt"
                    await message.reply_document(
                        document=out_file,
                    )
                    return await Tm.delete()
            else:
                msg = message.reply_to_message or message
                await client.send_message(
                    message.chat.id, response, reply_to_message_id=msg.id
                )
                return await Tm.delete()
        else:
            return await Tm.edit(
                f"<b><code>{message.text}</code> [ʀᴇᴘʟʏ ᴠᴏɪᴄᴇ_ᴄʜᴀᴛ/ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ]</b>"
            )
