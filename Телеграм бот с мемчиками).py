import telebot
import random

TOKEN = '8015222903:AAGJG3mIMZA-3LFHxjgUinlQ5VxrQb79kDo'
bot = telebot.TeleBot(TOKEN)

UPLOAD_FOLDER = "C:\\Users\\Lenovo\\OneDrive\\Документы\\GitHub\\Test\\1\\"

memes = ["1.jpg", "2.jpg", "3.jpg"]

@bot.message_handler(content_types=['photo'])
def receive_meme(message):

    file_info = bot.get_file(message.photo[-1].file_id)

    downloaded_file = bot.download_file(file_info.file_path)

    file_name = str(len(memes) + 1) + ".jpg"
    with open(UPLOAD_FOLDER + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    memes.append(file_name)

    bot.reply_to(message, "Мем отримано і збережено!")

@bot.message_handler(commands=['meme'])
def send_random_meme(message):
    if memes:
        meme = random.choice(memes)
        with open(UPLOAD_FOLDER + meme, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Мемів поки немає :(")

bot.polling()
