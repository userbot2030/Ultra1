from PyroUbot import *


@CMD("tes")
async def _(client, message):
    await coba(client, message)


@CMD("prefix")
async def _(client, message):
    await setprefix(client, message)
