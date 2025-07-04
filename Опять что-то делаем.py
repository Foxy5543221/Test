import tkinter as tk
import random


def on_click(event):
    Label.confing(text= "Мене натиснуто!")

def change_backgroung_color(event):
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F0E68C", "#FF33A1"]
    root.config(bg=random.choice(colors))

root = tk.Tk()
Label = tk.Label(root, text="Натисни на мене", bg="lightblue")
Label.pack(padx=20, pady=20)
Label1 = tk.Label(root, text="Натисни на Enter, щоб змінити колір фону", bg="lightblue")
root.bind("<Returrn>", change_backgroung_color)

Label.bind("<Button-3>", on_click)
root.mainloop()