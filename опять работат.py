import os
from easygui import *

path = os.path.join("data_base", "slovnik.txt")

while True:
    interface = buttonbox("Виберіть дію","Словник", ["Додати","Екзамен","Вихід"],"5.gif")

    if interface == "Додати":
        slova = multenterbox("Уведіть свої слова","Словник",["Англійська","Українська"])
        if slova:
            slova = [e.lower() for e in slova]
            with open(path, "a", encoding="utf-8") as file:
                file.write(f'{slova[0]} {slova[1]}\n')

            msgbox("Done", image="3.gif")

    elif interface == "Екзамен":
        with open(path, "r", encoding="utf-8") as file:
            score = 0
            readFile = file.readlines()

        mode = buttonbox("Оберіть мову для екзамену","Словник",["En","Ua"], "5.gif")

        if mode == "En":
            for line in readFile:
                words = line.split()
                zapitania = enterbox(f"Скажіть переклад слова - {words[0]}").lower()
                if zapitania == words[1]:
                    score +=1

        elif mode == "Ua":
            for line in readFile:
                words = line.split()
                zapitania = enterbox(f"Скажіть переклад слова - {words[1]}").lower()
                if zapitania == words[0]:
                    score +=1

        msgbox(f"Ви вгадали {score} слів із {len(readFile)}!", image="3.gif")
    else:
        msgbox("адиос мучачос!", image="3.gif")
        break
