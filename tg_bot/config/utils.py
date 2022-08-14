import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import settings


logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TG_SECRET_KEY)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
