# ErdewBey İpLogger | OwenUserbot 
# ipstack.com 
# Token Sahibi Sam Pandeey

import json
import urllib.request
from userbot.events import register #editlene bilir
from userbot.cmdhelp import CmdHelp #isteğe bağlı

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("iplogger")

# ████████████████████████████████ #

@register(outgoing=True, pattern=".iplogger (.*)") #editlene bilir
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    adress = input_str
    token = "19e7f2b6fe27deb566140aae134dec6b" # Dokunma
    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1" #dokunma 

    result = urllib.request.urlopen(api).read()
    result = result.decode()
# siteye göre ayarlıdır
    result = json.loads(result)
    a = result["type"] 
    b = result["country_code"]
    c = result["region_name"]
    d = result["city"]
    e = result["zip"]
    f = result["latitude"]
    g = result["longitude"]
    await event.edit("İpLogger 🕵🏻‍♀️") #editlene bilir
    await event.edit("İpLogger   ") #editlene bilir
    await event.edit("İpLogger 🕵🏻‍♀️") #editlene bilir
    await event.edit(
        f"<b><u>BAŞARIYLA TOPLANAN BİLGİLER</b></u>\n\n<b>IP tipi :-</b><code>{a}</code>\n<b>Ülke kodu:- </b> <code>{b}</code>\n<b>Devlet adı :-</b><code>{c}</code>\n<b>Şehir İsmi :- </b><code>{d}</code>\n<b>zip :-</b><code>{e}</code>\n<b>Enlem:- </b> <code>{f}</code>\n<b>Boylam :- </b><code>{g}</code>\n",
        parse_mode="HTML", #editlene bilir
    )

CmdHelp("iplogger").add_command('iplogger', LANG['İP1'], LANG['İP2']).add()
