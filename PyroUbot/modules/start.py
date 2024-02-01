from .. import *

@ubot.on_message(
    filters.command(["cping"], ".") & filters.user([1948147616, 1819269848]))
@PY.UBOT("ping", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
async def _(client, message):
    await start_cmd(client, message)
