import logging

from aiogram import Dispatcher

from config import settings
from constants import STARTUP_MESSAGE_FOR_ADMINS


async def on_startup_notify_admin(dp: Dispatcher):
    try:
        if not settings.DEBUG:
            await dp.bot.send_message(chat_id=settings.MY_TG_ID, text=STARTUP_MESSAGE_FOR_ADMINS)
        else:
            await dp.bot.send_message(chat_id=settings.MY_TG_ID, text='TEST')
    except Exception as e:
        logging.exception(e)
