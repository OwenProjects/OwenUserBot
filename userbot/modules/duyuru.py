# Erdem Bey / 

from telethon import events
import asyncio
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("duyuru")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.duyur ?(.*)")
async def yay(event):
    mesaj = event.pattern_match.group(1)
    if len(mesaj) < 1:
        await event.edit("`Birşeyleri Yaymak için bir mesaj vermeniz gerek. Örnek: ``.yay merhaba dünya`")
        return

    if event.is_private:
        await event.edit("`Bu komut sadece gruplarda çalışmaktadır.`")
        return

    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await event.edit("`Ciddi misin? Admin olmadığın bir grupta duyuru göndermene izin vermiyeceğim!`")
        return

    await event.edit("`Tüm üyelerinize duyurunuz gönderiliyor...`")
    all_participants = await event.client.get_participants(event.chat_id, aggressive=True)
    a = 0

    for user in all_participants:
        a += 1
        uid = user.id
        if user.username:
            link = "@" + user.username
        else:
            link = "[" + user.first_name + "](" + str(user.id) + ")"
        try:
            await event.client.send_message(uid, mesaj + "\n\n@OwenUserBot ile gönderildi.")
            son = f"**Son duyuru gönderilen kullanıcı:** {link}"
        except:
            son = f"**Son duyuru gönderilen kullanıcı:** **Gönderilemedi!**"
    
        await event.edit(f"`Tüm üyelerinize duyurunuz gönderiliyor...`\n{son}\n\n**Durum:** `{a}/{len(all_participants)}`")
        await asyncio.sleep(0.5)

    await event.edit("`Tüm üyelerinize duyurunuz gönderildi!`\n\nby @OwenUserBot 😙")
 
CmdHelp('duyuru').add_command(
	'duyuru', LANG['DUYURU1']
).add()
