import tkinter as tk
from logging import root
from tkinter import messagebox
import time
import keyboard
import mouse

def start_clicker():

    global running,delay
    clicks_per_second = int(entry.get())
    delay = 1/clicks_per_second
    messagebox.showinfo("Auto Tapai", "Auto Tapai started. Click 'ESC' to stop")
    running = True
    schedule_click()

def schedule_click():
    if running:
        mouse.click()
        time.sleep(delay)
        schedule_click()

def show_info(event):
    messagebox.showinfo("Інформація", "Це Автотапай, він буде тапати мишкою зі швидкістю, яку ти важеш!")

def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Tapai","Auto Tapai stopped.")
    root.destroy()

root = tk.Tk()
root.title("Auto Tapai")
root.geometry("300x220")
root.configure(bg= "#e0f7fa")
root.bind('i', show_info)
running = False
delay = 0
# Label: назва
title_label = tk.Label(root, text="Auto Tapai, font=(Trebuchet MS", 16, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10)


