from game import run_game
import pygame
import sys
from button import Button
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Niveles 🐍")

WHITE = (255, 255, 255)
GRAY = (30, 30, 30)
PURPLE = (180, 0, 255)
BLUE = (50, 150, 255)

font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.SysFont("Arial", 24)

class Particle:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = random.randint(600, 700)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def move(self):
        self.y -= self.speed
        if self.y < -10:
            self.y = random.randint(600, 700)
            self.x = random.randint(0, 600)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

particles = [Particle() for _ in range(100)]

def draw_particles():
    for p in particles:
        p.move()
        p.draw(screen)

def draw_credits():
    text1 = small_font.render("Creado por: Tu Nombre", True, WHITE)
    text2 = small_font.render("Universidad ", True, WHITE)
    screen.blit(text1, (10, 550))
    screen.blit(text2, (10, 575))

def draw_decor():
    pygame.draw.rect(screen, PURPLE, (0, 0, 600, 20))
    pygame.draw.rect(screen, PURPLE, (0, 580, 600, 20))
    pygame.draw.circle(screen, BLUE, (50, 50), 10)
    pygame.draw.circle(screen, BLUE, (550, 50), 10)

def main_menu():
    clock = pygame.time.Clock()
    title_y = 80
    color_shift = 0
    while True:
        screen.fill(GRAY)
        color_shift = (color_shift + 1) % 255
        dynamic_color = (color_shift, 100, 255 - color_shift)
        title = font.render("Snake Niveles 🐍", True, dynamic_color)
        screen.blit(title, (150, title_y))

        start_button = Button("Iniciar", 200, 220, 200, 60)
        credits_button = Button("Créditos", 200, 300, 200, 60)
        quit_button = Button("Salir", 200, 380, 200, 60)

        draw_particles()
        draw_decor()
        draw_credits()

        if start_button.draw(screen):
            run_game()
        if credits_button.draw(screen):
            show_credits()
        if quit_button.draw(screen):
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

def show_credits():
    clock = pygame.time.Clock()
    while True:
        screen.fill((10, 10, 10))
        credit_lines = [
            "Proyecto desarrollado en Python 🐍",
            "Utiliza la librería pygame",
            "Incluye niveles, obstáculos y sonidos 🎵",
            "Desarrollado por: Tu Nombre",
            "Para: Curso de Tecnologías / Ingeniería de Sistemas",
            "2025 - Universidad Ejemplo",
            "Presiona ESC para volver"
        ]
        for i, line in enumerate(credit_lines):
            text = small_font.render(line, True, WHITE)
            screen.blit(text, (50, 100 + i * 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main_menu()
