# ErdewBey OwenUserBot 

from userbot.events import register
from userbot import CMD_HELP 
import asyncio
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.fyazı(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 60
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Yanlış format`")
    await event.edit(f"`hiçbir şey yapmıyorum!`")
    await event.edit(f"`Şimdi Bir Yazı Yazacağım Herkes Beni İzlesin.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fses(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 60
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Yanlış format`")
    await event.edit(f"`Şimdi Bir Ses Atacağım Herkez Dinlesin`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 60
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Yanlış formatt`")
    await event.edit(f"`Şimdi Bir Video Atacağım Herkez İzlesin...`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)
CmdHelp('fakes').add_command(
	'fyazı', None, 'Fake Yazı Yazıyormuş Gibi Gösterir (1dk)').add_command(
    'fses', None, 'Fake Ses Kayıt Ediyormuş Gibi Gösterir (1dk)').add_command(
    'fvideo', None, 'Fake Video Kayıt Ediyormuş Gibi Gösterir (1dk)').add_info("`Botu Yeniden Başlatarak İşleme Son Veriniz` @ErdewBey ✨").add()
