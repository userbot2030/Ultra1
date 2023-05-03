from .. import *



@PY.UBOT(["kick", "ban", "mute", "unmute", "unban"], F=FILTERS.ME_GROUP)
async def _(client, message):
    await admin_bannen(client, message)



@PY.UBOT(["gban", "ungban"])
async def _(client, message):
    await global_banned(client, message)
