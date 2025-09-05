import pygame

# Ініціалізація pygame
pygame.init()

# Створення вікна
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Кольори
YELLOW = (253, 253, 150)
GREEN = (5, 244, 120)

# Початкові координати квадрата
x, y = 300, 200
width, height = 50, 50
speed = 5  # Швидкість руху квадрата

# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання стану клавіш
    keys = pygame.key.get_pressed()

    # Рух квадрата
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:   # Ліворуч
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Праворуч
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:     # Вгору
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:   # Вниз
        y += speed

    # Очищення екрану
    screen.fill(YELLOW)

    # Малюємо квадрат
    pygame.draw.rect(screen, GREEN, (x, y, width, height))

    # Оновлення екрану
    pygame.display.update()

    # Кадри на секунду
    clock.tick(60)

pygame.quit()
