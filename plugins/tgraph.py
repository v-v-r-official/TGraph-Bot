#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DforDarkAngel
# @DX_Botz

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton ,CallbackQuery
import os, shutil
from config import Config
from telegraph import upload_file
import logging
from translation import Translation

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.photo)
async def get_tgraph(bot, message):
    tmp = os.path.join("downloads",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    imgdir = tmp + "/" + str(message.message_id) +".jpg"
    dwn = await message.reply_text("`Processing...`", True)          
    await bot.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("`Uploading...`")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    shutil.rmtree(tmp,ignore_errors=True)
    
@Client.on_message(filters.video)
async def getvideo(bot, message):
    tmp = os.path.join("downloads",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    viddir = tmp + "/" + str(message.message_id) +".mp4"
    dwn = await message.reply_text("`Processing...`", True)          
    await bot.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("`Uploading...`")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    shutil.rmtree(tmp,ignore_errors=True)
    
@Client.on_message(filters.animation)
async def getanimation(bot, message):
    tmp = os.path.join("downloads",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    gifdir = tmp + "/" + str(message.message_id) +".mp4"
    dwn = await message.reply_text("`Processing...`", True)          
    await bot.download_media(
            message=message,
            file_name=gifdir
        )
    await dwn.edit_text("`Uploading...`")
    try:
        response = upload_file(gifdir)
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    shutil.rmtree(tmp,ignore_errors=True)