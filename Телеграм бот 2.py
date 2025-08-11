import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '7661401720:AAEcwGurnAN4FU3Nqd660D8C7VAERXerY9E'
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Створення клавіатури
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Привіт")
    button2 = KeyboardButton("Почати")
    keyboard.add(button1, button2)

    # Надсилання повідомлення з кнопками
    bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)

# Обробка текстових повідомлень (реакція на кнопки)
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Привіт":
        bot.send_message(message.chat.id, "Привіт! Як у тебе справи?")
    elif message.text == "Почати":
        bot.send_message(message.chat.id, "Давай почнемо! Що саме тебе цікавить?")
    else:
        bot.send_message(message.chat.id, "Невідома команда, спробуй натиснути кнопку😊")
# Запуск бота
bot.polling()
