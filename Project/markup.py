from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

random_button = KeyboardButton("/random_number")
stop_button = KeyboardButton("/bye")
main_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(random_button, stop_button)
