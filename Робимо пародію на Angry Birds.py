import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Створення вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Кольори
GREY = (125, 125, 125)
GREEN = (0, 163, 108)

# Завантаження зображень
FlyDog_img = pygame.image.load("FlyDog.png")
FlyDog_img_img = pygame.transform.smoothscale(FlyDog_img, (50, 50))  # Масштабування
Dog = FlyDog_img.get_rect()
Dog.topleft = (100, 100)  # Початкова позиція

# Фон
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Параметри руху
speed = 0          # Початкова вертикальна швидкість
gravity = 0.5      # Сила тяжіння
jump_speed = -8    # Швидкість стрибка (негативна — напрямок вгору)

# Параметри перешкод
obstacle_timer = 0
obstacles = []
obstacle_width = 50
gap_height = 150    # Відстань між верхньою і нижньою перешкодою
min_distance = 250  # Мінімальна горизонтальна відстань між перешкодами
score = 0
# Шрифт для тексту
font = pygame.font.Font(None, 36)

while True:
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed
    speed += gravity
    Dog.y += speed
    if Dog.y > 500:
        Dog.y = 550
        speed = 0
        pygame.quit()
    if Dog.y < -70:
        Dog.y = 550
        speed = 0
        pygame.quit()
    obstacle_timer += 1
    if obstacle_timer > min_distance:
        top_obstacle_height = random.randint(100,400)
        bottom_obstacle_height = screen.get_height() - top_obstacle_height - gap_height
        top_obstacle = pygame.Rect(800, 0, obstacle_width, top_obstacle_height)
        bottom_obstacle = pygame.Rect(800, screen.get_height() - bottom_obstacle_height, obstacle_width, bottom_obstacle_height)
        obstacles.append((top_obstacle, bottom_obstacle))
        obstacle_timer = 0
        for top_obstacle, bottom_obstacle in obstacles:
            # Рухаємo перешкоди вліво
            top_obstacle.x -= 5
            bottom_obstacle.x -= 5

            # Перевірка на зіткнення з котом
            if Dog.colliderect(top_obstacle) or Dog.colliderect(bottom_obstacle):
                print("Game Over!")
                print(f"Кількість очок: {score}")
                pygame.quit()
                exit()

            # Видаляємо перешкоду, якщо вона вийшла за межі екрану
            if top_obstacle.x < -obstacle_width:
                score += 1
                obstacles.remove((top_obstacle, bottom_obstacle))

        # Малюємо кота
        screen.blit(FlyDog_img, Dog.topleft)

        # Малюємо перешкоди
        for top_obstacle, bottom_obstacle in obstacles:
            pygame.draw.rect(screen, GREEN, top_obstacle)
            pygame.draw.rect(screen, GREEN, bottom_obstacle)

        score_text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        clock.tick(60)


