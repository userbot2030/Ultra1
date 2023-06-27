from PyroUbot import *


@CMD("prefix")
async def _(client, message):
    await setprefix(client, message)


@CMD("tes")
async def (client, message):
    await coba(client, message)

