import random

randomne_chuslo = random.randint(1, 10)
#Вводимо текст який буде в початку
print('Угадай число від 1 до 10: ')
#Щяс нужно вписать While True щоб був цикл
while True:
 cheluk = int(input('Введіть число: '))

 if cheluk == randomne_chuslo:
  print('Вітаю! Ви вгадали число!')
 elif cheluk < randomne_chuslo:
    print('Неправильне число! Загадане число більше!')
 else:
    print('Неправильне число! Загадане число менше!')
