from PyroUbot import *


@PY.UBOT("topcmd")
async def _(client, message):
    await get_top_module(client, message)
