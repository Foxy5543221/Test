import customtkinter as ctk

def button_pressed():
    print("Кнопка натиснута")

app = ctk.CTk()
app.title("First custom app")
button = ctk.CTkButton(app, text="Click me", command=button_pressed())
button.pack(pady=20)

app.mainloop()