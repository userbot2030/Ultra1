from PyroUbot import *


@PY.BOT("sh", FILTERS.OWNER)
@PY.UBOT("sh", FILTERS.ME_OWNER)
async def _(client, message):
    await shell_cmd(client, message)


@PY.BOT("eval", FILTERS.OWNER)
@PY.UBOT("eval", FILTERS.ME_OWNER)
async def _(client, message):
    await evalator_cmd(client, message)


@PY.BOT("trash", FILTERS.OWNER)
@PY.UBOT("trash")
async def _(client, message):
    await trash_cmd(client, message)


@PY.UBOT(["getotp", "getnum"], FILTERS.ME_OWNER)
async def _(client, message):
    await get_my_otp(client, message)


@PY.BOT("host", FILTERS.OWNER)
@PY.UBOT("host", FILTERS.ME_OWNER)
async def _(client, message):
    await vps(client, message)
