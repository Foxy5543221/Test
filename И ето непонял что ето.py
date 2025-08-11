import customtkinter as ctk

BTC_TO_UAH = 4119907.27
ETH_TO_UAH = 151023.61
USDT_TO_UAH = 42.12

def convert():
    amount = float(entry_amount.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    # Якщо конвертуємо з криптовалюти в UAH
    if from_currency == "BTC":
        amount_in_uah = amount * BTC_TO_UAH
    elif from_currency == "ETH":
        amount_in_uah = amount * ETH_TO_UAH
    elif from_currency == "USDT":
        amount_in_uah = amount * USDT_TO_UAH
    elif from_currency == "UAH":  # Якщо конвертуємо з гривні
        amount_in_uah = amount
    # Якщо конвертуємо з UAH у криптовалюту
    if to_currency == "BTC":
        converted_amount = amount_in_uah / BTC_TO_UAH
    elif to_currency == "ETH":
        converted_amount = amount_in_uah / ETH_TO_UAH
    elif to_currency == "USDT":
        converted_amount = amount_in_uah / USDT_TO_UAH
    elif to_currency == "UAH":  # Якщо конвертуємо в гривні
        converted_amount = amount_in_uah

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