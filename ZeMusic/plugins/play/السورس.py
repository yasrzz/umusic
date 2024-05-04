import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/e78d5b10a33e13c420596.jpg",
        caption = f"""<b> .<b>\n<a href="https://t.me/ngd_1"> 𝐬𝐨𝐮𝐫𝐜𝐞 𝐚𝐥𝐢𝐜𝐞🧚 </a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " المطور  ", url=f"https://t.me/ngd_2"),
                ],[
                    
                
                    InlineKeyboardButton(
                        " السورس ", url=f"https://t.me/ngd_1"),         
                ],

            ]

        ),

    )
