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
<b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ sᴇʙᴇsᴀʀ ʀᴘ25.000 = 1 ʙᴜʟᴀɴ</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
  <b>┣ ᴅᴀɴᴀ/ɢᴏᴘᴀʏ/ᴏᴠᴏ/sᴘᴀʏ</b>
  <b>┣    ┗</b> <code>089525658633</code>
  <b>┣ ǫʀɪs</b>
  <b>┗    ┗</b> <a href=https://api.qrcode-monkey.com/tmp/2274eaefa4ad07bab3a2578ac5c1e000.png>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b>
""",
)
