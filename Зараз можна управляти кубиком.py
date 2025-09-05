"""import pygame

# Ініціалізація Pygame
pygame.init()

# Створення вікна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Обробка клавіш")

running = True
while running:
    for event in pygame.event.get():
        # Закриття вікна
        if event.type == pygame.QUIT:
            running = False

        # Натискання клавіш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Хтось натиснув стрілочку вгору!")
            elif event.key == pygame.K_DOWN:
                print("Хтось натиснув стрілочку вниз!")
            elif event.key == pygame.K_s:
                print("S")
            elif event.key == pygame.K_w:
                print("W")
            elif event.key == pygame.K_a:
                print("A")
            elif event.key == pygame.K_SPACE:
                print("Space")
            elif event.key == pygame.K_LSHIFT:
                print("LEFT SHIFT")

        # Відпускання клавіш
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Хтось відпустив стрілочку вгору!")

# Завершення програми
pygame.quit()"""

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        # Виведення інформації про натиснуту клавішу
        if keys[pygame.K_LEFT]:
            message = "Клавіша ліворуч натиснута"
            print(message)
        elif keys[pygame.K_RIGHT]:
            message = "Клавіша праворуч натиснута"
            print(message)
        elif keys[pygame.K_UP]:
            message = "Клавіша вгору натиснута"
            print(message)
        elif keys[pygame.K_DOWN]:
            message = "Клавіша вниз натиснута"
            print(message)

pygame.quit()