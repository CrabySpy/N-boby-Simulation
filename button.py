import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self, text, pos, size, font):
        super().__init__()
        self.text = text
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.rect = pygame.Rect(pos, size)
        
        # Colors
        self.base_color = (200, 200, 200)
        self.hover_color = (170, 170, 170)
        self.text_color = (0, 0, 0)

        

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        # Change color on hover
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.base_color

        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        label = self.font.render(self.text, True, self.text_color)
        screen.blit(label, label.get_rect(center=self.rect.center))


    def is_clicked(self, event):
        """Return true if and only if the mouse click on the button."""
        return self.rect.collidepoint(event.pos)