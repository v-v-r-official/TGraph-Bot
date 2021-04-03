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

@Client.on_callback_query(filters.regex(r'^help_btn$'))
async def help_button(bot, update):
    await update.answer()
    buttons = [[
        InlineKeyboardButton('📌 Support Group', url='https://t.me/Dx_Support'),
        InlineKeyboardButton('Update Channel 📜', url='https://t.me/DX_Botz')
        ],[
        InlineKeyboardButton('♻️Share', url='tg://msg?text=**Hey%20Broh**%F0%9F%A5%B0%2C%0A__This%20Bot%20Generate%20Telegraph%20Link__%F0%9F%94%A5%0A%0A**Bot%20Link**%20%3A-%20%40TGraphDXBot'),
        InlineKeyboardButton('Close 🔐', callback_data='cancel_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await update.edit_message_text(
        text=Translation.HELP_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html")

@Client.on_callback_query(filters.regex(r'^cancel_btn$'))
async def cancel(bot, update):
    """Cancel and delete message"""
    await update.answer()
    #await message.delete()
    await update.message.delete()