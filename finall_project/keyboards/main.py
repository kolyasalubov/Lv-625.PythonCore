from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_photo = KeyboardButton(text='Переглянути фото')
write_message = KeyboardButton(text='НАписати повідомлення') 
# team_help = KeyboardButton(text='Таборовий помічник 🔰')
# training = KeyboardButton(text='Все про мандрівки ⛰')
# crs_DMD = KeyboardButton(text='Курси домедичної допомоги ⛑')
all_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_photo).\
    add(write_message)
#Основна клавіатура
