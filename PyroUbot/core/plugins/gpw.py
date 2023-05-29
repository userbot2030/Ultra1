import string, random


async def gen_password(client, message):
    try:
       count = int(message.command[1])
     except Exception as error:
         return await message.reply(error, quote=True)
     alphabet = string.ascii_letters + string.digits
     password = ''.join(random.choice(alphabet) for i in range(count))
     await message.reply(password, quote=True)
