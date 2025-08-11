import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Встав токен, який надіслав BotFather
bot = telebot.TeleBot('8015222903:AAGJG3mIMZA-3LFHxjgUinlQ5VxrQb79kDo')

# Команда /start: відправляє привітання, коли користувач пише /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій новий бот 😃")

# Команда /help: відправляє повідомлення з підказками

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help, /convert, /random"
" /start запускає бота, /help і сам вже знаєш, /convert конвертує разні одиниці вимірювання,но може буди відключеним, /random вибирає рандомне число від 1 до 10")

@bot.message_handler(commands=["random"])
def random_message(message):
    a = random.randint(1,10)
    bot.reply_to(message, f'Рандомне число {a}')
    # from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
        if message.text == "Привіт":
            bot.send_message(message.chat.id, "Привіт! Як 🟨 тебе справи?")
        elif message.text == "Почати":
            keyboard = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton("Відкрити сайт середовища для програмування", url="https://codehs.com/")
            button2 = InlineKeyboardButton("Відкрити сайт школи", url="https://justschool.me/uk")
            keyboard.add(button1, button2)
            bot.send_message(message.chat.id, "Обери дію:", reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, "Я не знаю такої команди, спробуй натиснути на кнопку 😊")

# Запуск бота
bot.polling()

