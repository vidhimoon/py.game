import pygame
import random

# Define the screen size and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My Game"

# Initialize the Pygame library
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption(SCREEN_TITLE)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a player object
player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill((255, 0, 0))
player.rect = player.image.get_rect()
player.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Create a group of enemy objects
enemies = pygame.sprite.Group()
for i in range(10):
    enemy = pygame.sprite.Sprite()
    enemy.image = pygame.Surface((50, 50))
    enemy.image.fill((0, 255, 0))
    enemy.rect = enemy.image.get_rect()
    enemy.rect.x = random.randint(0, SCREEN_WIDTH)
    enemy.rect.y = random.randint(0, SCREEN_HEIGHT)
    enemies.add(enemy)

# Create a group of bullet objects
bullets = pygame.sprite.Group()

# Game loop
while True:
    # Get the time since the last frame
    dt = clock.tick(60) / 1000  # Amount of seconds between each loop

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= 5
            elif event.key == pygame.K_RIGHT:
                player.rect.x += 5
            elif event.key == pygame.K_UP:
                player.rect.y -= 5
