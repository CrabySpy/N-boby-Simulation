import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self, text, pos, size, font):
        super().__init__()
        self.text = text
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.rect = pygame.Rect(pos, size)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect, border_radius=8)
        label = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(label, label.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        return self.rect.collidepoint(event.pos)