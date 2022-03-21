# Copyright (C) 2022 The  OwenProjects.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# OwenUserBot - ErdewBey - Ber4tbey

""" Olayları yönetmek için UserBot modülü.
 UserBot'un ana bileşenlerinden biri. """
import re
from requests import get
import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc
from telethon import events
import base64
from userbot import bot, BOTLOG_CHATID, LOGSPAMMER, PATTERNS, OWEN_VERSION, ForceVer
from telethon.tl.functions.channels import JoinChannelRequest


def register(**args):
    """ Yeni bir etkinlik kaydedin. """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)

    if pattern:
        args["pattern"] = pattern.replace("^.", "^["+ PATTERNS + "]")
    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
      
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']

    def decorator(func):
        async def wrapper(check):
         #events1 = base64.a85decode("95JNa+@:!g+EV19E+sD:ARoLkA8*21+@C'dGp%'7F*(u6+X$") #Ber4tbey - @OwenProjects Büyüdükçe gelişmeye geliştikçe büyümeye devam ediyoruz.
         #events2 = base64.a85decode("6uQRNATDBsCh3")
         #events3 = base64.a85decode(":NpAf:i^JhARfh'")
         #ber4tbey = open(events2, "r").read() 
         #if not re.search(str(events3),ber4tbey):
         #   await check.edit(str(events1))
        #    return
         #else:
          #  pass
          
          
            OwenVer = int(OWEN_VERSION.split(".")[1])
            if ForceVer > OwenVer:
                await check.edit(f"`🌈 Botu acilen güncellemen lazım! Bu sürüm artık kullanılamıyor..`\n\n__🥺 Sorunu çözmek için__ `.update now` __yazmalısın!__")
                return

            if not LOGSPAMMER:
                send_to = check.chat_id
            else:
                send_to = BOTLOG_CHATID

            if not trigger_on_fwd and check.fwd_from:
                return

            if check.via_bot_id and not trigger_on_inline:
                return
             
            if groups_only and not check.is_group:
                await check.respond("`⛔ Bunun bir grup olduğunu sanmıyorum. Bu plugini bir grupta dene! `")
                return

            try:
                await func(check)
                

            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except AttributeError:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    eventtext = str(check.text)
                    text = "**🛑USERBOT HATA RAPORU🛑**\n"
                    link = "[Owen Destek Grubuna](https://t.me/OwenSupport)"
                    if len(eventtext)<10:
                        text += f"\n**🗒️ Şu yüzden:** {eventtext}\n"
                    text += "\nℹ️ İsterseniz, bunu bildirebilirsiniz."
                    text += f"- sadece bu mesajı {link} gönderin.\n"
                    text += "Hata ve tarih haricinde hiçbir şey kayıt edilmez.\n"

                    ftext = "========== UYARI =========="
                    ftext += "\nBu dosya sadece burada yüklendi,"
                    ftext += "\nSadece hata ve tarih kısmını kaydettik,"
                    ftext += "\nGizliliğinize saygı duyuyoruz,"
                    ftext += "\nBurada herhangi bir gizli veri varsa"
                    ftext += "\nBu hata raporu olmayabilir, kimse verilerinize ulaşamaz.\n"
                    ftext += "--------USERBOT HATA GUNLUGU--------\n"
                    ftext += "\nTarih: " + date
                    ftext += "\nGrup ID: " + str(check.chat_id)
                    ftext += "\nGönderen kişinin ID: " + str(check.sender_id)
                    ftext += "\n\nOlay Tetikleyici:\n"
                    ftext += str(check.text)
                    ftext += "\n\nHata metni:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n\nGeri izleme bilgisi:\n"
                    ftext += str(format_exc())
                    ftext += "\n\n--------USERBOT HATA GUNLUGU BITIS--------"
                    ftext += "\n\n================================\n"
                    ftext += f"====== BOTVER : {OWEN_VERSION} ======\n"
                    ftext += "================================"

                    command = "git log --pretty=format:\"%an: %s\" -7"

                    ftext += "\n\n\nSon 7 commit:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

                    if LOGSPAMMER:
                        try:
                            await check.edit("`❕ Üzgünüm, UserBot bir hatayla karşılaştı.\n ℹ️ Hata günlükleri UserBot günlük grubunda saklanır.`")
                        except:
                            pass
                    await check.client.send_file(send_to,
                                                 "error.log",
                                                 caption=text)

                    remove("error.log")
            else:
                pass
        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))

        return wrapper

    return decorator
