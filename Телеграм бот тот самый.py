import telebot
import schedule
import time

# Токен бота
TOKEN = "8015222903:AAGJG3mIMZA-3LFHxjgUinlQ5VxrQb79kDo"
bot = telebot.TeleBot(TOKEN)

# ID користувача
CHAT_ID = 1879609348  # Введи ID чату, його можна знайти за допомогою @userinfobot

# Налаштування розкладу
def send_reminder():
    bot.send_message(CHAT_ID, "💡 Час зробити важливу справу!")

# Заплановані нагадування
schedule.every().day.at("09:00").do(send_reminder)    # Надсилає нагадування о 09:00
schedule.every().day.at("18:00").do(send_reminder)    # Надсилає нагадування о 18:00
schedule.every(1).minute.do(send_reminder)           # Надсилає нагадування кожні 2 секунди

# Основний цикл
while True:
    try:
        schedule.run_pending()        # Виконуємо заплановані завдання
        time.sleep(1)                 # Робимо паузу, щоб зменшити навантаження
    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)                 # У разі помилки робимо паузу
