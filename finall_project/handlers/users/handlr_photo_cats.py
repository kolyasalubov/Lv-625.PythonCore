import logging

from PIL import Image

from keyboards.inline_keyboards.photo_cats import return_markup, cat_markup
from loader import dp
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text_contains="redcat")  # команда коли обираєш документи для учасників
async def red_cat(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer (text="Red cat", reply_markup = return_markup)\


@dp.callback_query_handler(text_contains="return")
async def return_choise_cat(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer (text="Red cat", reply_markup = cat_markup)
