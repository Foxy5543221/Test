import telebot
('Старий код!')
# Токен бота
TOKEN = "7661401720:AAEcwGurnAN4FU3Nqd660D8C7VAERXerY9E"
bot = telebot.TeleBot(TOKEN)

# Функція для конвертації величин
def convert_units(value, from_unit, to_unit):
    # Словник коефіцієнтів для конвертації
    conversions = {
        'метри': {'фути': 3.28084, 'сантиметри': 100, 'міліметри': 1000},
        'фути': {'метри': 0.3048, 'сантиметри': 30.48, 'міліметри': 304.8},
        'сантиметри': {'метри': 0.01, 'фути': 0.0328084, 'міліметри': 10},
        'міліметри': {'метри': 0.001, 'фути': 0.00328084, 'сантиметри': 0.1},
    }

    if from_unit in conversions and to_unit in conversions[from_unit]:
        # Виконати конвертацію
        return value * conversions[from_unit][to_unit]
    else:
        return None

# Обробка команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привіт! Я допоможу конвертувати величини.\n"
                                      "Напиши в такому форматі: '5 метри в фути'.")
# Обробка текстових повідомлень
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    try:
        # Розділяємо текст на частини
        parts = text.split(" в ")
        value_and_from_unit = parts[0].split()
        to_unit = parts[1]

        # Визначаємо кількість значення і одиниці вимірювання
        value = float(value_and_from_unit[0])
        from_unit = value_and_from_unit[1]

        # Конвертуємо величину
        result = convert_units(value, from_unit, to_unit)

        if result is not None:
            bot.send_message(message.chat.id, f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            bot.send_message(message.chat.id,
                             "Перепрошую, я не можу виконати цю конвертацію.\nСпробуй ще раз.")
    except Exception as e:
        bot.send_message(message.chat.id,
                         "Сталася помилка. Переконайся, що введено правильний формат (наприклад: '5 метри в фути').")

# Запуск бота
bot.polling()