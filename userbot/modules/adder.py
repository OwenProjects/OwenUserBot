from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from userbot import CMD_HELP
from userbot.cmdhelp import CmdHelp
from userbot.events import register as erdem
from userbot import bot, BLACKLIST_CHAT

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Geçersiz Grup/Kanal`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`Böyle bir olduğuna eminmisin banlanmış olabilirsin.`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Böyle bir yer yok dostum.`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Geçersiz Grup/Kanal`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@erdem(outgoing=True, disable_errors=True, groups_only=True, pattern=r"^\.adder (.*)")
async def get_users(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await event.edit("Resmi Grupta Bunu Kullanamazsın.")
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        erdem = await event.edit("`Kullanıcı Listesi Alınıyor...`")
    else:
        erdem = await event.edit("`Üyeler Ekleniyor...`")
    farid = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await erdem.edit("`Kullanıcı Listesi Alınamadı.`")
    s = 0
    f = 0
    error = "None"

    await erdem.edit("**Owen UserBot ADDER**\n\n`Üyeler Ekleniyor...`")
    async for user in event.client.iter_participants(farid.full_chat.id):
        try:
            if error.startswith("Too"):
                return await erdem.edit(
                    f"**Owen UserBot ADDER**\n `Spamdasınız Galiba Emin Olmak İçin .sinfo Yazarak Kontrol Edebilirsiniz.` \nHata \n`{error}` \n\n `{s}` Üyeler Eklendi.\n `{f}` Kullanıcı Eklenemedi."
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await erdem.edit(
                f"**Owen UserBot ADDER**\n\n`{s}` Üyeler Eklendi.\n`{f}` Kullanıcı Eklenemedi \n\n**Hata:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await erdem.edit(
        f"**Owen UserBot ADDER** \n\nBaşarılı İşlem: ✔️ `{s}` .\nBaşarısız İşlem: ❌ `{f}`"
    )
