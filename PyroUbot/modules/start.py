from .. import *


@PY.UBOT("ping", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
async def _(client, message):
    await start_cmd(client, message)
