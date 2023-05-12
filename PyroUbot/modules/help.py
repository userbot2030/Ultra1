from PyroUbot import *


@PY.UBOT("help", PREFIX)
async def _(client, message):
    await help_cmd(client, message)


@PY.INLINE("^help")
@INLINE.QUERY
async def _(client, inline_query):
    await menu_inline(client, inline_query)


@PY.CALLBACK("help_(.*?)")
@INLINE.DATA
async def _(client, callback_query):
    await menu_callback(client, callback_query)
