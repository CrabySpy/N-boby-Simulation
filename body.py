import pygame
from pygame import Vector2
# import 

class Body(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, mass:float, velocity: tuple, acceleration: tuple, radius: int, dt: float, body_group) -> None:
        super().__init__()
        self.pos = Vector2(pos)
        self.mass = mass
        self.body_group = body_group
        self.dt = dt
        self.radius = radius

        self.current_pos = Vector2(pos)

        self.previous_pos = self.current_pos - Vector2(velocity) * dt

        self.acceleration = Vector2(acceleration)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.current_pos, self.radius)
    
    def update(self):
        # Update acceleration
        self.acceleration = get_grav_acc(self, self.body_group)

        # Update next position
        self.next_pos = get_pos(self.current_pos, self.previous_pos, self.acceleration, self.dt)

        # Update previous and current positions
        self.previous_pos = self.current_pos
        self.current_pos = self.next_pos

        # Check collision:
        # for other in self.body_group:
        #     if other != self and check_collision(self, other):
        #         pygame.sprite.Sprite.kill(self)
        #         pygame.sprite.Sprite.kill(other)
    
# Helper function
def get_grav_acc(self, body_group) -> Vector2:
    """Compute total gravitational acceleration on a body."""
    total_acc = Vector2(0, 0)
    # Calculate gravitational acceleration from other bodies
    for body in body_group:
        if body != self:
            # Calculate distance
            dx = body.current_pos.x - self.current_pos.x
            dy = body.current_pos.y - self.current_pos.y
            distance = (dx**2 + dy**2) ** 0.5 + 100

            if distance == 0:
                continue
            # Calculate acceleration
            acc = (10000 * body.mass) / (distance ** 2)
            total_acc.x += acc * (dx / distance)
            total_acc.y += acc * (dy / distance)

    return total_acc

def get_pos(current_pos, previous_pos, acceleration, dt) -> float:
    """Return the next position using Verlet integration."""
    next_pos = (2 * current_pos) - previous_pos + (acceleration * (dt ** 2))
    return next_pos

def check_collision(body_a, body_b) -> bool:
    """Return True if two circular bodies collide."""
    dx = body_b.current_pos.x - body_a.current_pos.x
    dy = body_b.current_pos.y - body_a.current_pos.y
    distance = (dx**2 + dy**2)
    radius_sum = body_a.radius + body_b.radius

    return distance <= radius_sum