
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# OwenUserBot - ErdewBey - ByMisakiMey - Midy
#
import requests
from googletrans import Translator
from telethon import events
from telethon.tl.types import User

from userbot import BLACKLIST_CHAT
from userbot import LOGS, bot, LANGUAGE as DIL
from userbot.events import register
from userbot.cmdhelp import CmdHelp

translator = Translator()
LANGUAGE = DIL

aktivet = []
LANGUAGES = LANGUAGE

url = "https://api-tede.herokuapp.com/api/chatbot?message={message}"

# ---------------------------------- #

#from userbot.language import get_value
#LANG = get_value("chatbot")      YAKINDA 

# ---------------------------------- #

async def cavablama(message):
    link = url.format(message=message)
    try:
        data = requests.get(link)
        if data.status_code == 200:
            return (data.json())["msg"]
        LOGS.info("Bir Hata Oluştu!")
    except Exception:
        LOGS.info("Hata: {str(e)}")


async def aktivetme(db, event):
    status = event.pattern_match.group(1).lower()
    chat_id = event.chat_id
    if status == "on":
        if chat_id not in db:
            db.append(chat_id)
            return await event.edit("```Chatbot aktif.```")
        await event.edit("```Chatbot başarıyla kapatıldı.```")
    elif status == "off":
        if chat_id in db:
            db.remove(chat_id)
            return await event.edit("```Chatbot başarıyla kapatıldı.```")
        await event.edit("```Chatbot başarıyla kapatıldı.```")
    else:
        await event.edit("```**Kullanımı:**\n.chatbot <on/off>```")


@register(outgoing=True, pattern=r"^\.chatbot(?: |$)(.*)")
async def chatbot(event):
    await aktivetme(aktivet, event)


@register(incoming=True)
async def chatbot(event):
    sender = await event.get_sender()
    if not isinstance(sender, User):
        return
    if event.chat_id not in aktivet:
        return
    if event.text and event.is_reply:
        rep = await cavablama(event.message.message)
        tr = translator.translate(rep, LANGUAGE)
        if tr:
            await event.reply(tr.text)
            

              
            
CmdHelp('chatbot').add_command(
'chatbot on', None, 'Chatbotu aktif eder.'
    ).add_command(
        'chatbot off', None, 'Chatbotu devredışı bırakır.'
    ).add()
