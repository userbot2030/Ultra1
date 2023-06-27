from PyroUbot import *


@CMD("prefix")
async def _(client, message):
    await setprefix(client, message)


@CMD("tes")
async def _(client, message):
    await coba(client, message)

