from aiogram.dispatcher.filters import Text

from keyboards.inline_keyboards.photo_cats import cat_markup
from loader import dp
from aiogram.types import Message


@dp.message_handler(Text(endswith=["Переглянути фото"]))
async def choose(msg: Message):
    return await msg.answer (text="Переглянути фото котів", reply_markup=cat_markup)
