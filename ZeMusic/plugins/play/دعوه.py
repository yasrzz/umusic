
from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from ZeMusic.utils.database import get_assistant
from pyrogram.types import Message
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic.core.call import Mody


@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("<b>‹   تم بدء المكالمه الي وده يسمعنا صوته يتفضل🍻</b>")
       

@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("<b>‹ - تم انهاء المحادثه الصوتية 🙁</b>")


@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"-الحلو {message.from_user.mention} \n- يبيك تصعد :"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass
