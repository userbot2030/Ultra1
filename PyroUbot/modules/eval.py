from .. import *


@PY.BOT("sh", FILTERS.OWNER)
@PY.UBOT("sh", FILTERS.ME_OWNER)
async def _(client, message):
    await shell_cmd(client, message)


@PY.BOT("trash", FILTERS.OWNER)
@PY.UBOT("trash", PREFIX)
async def _(client, message):
    await evalator_cmd(client, message)
