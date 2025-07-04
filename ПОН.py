try:
    nomer1 = float(input("Введіть перше число"))
    nomer2 = float(input("Введіть друге чисто"))
    total = nomer1 + nomer2
    print("Сума чисел", total)
except ValueError:
    print("Тут числа писати а не букви ти шо? Чи замість тебе кіт пише")