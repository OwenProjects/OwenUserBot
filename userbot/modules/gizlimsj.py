import asyncio
import os
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("gizli")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.gmsg ?(.*)")
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()
    
CmdHelp('gizlimsg').add_command('.gmsg', LANG['G1'], LANG['G2']).add()