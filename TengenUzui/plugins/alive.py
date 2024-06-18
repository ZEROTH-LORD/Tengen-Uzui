# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/O_okarma
# PROVIDED BY https://t.me/ProjectCodeX

# <============================================== IMPORTS =========================================================>
import random
from sys import version_info

import pyrogram
import telegram
import telethon
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from ZEROTH.karma import ALIVE_ANIMATION, ALIVE_BTN
from TengenUzui import BOT_NAME, app

# <=======================================================================================================>


# <================================================ FUNCTION =======================================================>
@app.on_message(filters.command("alive"))
async def alive(_, message: Message):
    library_versions = {
        "PTB": telegram.__version__,
        "TELETHON": telethon.__version__,
        "PYROGRAM": pyrogram.__version__,
    }

    library_versions_text = "\n".join(
        [f"➲ **{key}:** `{value}`" for key, value in library_versions.items()]
    )

    caption = f"""**HEY, I AM {BOT_NAME}**

━━━━━━ 🌟✿🌟 ━━━━━━
✪ **CREATOR:** [🄺🄰🅁🄼🄰](https://t.me/anime_Freakz)

{library_versions_text}

➲ **PYTHON:** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
➲ **BOT VERSION:** `2.0`
━━━━━━ 🌟✿🌟 ━━━━━━"""

    await message.reply_animation(
        random.choice(ALIVE_ANIMATION),
        caption=caption,
        reply_markup=InlineKeyboardMarkup(ALIVE_BTN),
    )


# <=======================================================================================================>


# <================================================ NAME =======================================================>
__mod_name__ = "ALIVE"
# <================================================ END =======================================================>
