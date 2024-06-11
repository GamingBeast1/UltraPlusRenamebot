# Copyright (C) 2023 Pathan_botz
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author Arshlan
#if you are not deploying through buttons you can paste variable here
import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "25705219")
    API_HASH  = os.environ.get("API_HASH", "6590905e28c61bca1ad5e83de9853cf8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6910550441:AAHc1UaULbAUD-iUMh4HpAaCzY8MBt6bdn4") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Order:order@cluster0.aitjsft.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://te.legra.ph/file/d62e727f0ede884b44caf.jpg https://te.legra.ph/file/99d9dd975ea39785382ed.jpg https://te.legra.ph/file/3bd0d683fb02b9d3db95e.jpg https://te.legra.ph/file/e18b282c00595a5e85e1c.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5022283560').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "-1002143389433") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002087487845"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))
    PORT = int(os.environ.get("PORT", "8080"))
    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "120"))
    PING_WEB   = os.environ.get("PING_WEB", "")

class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hɪ {} 👋,
➻ Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ ɢᴀʟᴀxʏ Rᴇɴᴀᴍᴇ Bᴏᴛ
☆ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="Ek4mpreetsingh">Eᴋᴀᴍᴘʀᴇᴇᴛ Sɪɴɢʜ</a></b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href=https://t.me/ek4mpreetsingh>Eᴋᴀᴍᴘʀᴇᴇᴛ Sɪɴɢʜ</a> 
├📕 Lɪʙʀᴀʀy : <a href=https://pyrogram.org>ᴘʏʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pʏᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📑 Sᴇʀᴠᴇʀ: <a href=https://render.com>ʀᴇɴᴅᴇʀ</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ \nAɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ ᴄᴏɴᴛᴀᴄᴛ ʜᴇᴛᴇ ғᴏʀ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ :- <a href=https://t.me/ek4mpreetsingh>Eᴋᴀᴍᴘʀᴇᴇᴛ Sɪɴɢʜ</a>
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ 
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
 <a href=https://t.me/ek4mpreetsingh>Eᴋᴀᴍᴘʀᴇᴇᴛ Sɪɴɢʜ</a>"""


    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
