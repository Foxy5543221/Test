import telebot
import requests

# Токени
TELEGRAM_BOT_TOKEN = "8015222903:AAGJG3mIMZA-3LFHxjgUinlQ5VxrQb79kDo"  # токен учня
COHERE_API_KEY = "ea8f495e-487c-4a6f-bc80-245c22322a63"             # токен учня
COHERE_API_URL = "https://api.cohere.ai/v1/generate"                  # рядок без змін

# Ініціалізація бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Налаштування режиму та стилю відповіді
RESPONSE_MODE = "детально"
RESPONSE_STYLE = "серйозний"


def generate_text(prompt):
    global RESPONSE_MODE, RESPONSE_STYLE

    # Якщо стиль "жартівливий", додаємо інструкцію
    if RESPONSE_STYLE == "жартівливий":
        prompt = f"Зроби, щоб відповідь була веселою: {prompt}"

    # Визначення кількості токенів
    max_tokens = 50 if RESPONSE_MODE == "коротко" else 100
    max_tokens = min(max_tokens, 256)

    # Заголовки запиту
    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json"
    }

    # Тіло запиту
    data = {
        "model": "command",
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.8,
        "p": 0.75,
        "k": 0
    }

    # Надсилання запиту до API
    response = requests.post(COHERE_API_URL, json=data, headers=headers)
    return response.json()
