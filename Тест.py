import pygame

pygame.init()

# Вікно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Рух об'єкта за допомогою Enter")

# Параметри об'єкта
rect_position = pygame.math.Vector2(100, 100)
object_size = 100
object_color = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                rect_position.x += 100
                rect_position.y += 200

    # Очищення екрану
    screen.fill((255, 255, 255))

    # Малюємо квадрат
    pygame.draw.rect(screen, object_color,
                     (rect_position.x, rect_position.y, object_size, object_size))

    # Оновлюємо екран
    pygame.display.flip()

pygame.quit()
