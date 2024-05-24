import asyncio
from ZeMusic import app
from config import OWNER_ID
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
import config

@app.on_message(filters.regex(r"^(بوت)$"))
async def BotMusic(client: Client, message: Message):
    
    italy = message.from_user.mention 
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 5145609515:
            rank = f"""<a href="tg://user?id={user_id}">مـطـور السـورس</a>"""
        elif user_id == OWNER_ID:
            rank = f"""<a href="tg://user?id={user_id}">Dev🏅</a>"""
        else:
            rank = italy
    except Exception as e:
        print(e)
    await message.reply_text(f"<b> مرحباً عزيزي :</b> {rank}\n<b> انا بوت لتشغيل لاغاني في المكالمات الصوتيه 🍻  </b>")

        


@app.on_message(filters.regex(r"^(ايديي|id)$"))
async def IdMusic(client: Client, message: Message):
    await message.reply_text(f"<b>-» ID : ›</b> <code>{message.from_user.id}</code>")




@app.on_message(filters.regex(r"^(اسمي)$"))
async def NameMusic(client: Client, message: Message):
    await message.reply_text(f"<b> اسمك : ›</b> {message.from_user.mention}")



@app.on_message(filters.regex(r"^(يوزري)$"))
async def UserMusic(client: Client, message: Message):
    await message.reply_text(f"<b> يوزرك : ›</b> @{message.from_user.username}")



@app.on_message(filters.regex(r"^(البايو)$"))
async def BioMusic(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    bio = usr.bio
    await message.reply_text(f"""<b> البايو : ›</b> {bio}""")
    



@app.on_message(filters.regex(r"^(بوت الحذف|رابط الحذف)$"))
async def DeletMusic(client: Client, message: Message):
    await message.reply_text(f"""<b> بوت الحذف : ›</b> ( @DTeLebot )\n\n<b> رابط الحذف : ›</b> ( <a href="https://my.telegram.org/auth?to=delete">اضغط هنا</a> )""")


