import telebot
from telebot import types
import name
from name import custumer
from count import count_menu

TOKEN = '2017166440:AAGOePROUZhJqBgsHu43VIWh7UHyobDV7PM'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Латте 330мл - 35 грн', callback_data='latte'))
    markup.add(telebot.types.InlineKeyboardButton(text='Каппучино 270мл - 35 грн', callback_data='cappucino'))
    markup.add(telebot.types.InlineKeyboardButton(text='Американо 200мл - 25 грн', callback_data='americano'))
    markup.add(telebot.types.InlineKeyboardButton(text='Отправить заказ', callback_data='sendorder'))
    name.custumer=message.chat.first_name
    bot.send_message('151908043',f'{name.custumer} собирается сделать заказ...')
    bot.send_message(message.chat.id, text="Вберите желаемые напитки и нажмите 'отправить заказ':", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за выбор!')
    answer = ''
    
    if call.data == 'latte':
        name.order+=' '+call.data
        answer = 'Вы заказали Латте'
        

    elif call.data == 'cappucino':
        name.order+=' '+call.data
        answer = 'Вы заказали Каппучино'
    elif call.data == 'americano':
        name.order+=' '+call.data
        answer = 'Вы заказали Американо'
    elif call.data == 'sendorder':
        #answer = 'без обработки функцией'+name.order+ ' \n '

        answer +='Ваш заказ:\n'+count_menu(name.order) +' уже готовится'

        bot.send_message('151908043',f'{name.custumer} заказал {count_menu(name.order)}') #отправляет сообщение лично мне

    bot.send_message(call.message.chat.id, answer)



bot.polling()