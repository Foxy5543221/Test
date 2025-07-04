def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль"
    return a / b
a = float (input('Введіть перше число: '))
b = float (input('Введіть друге число: '))

#Виводимо результати
print(add(5, 4))