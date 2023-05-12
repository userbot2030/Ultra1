from PyroUbot import *


@PY.CALLBACK("^confirm")
async def _(client, callback_query):
    await confirm_callback(client, callback_query)


@PY.CALLBACK("^(success|failed|home)")
async def _(client, callback_query):
    await success_failed_home_callback(client, callback_query)
