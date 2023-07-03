from PyroUbot import *


# @CMD("prefix")
@ubot.on_message(filters.text & command_filter("prefix"))
async def _(client, message):
    await setprefix(client, message)


# @CMD("tes")
@ubot.on_message(filters.text & command_filter("tes))
async def _(client, message):
    await coba(client, message)
