import pygame
import math
from scipy.constants import G
# import 

class Body(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, mass:float, velocity: tuple, acceleration: tuple, body_group, dt) -> None:
        super().__init__()
        self.pos = pygame.math.Vector2(pos)

        self.x_current_pos = self.pos[0]
        self.y_current_pos = self.pos[1]

        self.x_v = velocity[0]
        self.y_v = velocity[1]

        self.x_previous_pos = self.x_current_pos - self.x_v * dt
        self.y_previous_pos = self.y_current_pos - self.y_v * dt

        self.x_a = acceleration[0]
        self.y_a = acceleration[1]
        
        self.mass = mass
        self.body_group = body_group
        self.dt = dt

        print(self.pos)
        
    def draw(self, screen):
        self.rect = pygame.Rect(self.x_current_pos, self.y_current_pos, 10, 10)
        pygame.draw.rect(screen, "red", self.rect)
    
    def update(self):
        # Reset acceleration
        self.x_a = 0
        self.y_a = 0
        # Update acceleration
        for body in self.body_group:
            if body != self:
                # Calculate distance
                distance = self.pos.distance_to(body.pos)
                dx = body.x_current_pos - self.x_current_pos
                dy = body.y_current_pos - self.y_current_pos
                
                # Calculate acceleration
                acceleration = (1000 * body.mass) / (distance**2)
                self.x_a += acceleration * (dx / distance)
                self.y_a += acceleration * (dy / distance)
                # print(self.x_a)


        # # Update velocity
        # self.x_v += self.x_a * dt
        # self.y_v += self.y_a * dt

        # Update position
        self.x_next_pos = get_pos(self.x_current_pos, self.x_previous_pos, self.x_a, self.dt)
        self.y_next_pos = get_pos(self.y_current_pos, self.y_previous_pos, self.y_a, self.dt)

        self.x_previous_pos = self.x_current_pos
        self.y_previous_pos = self.y_current_pos

        self.x_current_pos = self.x_next_pos
        self.y_current_pos = self.y_next_pos
        # if self.y >= 600:
        #     self.kill()

# Helper function
def get_pos(current_pos, previous_pos, acceleration, dt):
    """Return the next position using Verlet integration."""
    next_pos = (2 * current_pos) - previous_pos + (acceleration * dt**2)
    return next_pos