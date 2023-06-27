from PyroUbot import *


@CMD("tes")
async def tes(client, message):
    await coba(client, message)


@CMD("prefix")
async def prefix(client, message):
    await setprefix(client, message)
