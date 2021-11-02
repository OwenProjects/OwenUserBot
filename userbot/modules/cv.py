# Credit Vermeyi Unutmayın Zsten Açık Kaynaklı Kodlar
#Owenuserbot-ErdewBey-ixelizm-ByMisakiMey

from telethon import events 
import asyncio 
from userbot.events import register as owen
from userbot import (MYID)
from userbot.main import PLUGIN_MESAJLAR
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("cv")

# ████████████████████████████████ #

@owen(incoming=True, pattern="^.cv")
async def cvhazırlama(ups):
    if ups.fwd_from:
        return
    if ups.is_reply:
        reply = await ups.get_reply_message()
        replytext = reply.text
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            await ups.reply(f"{PLUGIN_MESAJLAR['cv']}")
		        
@owen(outgoing=True, pattern="^.mycv")
async def komut(e):
        await e.edit(f"{PLUGIN_MESAJLAR['cv']}")

CmdHelp('cv').add_command(
	'cv',  LANG["CV1"]
	).add_command(
	'mycv', LANG["CV2"]
	).add_command(
	'.değiştir cv', LANG["CV3"]
).add()
