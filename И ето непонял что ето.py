import command
import customtkinter as ctk
import variable

BTC_TO_UAN = 4119907.27
ETH_TO_UAN = 151023.61
USDT_TO_UAN = 42.12

def convert():
    amount = float(entry_amount.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    if from_currency == "BTC":
        amount_in_uan = amount * BTC_TO_UAN
    elif from_currency == "ETH":
        amount_in_uan = amount * ETH_TO_UAN
    elif from_currency == "USDT":
        amount_in_uan = amount * USDT_TO_UAN
    elif from_currency == "UAN":
        amount_in_uan = amount

    if to_currency == "BTC":
        converted_amount = amount_in_uan / BTC_TO_UAN
    elif from_currency == "ETH":
        converted_amount = amount_in_uan / ETH_TO_UAN
    elif from_currency == "USDT":
        converted_amount = amount_in_uan / USDT_TO_UAN
    elif from_currency == "UAN":
        converted_amount = amount_in_uan

    result_label.configure(text=f"{amount} {from_currency} = {converted_amount:.4f} {to_currency}")

app = ctk.CTk()
app.title("Конвертер криптовалют")
app.geometry("400x300")

title_label = ctk.CTkLabel(app, text="Конвертер криптовалют", font=("Roboto", 18))
title_label.pack(pady=10)

entry_amount = ctk.CTkEntry(app, placeholder_text="Введи суму")
entry_amount.pack(pady=10)

from_currency_var = ctk.StringVar(value="BTC")
from_currency_menu = ctk.CTkOptionMenu(app, variable=from_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
from_currency_menu.pack(pady=5)

# Вибір валюти для конвертації в

to_currency_var = ctk.StringVar(value="UAH")
to_currency_menu= ctk.CTkOptionMenu(app, variable=to_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
to_currency_menu.pack(pady=5)
convert_button = ctk.CTkButton(app, text="Конвертувати", command=convert)
convert_button.pack(pady=10)

#Результат конвертації

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)
# Запуск програми
app.mainloop()