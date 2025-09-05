import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

t = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.time.get_ticks() - t > 2000:
        print("Час іде....")
        t = pygame.time.get_ticks()
