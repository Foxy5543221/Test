from idlelib.debugger_r import restart_subprocess_debugger

import telebot
from telebot import types

TOKEN = "7661401720:AAEcwGurnAN4FU3Nqd660D8C7VAERXerY9E"
bot = telebot.TeleBot(TOKEN)

# Конверсії
conversions = {
    'Довжина': {
        'метри': {'фути': 3.28084, 'сантиметри': 100, 'міліметри': 1000},
        'фути': {'метри': 0.3048, 'сантиметри': 30.48, 'міліметри': 304.8},
        'сантиметри': {'метри': 0.01, 'фути': 0.0328084, 'міліметри': 10},
        'міліметри': {'метри': 0.001, 'фути': 0.00328084, 'сантиметри': 0.1},
    },
    'Вага': {
        'кілограми': {'грами': 1000, 'фунти': 2.20462},
        'грами': {'кілограми': 0.001, 'фунти': 0.00220462},
        'фунти': {'кілограми': 0.453592, 'грами': 453.592},
    },
    'Обʼєм': {
        'літри': {'мілілітри': 1000, 'галони': 0.264172},
        'мілілітри': {'літри': 0.001, 'галони': 0.000264172},
        'галони': {'літри': 3.78541, 'мілілітри': 3785.41},
    }
}

user_data = {}

# Вітальне повідомлення
@bot.message_handler(commands=['convert'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Довжина', 'Вага', 'Обʼєм')
    bot.send_message(message.chat.id, " Привіт! Я допоможу тобі конвертувати величини.\n\n"
                                      "Спочатку обери категорію:", reply_markup=markup)

# Вибір категорії
@bot.message_handler(func=lambda message: message.text in conversions.keys())
def choose_category(message):
    category = message.text
    user_data[message.chat.id] = {'category': category}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for unit in conversions[category]:
        markup.add(unit)
    bot.send_message(message.chat.id, f"Обери одиницю З ЯКОЇ будемо конвертувати:", reply_markup=markup)

    bot.register_next_step_handler(message, choose_from_unit)

# Вибір одиниці З ЯКОЇ конвертуємо
def choose_from_unit(message):
    chat_id = message.chat.id
    from_unit = message.text
    category = user_data[chat_id]['category']

    if from_unit not in conversions[category]:
        bot.send_message(chat_id, " Невірна одиниця. Спробуй ще раз.")
        return

    user_data[chat_id]['from_unit'] = from_unit

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for to_unit in conversions[category][from_unit]:
        markup.add(to_unit)
    bot.send_message(chat_id, f"Обери одиницю В ЯКУ конвертувати:", reply_markup=markup)

    bot.register_next_step_handler(message, choose_to_unit)

# Вибір одиниці В ЯКУ конвертуємо
def choose_to_unit(message):
    chat_id = message.chat.id
    to_unit = message.text
    from_unit = user_data[chat_id]['from_unit']
    category = user_data[chat_id]['category']

    if to_unit not in conversions[category][from_unit]:
        bot.send_message(chat_id, " Невірна одиниця. Спробуй ще раз.")
        return

    user_data[chat_id]['to_unit'] = to_unit
    bot.send_message(chat_id, f"Введи числове значення для конвертації з {from_unit} в {to_unit}:")
    bot.register_next_step_handler(message, perform_conversion)

# Конвертація
def perform_conversion(message):
    chat_id = message.chat.id
    try:
        value = float(message.text)
        from_unit = user_data[chat_id]['from_unit']
        to_unit = user_data[chat_id]['to_unit']
        category = user_data[chat_id]['category']

        result = value * conversions[category][from_unit][to_unit]
        bot.send_message(chat_id, f" {value} {from_unit} = {round(result, 4)} {to_unit}")
        send_welcome(message)
    except ValueError:
        bot.send_message(chat_id, " Введи числове значення. Спробуй ще раз.")
        bot.register_next_step_handler(message, perform_conversion)

# Запуск бота
bot.polling()