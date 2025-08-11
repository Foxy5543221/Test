#menu
import tkinter as tk
# робимо головне вікно
root = tk.Tk()
root.title("Что ето такое?!")
# Створюємо меню
Ctoto = tk.Menu(root)
# Додаємо пункт перший ну щоб пусто небуло
file_menu1 = tk.Menu(Ctoto, tearoff=0)
file_menu1.add_command(label= "OPEN THE DOOR!")
file_menu1.add_command(label= "Save your live!")
file_menu1.add_command(label= "Вийди від сюда розбійник!")
# Додаємо другий пункт меню
file_menu2=tk.Menu(Ctoto, tearoff=0)
file_menu2.add_command(label="DON'T COPY MEEEEEE!")
file_menu2.add_command(label="NOOO DON'T CUT ME!")
file_menu2.add_command(label="Вставить")
# Додаємо 2 підменю в  головне меню в якому головніше меню
Ctoto.add_cascade(label="Файл.exe", menu=file_menu1)
Ctoto.add_cascade(label="Редагувати.exe", menu=file_menu2)
# Додаємо головне меню в вікно
root.config(menu=Ctoto)
root.mainloop()