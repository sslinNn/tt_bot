import asyncio
import os
import sys
import logging

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from handlers.start import send_welcome, router
from utils.async_db_connection import init_db

load_dotenv()
BOT_KEY = os.getenv('BOT_KEY')

_bot = Bot(token=BOT_KEY)
dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_KEY)
    # , default = DefaultBotProperties(parse_mode=ParseMode.HTML)

    dp.message.register(send_welcome, CommandStart())
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio


    # Инициализация базы данных
    async def on_startup():
        await init_db()


    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
