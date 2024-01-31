from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Mikobot import Mikobot
import requests

@Mikobot.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m = await message.reply_text("`processing...`")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url
    caption = f"""
๏ sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 
๏ ᴡʀɪᴛᴛᴇɴ ʙʏ » **@Nexuko_robot**
๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ » {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)