import pygame

position = pygame.math.Vector2(100, 150)

print(f"X: {position.x}, Y: {position.y}")

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

rect_position = pygame.math.Vector2(300, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), (rect_position.x, rect_position.y, 50, 50))

    pygame.display.flip()

pygame.quit()
