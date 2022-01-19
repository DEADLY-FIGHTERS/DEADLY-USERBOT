# credits to @deadly-fighters and @deadly-fighters

import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import deadlyub

from ..Config import Config
from ..funcs.managers import edit_or_reply
from . import awooify, baguette, convert_toimage, iphonex, lolice

plugin_category = "tools"


@deadlyub.deadly_cmd(
    pattern="mask$",
    command=("mask", plugin_category),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(deadlybot):
    "Hazmat suit maker"
    reply_message = await deadlybot.get_reply_message()
    if not reply_message.media or not reply_message:
        return await edit_or_reply(deadlybot, "```reply to media message```")
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        return await edit_or_reply(deadlybot, "```Reply to actual users message.```")
    event = await deadlybot.edit("```Processing```")
    async with deadlybot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await deadlybot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.edit(
                "```Please unblock @hazmat_suit_bot and try again```"
            )
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await deadlybot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@deadlyub.deadly_cmd(
    pattern="awooify$",
    command=("awooify", plugin_category),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def deadlybot(deadlymemes):
    "replied Image will be face of other image"
    replied = await deadlymemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    if replied.media:
        deadlyevent = await edit_or_reply(deadlymemes, "passing to telegraph...")
    else:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    download_location = await deadlymemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await deadlyevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await deadlyevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await deadlyevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await deadlyevent.edit("ERROR: " + str(exc))
    deadly = f"https://telegra.ph{response[0]}"
    deadly = await awooify(deadly)
    await deadlyevent.delete()
    await deadlymemes.client.send_file(deadlymemes.chat_id, deadly, reply_to=replied)


@deadlyub.deadly_cmd(
    pattern="lolice$",
    command=("lolice", plugin_category),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def deadlybot(deadlymemes):
    "replied Image will be face of other image"
    replied = await deadlymemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    if replied.media:
        deadlyevent = await edit_or_reply(deadlymemes, "passing to telegraph...")
    else:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    download_location = await deadlymemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await deadlyevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await deadlyevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await deadlyevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await deadlyevent.edit("ERROR: " + str(exc))
    deadly = f"https://telegra.ph{response[0]}"
    deadly = await lolice(deadly)
    await deadlyevent.delete()
    await deadlymemes.client.send_file(deadlymemes.chat_id, deadly, reply_to=replied)


@deadlyub.deadly_cmd(
    pattern="bun$",
    command=("bun", plugin_category),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def deadlybot(deadlymemes):
    "replied Image will be face of other image"
    replied = await deadlymemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    if replied.media:
        deadlyevent = await edit_or_reply(deadlymemes, "passing to telegraph...")
    else:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    download_location = await deadlymemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await deadlyevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await deadlyevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await deadlyevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await deadlyevent.edit("ERROR: " + str(exc))
    deadly = f"https://telegra.ph{response[0]}"
    deadly = await baguette(deadly)
    await deadlyevent.delete()
    await deadlymemes.client.send_file(deadlymemes.chat_id, deadly, reply_to=replied)


@deadlyub.deadly_cmd(
    pattern="iphx$",
    command=("iphx", plugin_category),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def deadlybot(deadlymemes):
    "replied image as iphone x wallpaper."
    replied = await deadlymemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    if replied.media:
        deadlyevent = await edit_or_reply(deadlymemes, "passing to telegraph...")
    else:
        return await edit_or_reply(deadlymemes, "reply to a supported media file")
    download_location = await deadlymemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await deadlyevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await deadlyevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await deadlyevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await deadlyevent.edit("ERROR: " + str(exc))
    deadly = f"https://telegra.ph{response[0]}"
    deadly = await iphonex(deadly)
    await deadlyevent.delete()
    await deadlymemes.client.send_file(deadlymemes.chat_id, deadly, reply_to=replied)
