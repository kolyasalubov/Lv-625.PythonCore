from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message


from keyboards.main import all_markup
from loader import dp


@dp.message_handler(CommandStart()) 
async def process_start_command(message: Message):

    await message.answer(
        "/n".join([
            f"Привіт, " + message.from_user.full_name + ", я бот 😊 "
                                                    " Вибери, що тебе цікавить?"


        ]), reply_markup=all_markup)