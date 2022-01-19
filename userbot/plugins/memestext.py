import random

from userbot import deadlyub

from ..funcs.managers import edit_or_reply
from . import deadlymemes

plugin_category = "fun"


@deadlyub.deadly_cmd(
    pattern="congo$",
    command=("congo", plugin_category),
    info={
        "header": " Congratulate the people..",
        "usage": "{tr}congo",
    },
)
async def _(e):
    "Congratulate the people."
    txt = random.choice(deadlymemes.CONGOREACTS)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="shg$",
    command=("shg", plugin_category),
    info={
        "header": "Shrug at it !!",
        "usage": "{tr}shg",
    },
)
async def shrugger(e):
    "Shrug at it !!"
    txt = random.choice(deadlymemes.SHGS)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="runs$",
    command=("runs", plugin_category),
    info={
        "header": "Run, run, RUNNN!.",
        "usage": "{tr}runs",
    },
)
async def runner_lol(e):
    "Run, run, RUNNN!"
    txt = random.choice(deadlymemes.RUNSREACTS)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="noob$",
    command=("noob", plugin_category),
    info={
        "header": "Whadya want to know? Are you a NOOB?",
        "usage": "{tr}noob",
    },
)
async def metoo(e):
    "Whadya want to know? Are you a NOOB?"
    txt = random.choice(deadlymemes.NOOBSTR)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="insult$",
    command=("insult", plugin_category),
    info={
        "header": "insult someone.",
        "usage": "{tr}insult",
    },
)
async def insult(e):
    "insult someone."
    txt = random.choice(deadlymemes.INSULT_STRINGS)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="love$",
    command=("love", plugin_category),
    info={
        "header": "Chutiyappa suru",
        "usage": "{tr}love",
    },
)
async def suru(chutiyappa):
    "Chutiyappa suru"
    txt = random.choice(deadlymemes.LOVESTR)
    await edit_or_reply(chutiyappa, txt)


@deadlyub.deadly_cmd(
    pattern="dhoka$",
    command=("dhoka", plugin_category),
    info={
        "header": "Dhokha kha gya",
        "usage": "{tr}dhoka",
    },
)
async def katgya(chutiya):
    "Dhokha kha gya"
    txt = random.choice(deadlymemes.DHOKA)
    await edit_or_reply(chutiya, txt)


@deadlyub.deadly_cmd(
    pattern="hey$",
    command=("hey", plugin_category),
    info={
        "header": "start a conversation with people",
        "usage": "{tr}hey",
    },
)
async def hoi(e):
    "start a conversation with people."
    txt = random.choice(deadlymemes.HELLOSTR)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="pro$",
    command=("pro", plugin_category),
    info={
        "header": "If you think you're pro, try this.",
        "usage": "{tr}pro",
    },
)
async def proo(e):
    "If you think you're pro, try this."
    txt = random.choice(deadlymemes.PRO_STRINGS)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="react ?([\s\S]*)",
    command=("react", plugin_category),
    info={
        "header": "Make your userbot react",
        "types": [
            "happy",
            "think",
            "wave",
            "wtf",
            "love",
            "confused",
            "dead",
            "sad",
            "dog",
        ],
        "usage": ["{tr}react <type>", "{tr}react"],
    },
)
async def _(e):
    "Make your userbot react."
    input_str = e.pattern_match.group(1)
    if input_str in "happy":
        emoticons = deadlymemes.FACEREACTS[0]
    elif input_str in "think":
        emoticons = deadlymemes.FACEREACTS[1]
    elif input_str in "wave":
        emoticons = deadlymemes.FACEREACTS[2]
    elif input_str in "wtf":
        emoticons = deadlymemes.FACEREACTS[3]
    elif input_str in "love":
        emoticons = deadlymemes.FACEREACTS[4]
    elif input_str in "confused":
        emoticons = deadlymemes.FACEREACTS[5]
    elif input_str in "dead":
        emoticons = deadlymemes.FACEREACTS[6]
    elif input_str in "sad":
        emoticons = deadlymemes.FACEREACTS[7]
    elif input_str in "dog":
        emoticons = deadlymemes.FACEREACTS[8]
    else:
        emoticons = deadlymemes.FACEREACTS[9]
    txt = random.choice(emoticons)
    await edit_or_reply(e, txt)


@deadlyub.deadly_cmd(
    pattern="10iq$",
    command=("10iq", plugin_category),
    info={
        "header": "You retard !!",
        "usage": "{tr}10iq",
    },
)
async def iqless(e):
    "You retard !!"
    await edit_or_reply(e, "♿")


@deadlyub.deadly_cmd(
    pattern="fp$",
    command=("fp", plugin_category),
    info={
        "header": "send you face pam emoji!",
        "usage": "{tr}fp",
    },
)
async def facepalm(e):
    "send you face pam emoji!"
    await edit_or_reply(e, "🤦‍♂")


@deadlyub.deadly_cmd(
    pattern="bt$",
    command=("bt", plugin_category),
    info={
        "header": "Believe me, you will find this useful.",
        "usage": "{tr}bt",
    },
    groups_only=True,
)
async def bluetext(e):
    """Believe me, you will find this useful."""
    await edit_or_reply(
        e,
        "/BLUETEXT /MUST /CLICK.\n"
        "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?",
    )


@deadlyub.deadly_cmd(
    pattern="session$",
    command=("session", plugin_category),
    info={
        "header": "telethon session error code(fun)",
        "usage": "{tr}session",
    },
)
async def _(event):
    "telethon session error code(fun)."
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplicatedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await edit_or_reply(event, mentions)
