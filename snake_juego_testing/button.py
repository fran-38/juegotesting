import pygame

class Button:
    def __init__(self, text, x, y, width, height, color=(100, 100, 255), hover_color=(150, 150, 255), text_color=(255, 255, 255)):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        is_hovered = self.rect.collidepoint(mouse_pos)
        if is_hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        if is_hovered and click[0] == 1:
            pygame.time.delay(200)
            return True
        return False
