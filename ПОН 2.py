import math

try:
    nomber = float(input("Введіть число:" ))
    if nomber < 0:
        print("Помилка:Ну ти шо робиш яке менше нуля з дуба впав чи шо?")
    else:
        resultat = math.sqrt(nomber)
        print("Квадратний корінь числа:", resultat)
except ValueError:
    print("Ну звону? Та ти за.... Ой задрав!")