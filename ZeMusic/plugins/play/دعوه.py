
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
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"<b>تم انهاء مكالمة الفيديو مدتها {da} ثواني وصكرها</b> ")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f" <b>تم انهاء مكالمة الفيديو مدتها دقيقه</b>")
        elif 2 <= ma[0] < 3:
            await message.reply(f" <b>تم انهاء مكالمة الفيديو مدتها دقيقتين</b> ")
        elif 3 <= ma[0] < 11:
            await message.reply(f"<b>تم انهاء مكالمة الفيديو مدتها {ma[0]} دقايق</b> ")  
        else:
            await message.reply(f"<b>تم إنهاء مكالمة الفيديو مدتها {ma[0]} دقيقه</b>")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"<b>تم انهاء مكالمة الفيديو مدتها ساعه</b> ")
        elif 2 <= ho[0] < 3:
            await message.reply(f"<b>تم انهاء مكالمة الفيديو مدتها ساعتين</b> ")
        elif 3 <= ho[0] < 11:
            await message.reply(f"<b>تم انهاء مكالمة الفيديو مدتها {ho[0]} ساعات</b> ")  
        else:
            await message.reply(f"<b>تم إنهاء مكالمة الفيديو مدتها {ho[0]} ساعة</b> ")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"<b>تم انهاء مكالمة الفيديو مدتها يوم</b> ")
        elif 2 <= day[0] < 3:
            await message.reply(f" <b>تم انهاء مكالمة الفيديو مدتها يومين</b> ")
        elif 3 <= day[0] < 11:
            await message.reply(f" <b>تم انهاء مكالمة الفيديو مدتها {day[0]} ايام</b> ")  
        else:
            await message.reply(f" <b>تم إنهاء مكالمة الفيديو مدتها {day
