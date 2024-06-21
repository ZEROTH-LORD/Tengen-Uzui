# https://github.com/ZEROTH-LORD/TengenUzui
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from TengenUzui import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/40b93b46642124605e678.jpg",
    "https://telegra.ph/file/01a2e0cd1b9d03808c546.jpg",
    "https://telegra.ph/file/ed4385c26dcf6de70543f.jpg",
    "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg",
    "https://telegra.ph/file/cce9038f6a9b88eb409b5.jpg",
    "https://telegra.ph/file/262c86393730a609cdade.jpg",
    "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg",
]

HEY_IMG = "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "👋🏼 *ʜᴇʟʟᴏ* `{}` *ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇɴɢᴇɴ ᴜᴢᴜɪ ʙᴏᴛ!* ✨"

PM_START_TEXT = "🍃ɪ ᴀᴍ ᴛᴇɴɢᴇɴ ᴜᴢᴜɪ,ɪɴsᴘɪʀᴇᴅ ʙʏ ᴛʜᴇ ғʟᴀᴍʙᴏʏᴀɴᴛ ʜᴀsʜɪʀᴀ ғʀᴏᴍ ᴅᴇᴍᴏɴ sʟᴀʏᴇʀ, ᴛᴇɴɢᴇɴ ᴜᴢᴜɪ ʙᴏᴛ ɪs ʜᴇʀᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ sᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛs ᴡɪᴛʜ ᴜɴᴍᴀᴛᴄʜᴇᴅ ғʟᴀɪʀ ᴀɴᴅ ᴘʀᴇᴄɪsɪᴏɴ. 💥\n\n*ᴡʜᴀᴛ ᴄᴀɴ ᴛᴇɴɢᴇɴ ᴜᴢᴜɪ ᴅᴏ ғᴏʀ ʏᴏᴜ?\n\nᴀᴅᴠᴀɴᴄᴇᴅ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ:* \nᴇғғᴏʀᴛʟᴇssʟʏ ᴏʀɢᴀɴɪᴢᴇ ᴀɴᴅ ᴄᴏɴᴛʀᴏʟ ɢʀᴏᴜᴘ ᴀᴄᴛɪᴠɪᴛɪᴇs ᴡɪᴛʜ ᴘᴏᴡᴇʀғᴜʟ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ᴛᴏᴏʟs.\n\n*ᴇɴʜᴀɴᴄᴇᴅ sᴇᴄᴜʀɪᴛʏ:* ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ғʀᴏᴍ sᴘᴀᴍ ᴀɴᴅ ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴀᴄᴄᴇss ᴡɪᴛʜ ʀᴏʙᴜsᴛ sᴇᴄᴜʀɪᴛʏ ғᴇᴀᴛᴜʀᴇs.\n\n*ᴄᴜsᴛᴏᴍɪᴢᴀʙʟᴇ sᴇᴛᴛɪɴɢs:* \nᴛᴀɪʟᴏʀ ᴛʜᴇ ʙᴏᴛ’s ғᴜɴᴄᴛɪᴏɴs ᴛᴏ sᴜɪᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴜɴɪǫᴜᴇ ɴᴇᴇᴅs.\n\n*ᴀᴄᴛɪᴠɪᴛʏ ᴍᴏɴɪᴛᴏʀɪɴɢ:* \nᴋᴇᴇᴘ ᴛʀᴀᴄᴋ ᴏғ ɢʀᴏᴜᴘ ɪɴᴛᴇʀᴀᴄᴛɪᴏɴs ᴀɴᴅ ᴍᴀɪɴᴛᴀɪɴ ᴀ ʜᴇᴀʟᴛʜʏ ᴄʜᴀᴛ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ.ɢᴇᴛ ʀᴇᴀᴅʏ ғᴏʀ ᴀ sᴇᴄᴜʀᴇ ᴀɴᴅ ᴡᴇʟʟ-ᴍᴀɴᴀɢᴇᴅ ᴄʜᴀᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴛʜᴀᴛ's ᴀs ғʟᴀsʜʏ ᴀɴᴅ ᴇғғᴇᴄᴛɪᴠᴇ ᴀs ᴛᴇɴɢᴇɴ ᴜᴢᴜɪ ʜɪᴍsᴇʟғ! 🌟\n\nᴛʏᴘᴇ /help ᴏʀ ᴄʟɪᴄᴋ ᴏɴ ғᴏʟʟᴏᴡɪɴɢ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs. 💡🛠️\n\nsᴛᴀʏ ғʟᴀsʜʏ, sᴛᴀʏ sᴇᴄᴜʀᴇ! ✨"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Hydra_Updates"),
        ib(text="SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
