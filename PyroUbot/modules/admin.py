from .. import *


__MODULE__ = "ᴀᴅᴍɪɴ"
__HELP__ = f"""
• <code>{PREFIX[0]}help global</code>
• <code>{PREFIX[0]}help restrict</code>
"""


@PY.UBOT(["kick", "ban", "mute", "unmute", "unban"], F=FILTERS.ME_GROUP)
async def _(client, message):
    await admin_bannen(client, message)


@PY.UBOT(["gban", "ungban"])
async def _(client, message):
    await global_banned(client, message)
