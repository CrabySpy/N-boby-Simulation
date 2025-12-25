import pygame
import random
from body import Body

pygame.init()
pygame.display.set_caption("Simulation")
#--------------------------
# Initialize constants
WIDTH, HEIGHT = 1100, 800
MENU = "menu"
PRESET = "preset"
BASIC = "basic"
CIRCULAR = "basic"
ELLIPTICAL = "elliptical"
GRAV_COLLAPSE = "gravitational collapse"
SIMULATION = "simulation"
QUIT = "quit"

#--------------------------
# Initialize sprite groups
# font = pygame.font.Font("assets\font\main_menu_font.otf")

#--------------------------
# Initialize sprite groups
body_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()

#--------------------------
# Initialize global variable
spawn_timer = 0
mouse_held = False
spawn_cooldown = 0
SPAWN_INTERVAL = 0.01
#--------------------------

clock = pygame.time.Clock()

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
        velocity = (1000, 0)
        acceleration = (0, 0)
        mass = 1000
        radius = 10
        body_group.add(Body(pos, mass, velocity, acceleration, radius, dt, body_group))
        spawn_cooldown = 0
        mouse_held = False
    else:
        spawn_cooldown = 0
    
    body_group.update()
    
def draw(screen):
    """Draws objects on the screen."""
    screen.fill((0, 0, 0))

    for body in body_group:
        body.draw(screen)

def reset_game():
    """Reset the game."""
    body_group.empty()
    body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, body_group))


def simulation_loop(screen, sim_type, fps):
    global mouse_held

    pygame.display.set_caption("Simulation")
    if sim_type == BASIC:
        body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, body_group))
    elif sim_type == CIRCULAR:
        body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, body_group))
    elif sim_type == ELLIPTICAL:
        body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, body_group))
    elif sim_type == GRAV_COLLAPSE:
        body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, body_group))

    # Game loop.
    while True:
        # Event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):  # press "Q" to quit
                return QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_held = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_held = False
            
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                reset_game()
            

        # Update.
        dt = 1/fps
        update(dt)
        # Draw.
        draw(screen)
        
        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    pass