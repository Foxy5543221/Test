import time

month = time.localtime().tm_mon
print(f'Зараз в нас {month}')
# Запитуємо у человечка номер місяця народження
month = int(input("Введіть місяц твого народження (від 1 до 12): "))

# Так тут будуть пора року
if month in [12, 1, 2]:
    season = "зимою"
elif month in [3, 4, 5]:
    season = "весною"
elif month in [6, 7, 8]:
    season = "літом"
elif month in [9, 10, 11]:
    season = "осіню"
else:
    season = None

# Даємо результат
if season:
    print(f"Ти народився {season}.")
else:
    print("Введено неправильний місяц. Попробуй знову!")