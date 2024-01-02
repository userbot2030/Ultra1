from .. import *


@PY.UBOT("catur", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await catur_cmd(client, message)
