import pygame
from snake import Snake
from food import Food
from obstacle import get_obstacles
from test_game_logic import GameLogic

pygame.mixer.init()
eat_sound = pygame.mixer.Sound("assets/sounds/eat.wav")
gameover_sound = pygame.mixer.Sound("assets/sounds/gameover.wav")
pygame.mixer.music.load("assets/sounds/bg_music1.mp3")
pygame.mixer.music.set_volume(0.2)

def draw_snake(screen, snake):
    for segment in snake.body:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))

def draw_food(screen, food):
    pygame.draw.rect(screen, (255, 0, 0), (*food.position, 20, 20))

def draw_obstacles(screen, obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, (150, 150, 150), (*obs, 20, 20))

def draw_score(screen, font, game_logic):
    score_text = font.render(
        f"Puntaje: {game_logic.get_score()}  Nivel: {game_logic.get_level()}",
        True, (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def handle_keys(snake):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.change_direction("UP")
    elif keys[pygame.K_DOWN]:
        snake.change_direction("DOWN")
    elif keys[pygame.K_LEFT]:
        snake.change_direction("LEFT")
    elif keys[pygame.K_RIGHT]:
        snake.change_direction("RIGHT")

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Snake con niveles 🐍")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 30)

    snake = Snake()
    food = Food(snake.body)
    game_logic = GameLogic()
    speed = 10
    obstacles = get_obstacles(game_logic.get_level())
    pygame.mixer.music.play(-1)

    running = True
    while running:
        screen.fill((0, 0, 0))

        if not handle_events():
            break

        handle_keys(snake)
        snake.move()

        if snake.head() == food.position:
            eat_sound.play()
            snake.grow()
            score, level = game_logic.increase_score()
            food = Food(snake.body + obstacles)
            if score % 5 == 0:
                speed += 2
                obstacles = get_obstacles(level)

        if snake.check_collision() or snake.head() in obstacles:
            pygame.mixer.music.stop()
            gameover_sound.play()
            pygame.time.delay(2000)
            running = False

        draw_snake(screen, snake)
        draw_food(screen, food)
        draw_obstacles(screen, obstacles)
        draw_score(screen, font, game_logic)

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
