import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from userbot import deadlyub

from ..funcs.managers import edit_or_reply
from . import Build_Poll, reply_id

plugin_category = "tools"


@deadlyub.deadly_cmd(
    pattern="poll(?:\s|$)([\s\S]*)",
    command=("poll", plugin_category),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(deadlypoll):
    "To create a poll"
    reply_to_id = await reply_id(deadlypoll)
    string = "".join(deadlypoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await deadlypoll.client.send_message(
                deadlypoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await deadlypoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                deadlypoll,
                "`A poll option used invalid data (the data may be too long).`",
            )
        except ForbiddenError:
            await edit_or_reply(deadlypoll, "`This chat has forbidden the polls`")
        except exception as e:
            await edit_or_reply(deadlypoll, str(e))
    else:
        deadlyinput = string.split(";")
        if len(deadlyinput) > 2 and len(deadlyinput) < 12:
            options = Build_Poll(deadlyinput[1:])
            try:
                await deadlypoll.client.send_message(
                    deadlypoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=deadlyinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await deadlypoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    deadlypoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await edit_or_reply(deadlypoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await edit_or_reply(deadlypoll, str(e))
        else:
            await edit_or_reply(
                deadlypoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )
