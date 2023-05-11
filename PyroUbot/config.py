import os

API_ID = int(os.getenv("API_ID", "22039315"))

API_HASH = os.getenv("API_HASH", "b9d878c0e74f6b2a2e2df3a1d9be968b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6207982225:AAGVegK7PzqYd20G1qnAzgl2vyqJNbnSv3A")

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

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://PremUbot:sST5VL04n85JkcxS@cluster0.wixneuz.mongodb.net/?retryWrites=true&w=majority")

TEXT_PAYMENT = os.getenv(
    "TEXT_PAYMENT",
    """
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ sᴇʙᴇsᴀʀ ʀᴘ25.000 = 1 ʙᴜʟᴀɴ</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
  <b>┣ ᴅᴀɴᴀ: </b> <code>089525658633</code>
  <b>┣ ɢᴏᴘᴀʏ:</b> </b> <code>089525658633</code>
  <b>┣ ᴏᴠᴏ:</b> </b> <code>089525658633</code>
  <b>┣ sᴘᴀʏ</b> </b> <code>089525658633</code>
  <b>┗ ǫʀɪs:</b> </b> <a href=https://api.qrcode-monkey.com/tmp/2274eaefa4ad07bab3a2578ac5c1e000.png>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
""",
)
