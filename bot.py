import asyncio
import os
import sys
import logging
from aiogram.enums import ParseMode
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher


load_dotenv()
BOT_KEY = os.getenv('BOT_KEY')

_bot = Bot(token=BOT_KEY)
dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_KEY, parse_mode=ParseMode.HTML)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

