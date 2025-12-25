import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self, pos, font):
        super().__init__()
        self.pos = pos