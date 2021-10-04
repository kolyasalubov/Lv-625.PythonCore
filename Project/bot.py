from aiogram.types import Message, ReplyKeyboardRemove
import requests
from datetime import datetime
from config import token, open_weather_token
from aiogram import Bot, Dispatcher, executor
import random
import markup as key

bot = Bot(token=token, parse_mode = "HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    sticker = open("G:\VSCode\HW\Project\stickers\welcome.webp", "rb")
    await bot.send_sticker(message.chat.id, sticker)
    await message.answer("<b>Welcome {0.first_name}!\nWrite the name of the city whose weather you want to see:</b>".format(message.from_user), reply_markup = key.main_menu)

@dp.message_handler(commands=['bye'])
async def stop(message: Message):
    our_time = datetime.now().strftime("%H")
    t = int(our_time)
    if  t > 7 and t < 18:
       bye = open("G:/VSCode/HW/Project/stickers/bye.tgs", "rb")
       await bot.send_sticker(message.chat.id, bye)
       await message.answer("<b>Goodbye! Have a nice day.</b>", reply_markup = ReplyKeyboardRemove())
    else:
        bye = open("G:/VSCode/HW/Project/stickers/bye.tgs", "rb")
        await bot.send_sticker(message.chat.id, bye)
        await message.answer("<b>Good evening! See you soon.<b>", reply_markup = ReplyKeyboardRemove()) 
        
@dp.message_handler(commands = ["random_number"])
async def keyboard(message: Message):
    if message.text == "/random_number":
        await bot.send_message(message.chat.id, random.randint(0, 1000))


@dp.message_handler()
async def weather(message: Message):
    try:

        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        
        data = req.json()


        curent_weather = data["main"]["temp"]
        t_min = data["main"]["temp_min"]
        t_max = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.fromtimestamp(data["sys"]["sunset"])
        await message.answer(f"<b>{datetime.now().strftime('%d-%m-%Y %H-%M')}\n</b>"
              f"<b>Weather in  {message.text.capitalize()}\nTemperature: {curent_weather}C°\n</b>"
              f"<b>Min temperature: {t_min}C°\nMax temperature: {t_max}C°\n</b>"
              f"<b>Humidity: {humidity}%\n</>"
              f"<b>Sunrise time: {sunrise_time}\nSunset time: {sunset_time}</b>")
        s_weather = float(curent_weather)
        if s_weather < 10:
            sti = open("G:\VSCode\HW\Project\stickers\cold.webp", "rb")
            await bot.send_sticker(message.chat.id, sti)
            await message.answer("<b>It\'s cold outside, put on something warm.</b>")
        elif s_weather > 10 and s_weather < 17:
            sti = open("G:/VSCode/HW/Project/stickers/good.webp", "rb")
            await bot.send_sticker(message.chat.id, sti)
            await message.answer("<b>On the street is not hot and not cold temperature, can wear something lighter.</b>")
        elif s_weather > 17:
            sti = open("G:\VSCode\HW\Project\stickers\warm.webp", "rb")
            await bot.send_sticker(message.chat.id, sti)
            await message.answer("<b>It\'s hot outside, dress lightly.</b>")

    except:
        await message.answer("\U000026A0 Check the city name \U000026A0")
        

if __name__ == "__main__":
    executor.start_polling(dp)
