from PyroUbot import *



@PY.UBOT("staff")
@PY.TOP_CMD
async def _(client, message):
    await staff_cmd(client, message)
