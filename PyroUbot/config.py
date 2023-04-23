import os

API_ID = int(os.getenv("API_ID"))

API_HASH = os.getenv("API_HASH")

BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("OWNER_ID"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))

COMMAND = os.getenv("COMMAND", ". , : ; !")
PREFIX = COMMAND.split()

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "25"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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",
).split()

MONGO_URL = os.getenv("MONGO_URL")

TEXT_PAYMENT = os.getenv(
    "TEXT_PAYMENT",
    """
<b>💬 SILAHKAN MELAKUKAN PEMBAYARAN SEBESAR RP25.000 = 1 BULAN</b>

<b>💳 MOTODE PEMBAYARAN:</b>
  <b>┣ DANA/GOPAY/OVO/SPAY</b>
  <b>┣    ┗</b> <code>089525658633</code>
  <b>┣ QRIS</b>
  <b>┗    ┗</b> <a href=https://telegra.ph/file/21e888e1960b1ce9392a7.jpg>KLIK DISINI</a>

<b>✅ KLIK TOMBOL KONFIRMASI UNTUK KIRIM BUKTI PEMBAYARAN ANDA</b>
""",
)
