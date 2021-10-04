from aiogram.types import Message

from keyboards.main import all_markup
from loader import dp


@dp.message_handler(commands=['openmenu'])  #команда, щоб розпочати роботу бота
async def process_start_command(msg: Message):
    return await msg.reply(text= " Головне меню ", reply_markup=all_markup)


@dp.message_handler(commands=['aboutus']) #команда, щоб відкрити вікно інофрмацію про нас
async def unknown_message(msg: Message):
    return await msg.reply('ЦРТ - Центр Розвитку Табірництва, заснований у 2019 році і відповідає за табори у станиці '
                           'Львів')


@dp.message_handler(commands=['contacts']) #команда, щоб відкрити вікно про контакти
async def unknown_message(msg: Message):
    return await msg.reply('\nЕлектронна пошта:')