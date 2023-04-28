from PyroUbot.config import PREFIX

help_admin = [
    f"""
<b>『 Bantuan Admin Global 』</b>

    <b>• Perintah-:</b> <code>{PREFIX[0]}gban</code> [user_id/username/reply to user]
    <b>• Penjelasan:</b> Untuk banned user dari semua group chat 

    <b>• Perintah:</b> <code>{PREFIX[0]}ungban</code> [user_id/username/reply to user]
    <b>• Penjelasan:</b> Untuk unbanned user dari semua group chat
""",
    f"""
<b>『 Bantuan Admin Restrict 』</b>

    <b>• Perintah:</b> <code>{PREFIX[0]}kick</code> [user_id/username/reply user]
    <b>• Penjelasan:</b> Untuk menendang anggota dari grup 

    <b>• Perintah:</b> <code>{PREFIX[0]}ban</code> [user_id/username/reply user]
    <b>• Penjelasan:</b> Untuk memblokir anggota dari grup 

    <b>• Perintah:</b> <code>{PREFIX[0]}mute</code> [user_id/username/reply user]
    <b>• Penjelasan:</b> Untuk membisukan anggota dari grup 

    <b>• Perintah:</b> <code>{PREFIX[0]}unban</code> [user_id/username/reply user]
    <b>• Penjelasan:</b> Untuk melepas pemblokiran anggota dari grup 

    <b>• Perintah:</b> <code>{PREFIX[0]}unmute</code> [user_id/username/reply user]
    <b>• Penjelasan:</b> Untuk melepas pembisuan anggota dari grup
""",
]

help_sticker = [
    f"""
<b>『 Bantuan Sticker Kang 』</b>

    <b>• Perintah:</b> <code>{PREFIX[0]}kang</code> [reply to image/sticker]
    <b>• Penjelasan:</b> Untuk Menambahkan dan costum emoji sticker Ke Sticker Pack
""",
    f"""
<b>『 Bantuan Sticker Memify 』</b>

    <b>• Perintah:</b> <code>{PREFIX[0]}mmf</code> [text]
    <b>• Penjelasan:</b> Balas Ke Sticker atau Foto akan Di ubah menjadi sticker teks meme yang di tentukan
""",
    f"""
<b>『 Bantuan Sticker Memes 』</b>

    <b>• Perintah:</b> <code>{PREFIX[0]}memes</code> [text]
    <b>• Penjelasan:</b> Untuk membuat stiker memes random
""",
    f"""
<b>『 Bantuan Sticker Quotly 』</b>

    <b>• Perintah:</b> <code>{PREFIX[0]}q</code> [text/reply to text/media]
    <b>• Penjelasan:</b> Untuk merubah text menjadi sticker
""",
    f"""
<b>『 Bantuan Sticker Tiny 』</b>

    <b>• Perintah:</b> <code>{PREFIX[0]}tiny</code> [reply to sticker]
    <b>• Penjelasan:</b> Untuk merubah sticker menjadi kecil
""",
]

HelpText = {
    "global": help_admin[0],
    "restrict": help_admin[1],
    "kang": help_sticker[0],
    "memify": help_sticker[1],
    "memes": help_sticker[2],
    "quotly": help_sticker[3],
    "tiny": help_sticker[4],
}


