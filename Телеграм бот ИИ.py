import telebot
import requests

TELEGRAM_BOT_TOKEN = "8015222903:AAGJG3mIMZA-3LFHxjgUinlQ5VxrQb79kDo"

COHERE_API_KEY = "ea8f495e-487c-4a6f-bc80-245c22322a63"
COHERE_API_URL = "https://api.cohere.ai/v1/generate"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def generate_text(prompt):

    headers = {

        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json",

    }
    data = {

        "model": "command",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.8,
        "p": 0.75,
        "k": 0,


    }

try:
    response = requests.post(COHERE_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        if "generations" in response_data and len(response_data["generations"]) > 0:
            generation = response_data["generations"][0]["text"]
            return generation
        else:
            return "Помилка: пустий результат від API."
    else:
        return f"Помилка: {response.status_code}"
except Exception as e:
    return f"Помилка: {e}"


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напиши мені текст, і я спробую продовжити його за допомогою Cohere API.")


# Обробка текстових повідомлень
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    bot.reply_to(message, "Генерую відповідь, зачекайте...")
    generated_text = generate_text(user_input)
    bot.send_message(message.chat.id, generated_text)


if __name__ == "__main__":
    print("Бот запущено!")
    bot.polling()
