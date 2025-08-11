import tkinter as tk
import random

ideas = [
    "Створи додаток для планування справ",
    "Гра 'Вгадай число'",
    "Словничок нових слів",
    "Міні-калькулятор",
    "Генератор паролів"
]

def generator_idea():
    idea = random.choice(ideas)
    idea_label.config(text=idea)

root = tk.Tk()
root.title("Генератор ідей")

idea_label = tk.Label(root, text="Натисни кнопку, щоб отримати ідею!", font=("Arial", 14))
idea_label.pack(pady=20)

generate_button = tk.Button(root, text="Генерувати ідею 💡", command=generate_idea, font=("Arial", 12))
generate_button.pack(pady=10)

root.mainloop()