import pygame
import random
from body import Body

pygame.init()

#--------------------------
# Initialize constants
FPS = 60
WIDTH, HEIGHT = 1100, 800
DIMENSIONS = (WIDTH, HEIGHT)

#--------------------------
# Initialize sprite groups
body_group = pygame.sprite.Group()

#--------------------------
# Initialize global variable
spawn_timer = 0
mouse_held = False
spawn_cooldown = 0
SPAWN_INTERVAL = 0.01

clock = pygame.time.Clock()
screen = pygame.display.set_mode((DIMENSIONS))


def update(dt):
    """Updates the game once per given time dt."""
    global spawn_timer
    global spawn_cooldown
    global mouse_held
    
    spawn_timer += dt
    if spawn_timer > 1:
        print(body_group)
        spawn_timer = 0

    if mouse_held:
        spawn_cooldown += dt
        # if spawn_cooldown >= SPAWN_INTERVAL:
        pos = pygame.mouse.get_pos()
        velocity = (0, 0)
        acceleration = (0, 0)
        mass = 1000
        body_group.add(Body(pos, mass, velocity, acceleration, body_group, dt))
        spawn_cooldown = 0
        mouse_held = False
    else:
        spawn_cooldown = 0
    
    body_group.update()
    
def draw(screen):
    """Draws objects on the screen."""
    screen.fill((30, 0, 0))

    for body in body_group:
        body.draw(screen)

def reset_game():
    """Reset the game."""
    body_group.empty()

# Game loop.
running = True
while running:
    # Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):  # press "Q" to quit
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False
        
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
            reset_game()
        

    # Update.
    dt = 1/FPS
    update(dt)
    # Draw.
    draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()