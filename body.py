import pygame
from scipy.constants import G
# import 

class Body(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, mass:float, velocity: tuple, acceleration: tuple, body_group) -> None:
        super().__init__()
        self.x_pos= pos[0]
        self.y_pos = pos[1]
        self.x_v = velocity[0]
        self.y_v = velocity[1]
        self.x_a = acceleration[0]
        self.y_a = acceleration[1]
        self.mass = mass
        self.body_group = body_group

        self.pos = pygame.math.Vector2(pos)
        

    def draw(self, screen):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, 10, 10)
        pygame.draw.rect(screen, "red", self.rect)
    
    def update(self, dt):
        # Update acceleration
        for body in self.body_group:
            if body != self:
                distance = self.pos.distance_to(body.pos)
                self.x_a = (0.1 * body.mass) / (distance**2)
                self.y_a = (0.1 * body.mass) / (distance**2)
                # print(self.x_a)


        # Update velocity
        self.x_v += self.x_a * dt
        self.y_v += self.y_a * dt

        # Update position
        self.x_pos += self.x_v * dt
        self.y_pos += self.y_v * dt
        # if self.y >= 600:
        #     self.kill()