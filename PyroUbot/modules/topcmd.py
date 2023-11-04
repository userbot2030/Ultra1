from PyroUbot import *


@PY.UBOT("topcmd", FILTERS.ME_OWNER)
async def _(client, message):
    await get_top_module(client, message)
