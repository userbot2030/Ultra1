from PyroUbot import *
from pyrogram.raw.functions.contacts import AddContact

@PY.UBOT("savekon")
@PY.TOP_CMD
async def save_contact(client, message):
    user_id = None
    first_name = None
    last_name = ""

    # Check if the message is a reply to another message
    reply_message = message.reply_to_message
    if reply_message and reply_message.from_user:
        user = reply_message.from_user
        user_id = user.id
        first_name = user.first_name
        last_name = user.last_name or ""
    else:
        # Check if the message contains a user ID argument
        args = message.command
        if len(args) < 2:
            return await message.reply_text("❎ Mohon reply ke pengguna atau masukkan ID pengguna untuk menyimpan kontak.")
        
        user_id = int(args[1])
        
        # Fetch user details using user ID
        try:
            user = await client.get_users(user_id)
            first_name = user.first_name
            last_name = user.last_name or ""
        except Exception as e:
            return await message.reply_text(f"❎ Terjadi kesalahan: {e}")

    # Resolve the peer ID of the user
    chat_id = await client.resolve_peer(user_id)

    # Attempt to add the contact
    try:
        response = await client.invoke(
            AddContact(
                id=chat_id,
                first_name=first_name,
                last_name=last_name,
                phone=""
            )
        )
        # Check if the contact was added successfully
        if response.users and response.users[0].contact:
            await message.reply_text(f"✅ Berhasil menyimpan kontak dengan nama {first_name}")
        else:
            await message.reply_text("❎ Terjadi kesalahan saat menyimpan kontak.")
    except Exception as e:
        await message.reply_text(f"❎ Terjadi kesalahan: {e}")
        
