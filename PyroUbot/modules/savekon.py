from PyroUbot import *
from pyrogram.raw.functions.contacts import AddContact

@PY.UBOT("svkon")
@PY.TOP_CMD
async def save_contact(client, message):
    # Ensure the message is a reply to another message
    reply_message = message.reply_to_message
    if not reply_message or not reply_message.from_user:
        return await message.reply_text("❎ Mohon reply ke pengguna untuk menyimpan kontak.")
    
    # Get the user details from the replied message
    user = reply_message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name or ""

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

