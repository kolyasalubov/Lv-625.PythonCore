# # Python Crypto Converter Project

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
from datetime import datetime

class RealTimeCryptoConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount
        if from_currency != 'btc' : 
            amount = amount / self.currencies[from_currency]['value'] 
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency]['value'], 8)
        global name_f
        name_f = self.currencies[from_currency]['name'] 
        global name_t
        name_t = self.currencies[to_currency]['name'] 
        return amount

class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        datetime.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        #self.configure(background = 'blue')
        self.geometry("500x400")
        
        # Label
        self.intro_label = Label(self, text = 'Welcome to Real Time Crypto Converter',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font = ('Courier',15,'bold'))

        self.intro_label.place(x = 25 , y = 25)

        # self.date_label = Label(self, text = f"1 from_curr equals = {converter.convert('INR','USD',1)} USD \n Date : {converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
        self.dt_string = datetime.now()
        self.dt_string = self.dt_string.strftime("%d/%m/%Y %H:%M:%S")
        self.date_label = Label(self, text = f"Date : {self.dt_string}", relief = tk.FLAT, borderwidth = 3)

        self.date_label.place(x = 185, y= 80)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
        self.conversion_result_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("eth") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("btc") # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x = 30, y= 120)
        self.amount_field.place(x = 36, y = 150)
        self.to_currency_dropdown.place(x = 340, y= 120)
        #self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x = 346, y = 150)
        self.conversion_result_field_label.place(x = 195, y = 200)

        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x = 225, y = 135)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 8)

        self.converted_amount_field_label.config(text = str(converted_amount))
        self.conversion_result_field_label.config(text = str(amount) + " " + str(name_f) + "\n equals \n" + str(converted_amount) + " " +  str(name_t)) 
               
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
    url = 'https://api.coingecko.com/api/v3/exchange_rates'
    converter = RealTimeCryptoConverter(url)

    App(converter)
    mainloop()