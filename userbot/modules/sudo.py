# OwenProjects Erdem Bey ByMisakimey

import os
import re
from userbot.events import register
from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    SUDO_ID,
    bot,
)
import heroku3
from telethon.tl.functions.users import GetFullUserRequest

Heroku = heroku3.from_key(HEROKU_APIKEY)
heroku_api = "https://api.heroku.com"
owensudo = os.environ.get("SUDO_ID", None)

@register(outgoing=True,
          pattern=r"^.sudoekle")
async def addsudo(event):
    await event.edit("`Kullanıcı sudo olarak ayarlanıyor`...")
    owen = "SUDO_ID"
    if HEROKU_APPNAME is not None:
        app = Heroku.app(HEROKU_APPNAME)
    else:
        await event.edit("HEROKU:" "\nLütfen **HEROKU_APPNAME** değerini tanımlayın.")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        owentext = await get_user(event)
    except Exception:
        await event.edit("`Lütfen bir kullanıcının mesajına cevap verin.`")
    if owensudo:
        yenisudo = f"{owensudo} {owentext}"
    else:
        yenisudo = f"{owentext}"
    await event.edit("`Kullanıcı sudo olarak ayarlandı.👌` \n`Botunuz yeniden başlatılıyor...`")
    heroku_var[owen] = yenisudo


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    owentext = replied_user.user.id
    return owentext

@register(outgoing=True,
          pattern=r"^.sudosil")
async def sudosil(event):
  Heroku = heroku3.from_key(HEROKU_APIKEY)
  app = Heroku.app(HEROKU_APPNAME)
  heroku_var = app.config()
  if not event.is_reply:
    return await event.edit("`Lütfen bir kullanıcının mesajına cevap verin.`")
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    ad = (await bot.get_entity(id)).first_name
    op = re.search(str(id), str(owensudo))
    if op:
      i = ""
      esudo = owensudo.split(" ")
      esudo.remove(str(id))
      i += str(esudo)
      x = i.replace("[", "")
      xx = x.replace("]", "")
      xxx = xx.replace(",", "")
      hazir = xxx.replace("'", "")
      heroku_var["SUDO_ID"] = hazir
      await event.edit(f"`{ad}``Artık Sudo değil 👌.`\n`Botunuz yeniden başlatılıyor...`")
    else:
      await event.edit(f"`Kusura bakma,` `{ad}` `Zaten Bir Sudo Değil!`")
    if heroku_var["SUDO_ID"] == None:
       await event.edit(f"`Sudo Bulunmamaktadır!`") 
    
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    owent = replied_user.user.id
    return owent
    
@register(incoming=True, from_users=SUDO_ID, pattern="^.salive$")
async def _(q):
    await q.client.send_message(q.chat_id,"`Sudom ❤️ OwenUserBot Çalışıyor...`")
