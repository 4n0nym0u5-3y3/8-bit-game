import pygame
import sys
import random

# Initialize pygame
pygame.init()
RESOLUTION = (720, 720)

# Random color generation
def random_color():
    return (random.randint(125, 255), random.randint(0, 255), random.randint(0, 255))

# Screen and clock setup
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

# Color definitions
WHITE = (255, 255, 255)
DARK_GRAY = (100, 100, 100)
LIGHT_GRAY = (169, 169, 169)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (65, 25, 64)

# Initialize game variables
player_color = random.choice([RED, GREEN, BLUE])
enemy_color = BLUE
player_size = 40
enemy_size = 50
player_x = 40
player_y = RESOLUTION[1] // 2
speed = 15
score = 0

# Fonts
font_small = pygame.font.SysFont('Corbel', 35)
font_large = pygame.font.SysFont('Corbel', 60)

# Function to display game over screen
def show_game_over():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 100 < mouse_pos[0] < 140 and RESOLUTION[1] - 100 < mouse_pos[1] < RESOLUTION[1] - 80:
                    pygame.quit()
                    sys.exit()

                if RESOLUTION[0] - 180 < mouse_pos[0] < RESOLUTION[0] - 100 and RESOLUTION[1] - 100 < mouse_pos[1] < RESOLUTION[1] - 80:
                    main_game_loop()

        screen.fill(BACKGROUND_COLOR)
        game_over_text = font_large.render('GAME OVER', True, WHITE)
        restart_text = font_small.render('Restart', True, WHITE)
        exit_text = font_small.render('Exit', True, WHITE)
        mouse_pos = pygame.mouse.get_pos()

        # Draw buttons
        pygame.draw.rect(screen, LIGHT_GRAY if 100 < mouse_pos[0] < 140 and RESOLUTION[1] - 100 < mouse_pos[1] < RESOLUTION[1] - 80 else DARK_GRAY, [100, RESOLUTION[1] - 100, 40, 20])
        pygame.draw.rect(screen, LIGHT_GRAY if RESOLUTION[0] - 180 < mouse_pos[0] < RESOLUTION[0] - 100 and RESOLUTION[1] - 100 < mouse_pos[1] < RESOLUTION[1] - 80 else DARK_GRAY, [RESOLUTION[0] - 180, RESOLUTION[1] - 100, 80, 20])

        screen.blit(exit_text, (100, RESOLUTION[1] - 100))
        screen.blit(restart_text, (RESOLUTION[0] - 180, RESOLUTION[1] - 100))
        screen.blit(game_over_text, (RESOLUTION[0] // 2 - 150, RESOLUTION[1] // 2 - 30))

        pygame.display.update()

# Main game loop
def main_game_loop():
    global player_x, player_y, speed, score
    player_x = 40
    player_y = RESOLUTION[1] // 2
    speed = 15
    score = 0

    enemy1_pos = [RESOLUTION[0], random.randint(50, RESOLUTION[1] - 50)]
    enemy2_pos = [random.randint(RESOLUTION[0], RESOLUTION[0] + 100), random.randint(50, RESOLUTION[1] - 100)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= 10
        if keys[pygame.K_DOWN]:
            player_y += 10

        # Background and player
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, player_color, [player_x, player_y, player_size, player_size])

        # Enemy movement
        for enemy_pos in [enemy1_pos, enemy2_pos]:
            if enemy_pos[0] > 0:
                enemy_pos[0] -= 10
            else:
                enemy_pos[0] = RESOLUTION[0] + 100
                enemy_pos[1] = random.randint(50, RESOLUTION[1] - 50)

            pygame.draw.rect(screen, enemy_color, [enemy_pos[0], enemy_pos[1], enemy_size, enemy_size])

            # Collision detection
            if player_x <= enemy_pos[0] <= player_x + player_size and player_y <= enemy_pos[1] <= player_y + player_size:
                show_game_over()

            if player_x <= enemy_pos[0] <= player_x + player_size and player_y <= enemy_pos[1] + enemy_size <= player_y + player_size:
                show_game_over()

        # Check player boundaries
        if player_y <= 0 or player_y >= RESOLUTION[1] - player_size:
            show_game_over()

        if enemy1_pos[0] <= 0:
            show_game_over()

        # Score and exit
        score_text = font_small.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (RESOLUTION[0] - 120, RESOLUTION[1] - 40))

        pygame.display.update()
        clock.tick(speed)

# Intro screen
def intro_screen():
    colox_color1, colox_color2 = random_color()
    colox_color3 = random_color()
    intro_active = True

    while intro_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 < mouse_pos[0] < 420 and 290 < mouse_pos[1] < 330:
                    main_game_loop()
                if 300 < mouse_pos[0] < 420 and 365 < mouse_pos[1] < 405:
                    pygame.quit()
                    sys.exit()

        screen.fill(BACKGROUND_COLOR)
        colox_color1 = (colox_color1 + 1) % 256
        colox_color2 = (colox_color2 + 1) % 256

        pygame.draw.rect(screen, (colox_color2, colox_color1, colox_color3[2]), [0, 0, 40, RESOLUTION[1]])
        pygame.draw.rect(screen, (colox_color2, colox_color1, colox_color3[2]), [RESOLUTION[0] - 40, 0, 40, RESOLUTION[1]])

        # Buttons
        pygame.draw.rect(screen, LIGHT_GRAY if 300 < mouse_pos[0] < 420 and 290 < mouse_pos[1] < 330 else DARK_GRAY, [300, 290, 120, 40])
        pygame.draw.rect(screen, LIGHT_GRAY if 300 < mouse_pos[0] < 420 and 365 < mouse_pos[1] < 405 else DARK_GRAY, [300, 365, 120, 40])

        title_text = font_large.render('Colox', True, (colox_color3[0], colox_color1, colox_color2))
        start_text = font_small.render('Start', True, WHITE)
        options_text = font_small.render('Options', True, WHITE)
        exit_text = font_small.render('Exit', True, WHITE)

        screen.blit(title_text, (RESOLUTION[0] // 2 - 100, 50))
        screen.blit(start_text, (300, 290))
        screen.blit(options_text, (300, 365))
        screen.blit(exit_text, (300, 440))

        pygame.display.update()
        clock.tick(60)

intro_screen()
