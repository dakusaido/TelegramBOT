import logging

from aiogram import executor

from handlers import dp
from utils.datbase import create_base


async def on_startup(dp):
    create_base()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup)
