import random
import string


async def gen_password(client, message):
    if len(message.command) < 2:
        return await message.delete()
    try:
        count = int(message.command[1])
    except Exception as error:
        return await message.reply(error, quote=True)
    alphabet = string.ascii_letters + string.digits
    password = "".join(random.choice(alphabet) for i in range(count))
    return await message.reply(password, quote=True)
