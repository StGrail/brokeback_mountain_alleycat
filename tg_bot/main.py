import asyncio

from aiogram import executor

from config.utils import dp
from handlers.admins_info import on_startup_notify_admin


async def on_startup(dp):
    pass
    # await on_startup_notify_admin(dp)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
