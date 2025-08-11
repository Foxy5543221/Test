import tkinter as tk

def change_to_red():
    root.config(bg="red")
def change_to_blue():
    root.config(bg="blue")
def change_to_green():
    root.config(bg="green")
def change_to_yellow():
    root.config(bg="yellow")
def change_to_purple():
    root.config(bg="purple")
def change_to_orange():
    root.config(bg="orange")
# Головне меню
root = tk.Tk()
root.title("Додаток для професіональних художників")
root.geometry("400x400")
# Робимо меню
menuhydognika = tk.Menu(root)
# Створюємо підменю
color_menu = tk.Menu(menuhydognika, tearoff=0)
color_menu.add_command(label="Червоний", command=change_to_red)
color_menu.add_command(label="Синій", command=change_to_blue)
color_menu.add_command(label="Зелений", command=change_to_green)
color_menu.add_command(label="Жовтий", command=change_to_yellow)
color_menu.add_command(label="Фіолетовий", command=change_to_purple)
color_menu.add_command(label="Помаранчевий", command=change_to_orange)
# Додаємо підменю на головне меню
menuhydognika.add_cascade(label="Вибір кольору", menu=color_menu)
# Додаємо головне меню до вікна
root.config(menu=menuhydognika)
root.mainloop()