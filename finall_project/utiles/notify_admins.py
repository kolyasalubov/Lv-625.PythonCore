import logging

from aiogram import Dispatcher

from config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот запущено і готовий до роботи")

        except Exception as err:
            logging.exception(err)