import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Рух об'єкта за допомогою Enter")
rect_position = pygame.math.Vector2(100,100)
object_size = 100
object_color = (255,0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                rect_position.x +=100
                rect_position.y +=200
    screen.fill((255,255,255))
    pygame.draw.rect(screen, object_color, (rect_position.x, rect_position.y, object_size, object_size))
    pygame.display.flip()
pygame.quit()


import pygame

# Ініціалізація pygame
pygame.init()

# Розміри вікна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Рух об'єкта за допомогою Enter")

# Початкові координати об'єкта
object_position = pygame.math.Vector2(100, 100)
object_size = 50 # Розмір об'єкта (квадрат)

# Колір об'єкта
object_color = (255, 0, 0) # Червоний

# Головний цикл гри
running = True
while running:

for event in pygame.event.get():

if event.type == pygame.QUIT:

running = False

elif event.type == pygame.KEYDOWN:

# Якщо натиснуто Enter, рухаємо об'єкт вправо

if event.key == pygame.K_RETURN:

object_position += pygame.math.Vector2(50, 0)

# Очищаємо екран
screen.fill((255, 255, 255)) # Білий фон

# Малюємо об'єкт
pygame.draw.rect(screen, object_color, (object_position.x, object_position.y, object_size, object_size))

# Оновлюємо екран
pygame.display.update()

# Затримка для зручності
pygame.time.Clock().tick(30)

pygame.quit()