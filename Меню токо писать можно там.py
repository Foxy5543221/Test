import tkinter as tk

root = tk.Tk()
root.title("Простий редактор для панелі інструменті")
root.geometry("400x400")
# Створюємо фрейм для панелі
toolinctrymenti = tk.Frame(root, bd=1, relief=tk.RAISED)
# Кнопка "Нове"
new_button = tk.Button(toolinctrymenti, text="Нове", command=new_file)
new_button.pack(side=tk.LEFT, padx=2, pady=2)
# Кнопка "Зберегти"
new_button = tk.Button(toolinctrymenti, text="Зберегти", command=new_file)
new_button.pack(side=tk.LEFT, padx=2, pady=2)
# Кнопка "Відкрити"
new_button = tk.Button(toolinctrymenti, text="Відкрити", command=new_file)
new_button.pack(side=tk.LEFT, padx=2, pady=2)
# Кнопка "Вирізати"
cut_button = tk.Button(toolinctrymenti, text="Вирізати", command=new_file)
cut_button.pack(side=tk.LEFT, padx=2, pady=2)
# Кнопка "Копіювати"