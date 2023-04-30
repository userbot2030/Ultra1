import json

import requests


async def jadwal_adzan(client, message):
    LOKASI = message.text.split(None, 1)[1]
    if len(message.command) < 2:
        return await message.reply("<b>sɪʟᴀʜᴋᴀɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴋᴏᴛᴀ ᴀɴᴅᴀ</b>")
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 20:
        await message.reply(f"<b>ᴍᴀᴀꜰ ᴛɪᴅᴀᴋ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴋᴏᴛᴀ</b> <code>{LOKASI}</code>")
    result = json.loads(request.text)
    catresult = """
<b>ᴊᴀᴅᴡᴀʟ sʜᴀʟᴀᴛ ʜᴀʀɪ ɪɴɪ</b>

<b>ᴛᴀɴɢɢᴀʟ</b> <code>{}</code>
<b>ᴋᴏᴛᴀ</b> <code>{} | {}</code>

<b>ᴛᴇʀʙɪᴛ:</b> <code>{}</code>
<b>sᴜʙᴜʜ:</b> <code>{}</code>
<b>ᴢᴜʜᴜʀ:</b> <code>{}</code>
<b>ᴀsʜᴀʀ:</b> <code>{}</code>
<b>ᴍᴀɢʜʀɪʙ:</b> <code>{}</code>
<b>ɪsʏᴀ:</b> <code>{}</code>
"""
    await message.reply(
        catresult.format(
            result["items"][0]["date_for"],
            result["query"],
            result["country"],
            result["items"][0]["shurooq"],
            result["items"][0]["fajr"],
            result["items"][0]["dhuhr"],
            result["items"][0]["asr"],
            result["items"][0]["maghrib"],
            result["items"][0]["isha"],
        )
    )
