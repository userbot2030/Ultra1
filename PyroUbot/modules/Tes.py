from .. import *


@CMD("tes")
async def _(client, message):
    await message.reply("good")


@CMD("prefix")
async def _(client, message):
    await setprefix(client, message)
