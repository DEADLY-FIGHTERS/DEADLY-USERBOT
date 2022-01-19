#  Copyright (C) 2020  Copyless786(π.$)
# credits to @deadly-fighters (@deadly-fighters)
import asyncio
import os
import re

from userbot import deadlyub

from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_category = "fun"


@deadlyub.deadly_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs Deadly ; One of the Popular userbot",
    },
)
async def nekobot(deadly):
    "Fake google search meme"
    text = deadly.pattern_match.group(1)
    reply_to_id = await reply_id(deadly)
    if not text:
        if deadly.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(deadly, "`What should i search in google.`", 5)
    cate = await edit_or_reply(deadly, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            deadly,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    deadlyfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await deadly.client.send_file(deadly.chat_id, deadlyfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(deadlyfile):
        os.remove(deadlyfile)


@deadlyub.deadly_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump Deadly is One of the Popular userbot",
    },
)
async def nekobot(deadly):
    "trump tweet sticker with given custom text_"
    text = deadly.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(deadly)

    reply = await deadly.get_reply_message()
    if not text:
        if deadly.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(deadly, "**Trump : **`What should I tweet`", 5)
    cate = await edit_or_reply(deadly, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    deadlyfile = await trumptweet(text)
    await deadly.client.send_file(deadly.chat_id, deadlyfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(deadlyfile):
        os.remove(deadlyfile)


@deadlyub.deadly_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi Deadly is One of the Popular userbot",
    },
)
async def nekobot(deadly):
    "modi tweet sticker with given custom text"
    text = deadly.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(deadly)

    reply = await deadly.get_reply_message()
    if not text:
        if deadly.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(deadly, "**Modi : **`What should I tweet`", 5)
    cate = await edit_or_reply(deadly, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    deadlyfile = await moditweet(text)
    await deadly.client.send_file(deadly.chat_id, deadlyfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(deadlyfile):
        os.remove(deadlyfile)


@deadlyub.deadly_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm Deadly is One of the Popular userbot",
    },
)
async def nekobot(deadly):
    text = deadly.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(deadly)

    reply = await deadly.get_reply_message()
    if not text:
        if deadly.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(deadly, "`Give text to write on banner, man`", 5)
    cate = await edit_or_reply(deadly, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    deadlyfile = await changemymind(text)
    await deadly.client.send_file(deadly.chat_id, deadlyfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(deadlyfile):
        os.remove(deadlyfile)


@deadlyub.deadly_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna Deadly is One of the Popular userbot",
    },
)
async def nekobot(deadly):
    "kanna chan sticker with given custom text"
    text = deadly.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(deadly)

    reply = await deadly.get_reply_message()
    if not text:
        if deadly.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(deadly, "**Kanna : **`What should i show you`", 5)
    cate = await edit_or_reply(deadly, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    deadlyfile = await kannagen(text)
    await deadly.client.send_file(deadly.chat_id, deadlyfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(deadlyfile):
        os.remove(deadlyfile)


@deadlyub.deadly_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; Deadly is One of the Popular userbot",
    },
)
async def nekobot(deadly):
    "The desired person tweet sticker with given custom text"
    text = deadly.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(deadly)

    reply = await deadly.get_reply_message()
    if not text:
        if deadly.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                deadly,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            deadly,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    cate = await edit_or_reply(deadly, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    deadlyfile = await tweets(text, username)
    await deadly.client.send_file(deadly.chat_id, deadlyfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(deadlyfile):
        os.remove(deadlyfile)
