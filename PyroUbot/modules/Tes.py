from PyroUbot import *


@CMD("prefix")
async def _(client, message):
    await setprefix(client, message)


@CMD(["tas", "tes"])
async def _(client, message):
    await coba(client, message)
