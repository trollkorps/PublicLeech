#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

import configparser

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)
from tobrot import (
    R_CLONE_CONF_URI
)
from tobrot.helper_funcs.r_clone import (
    get_r_clone_config
)


async def get_markup(message: Message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton(
        "youtube-dl",
        callback_data=("ytdl").encode("UTF-8")
    ))
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    inline_keyboard = []

    reply_text = (
        "please select the required option"
    )
    return reply_text, reply_markup
