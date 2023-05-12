from PyroUbot import *


@PY.BOT("sh", FILTERS.OWNER)
@PY.UBOT("sh", FILTERS.ME_OWNER)
async def _(client, message):
    await shell_cmd(client, message)


@PY.BOT("eval", FILTERS.OWNER)
@PY.UBOT("eval")
async def _(client, message):
    await evalator_cmd(client, message)
