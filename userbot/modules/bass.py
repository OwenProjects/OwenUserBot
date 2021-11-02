#OwenProjects-Owenuserbot
#ByMisakiMey-erdewbey-İxelizm
import asyncio
import io, os, math
from io import BytesIO
import numpy as np
from pydub import AudioSegment
from telethon import types
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("bass")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.bass ?(.*)")
async def bassbooster(e):
    v = False
    accentuate_db = 40
    reply = await e.get_reply_message()
    if not reply:
        await e.edit("**Bir sesli medyaya cevap verin**")
        return
    if e.pattern_match.group(1):
        ar = e.pattern_match.group(1)
        try:
            int(ar)
            if int(ar) >= 2 and int(ar) <= 100:
                accentuate_db = int(ar)
            else:
                await e.edit("**BassBost** `seviyeesi 2-100 arası olmalıdır.`")
                return
        except Exception as exx:
            await e.edit("`Bir Hata oluştu` \n**Hata:** " + str(exx))
            return
    else:
        accentuate_db = 2
    await e.edit("`Dosya yükleniyor...`")
    fname = await e.client.download_media(message=reply.media)
    await e.edit("`Bass effekti hazırlanıyor...`")
    if fname.endswith(".oga") or fname.endswith(".ogg"):
        v = True
        audio = AudioSegment.from_file(fname)
    elif fname.endswith(".mp3") or fname.endswith(".m4a") or fname.endswith(".wav"):
        audio = AudioSegment.from_file(fname)
    else:
        await e.edit(
            "`Desteklenmeyen dosya tipi` \n**Desteklenen dosya tipleri :** `mp3, m4a, wav.`"
        )
        os.remove(fname)
        return
    sample_track = list(audio.get_array_of_samples())
    await asyncio.sleep(0.3)
    est_mean = np.mean(sample_track)
    await asyncio.sleep(0.3)
    est_std = 3 * np.std(sample_track) / (math.sqrt(2))
    await asyncio.sleep(0.3)
    bass_factor = int(round((est_std - est_mean) * 0.005))
    await asyncio.sleep(5)
    attenuate_db = 0
    filtered = audio.low_pass_filter(bass_factor)
    await asyncio.sleep(5)
    out = (audio - attenuate_db).overlay(filtered + accentuate_db)
    await asyncio.sleep(6)
    m = io.BytesIO()
    if v:
        m.name = "voice.ogg"
        out.split_to_mono()
        await e.edit("`Hazırlanıyor...`")
        await asyncio.sleep(0.3)
        out.export(m, format="ogg", bitrate="64k", codec="libopus")
        await e.edit("`Effekt hazırlandı\n Dosy gönderiliyor...`")
        await e.client.send_file(
            e.to_id,
            m,
            reply_to=reply.id,
            voice_note=True,
            caption=" `@OwenUserBot `ile bass boostlandı.`",
        )

    else:
        m.name = "OwenBASS.mp3"
        await e.edit("`Hazırlanıyor...`")
        await asyncio.sleep(0.3)
        out.export(m, format="mp3")
        await e.edit("`Effekt hazırlandı\n Dosya Gönderiliyor`")
        await e.client.send_file(
            e.to_id,
            m,
            reply_to=reply.id,
            attributes=[
                types.DocumentAttributeAudio(
                    duration=reply.document.attributes[0].duration,
                    title=f"BassBoost {str(accentuate_db)}lvl",
                    performer="BassBoost",
                )
            ],
            caption="@OwenUserBot `ile bass boostlandı.",
        )
    await e.delete()
    os.remove(fname)
    
CmdHelp('bass').add_command('bass', (LANG['BASS1']), (LANG['BASS2'])
).add_warning((LANG['BASS3'])
).add_info('🎆 By @ErdewBey').add()
