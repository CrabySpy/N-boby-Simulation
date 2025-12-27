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
BACK = "back"
QUIT = "quit"

BASIC = "basic"
CIRCULAR = "circular"
ELLIPTICAL = "elliptical"
GRAV_COLLAPSE = "gravitational collapse"

SIMULATION = "simulation"


#--------------------------
# Initialize sprite groups
body_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()

#--------------------------

clock = pygame.time.Clock()

def spawn_preset(sim_type):
    body_group.empty()

    if sim_type == BASIC:
        pass
    elif sim_type == CIRCULAR:
        body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, True, body_group))
    elif sim_type == ELLIPTICAL:
        body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, True, body_group))
    elif sim_type == GRAV_COLLAPSE:
        body_group.add(Body((WIDTH//2,HEIGHT//2), 50000, (0,0), (0,0), 40, 0, True, body_group))
    

def update(dt):
    """Updates the game once per given time dt."""
    body_group.update()
    
def draw(screen):
    """Draws objects on the screen."""
    screen.fill((0, 0, 0))

    for body in body_group:
        body.draw(screen)



def simulation_loop(screen, sim_type, fps):
    mouse_held = False

    pygame.display.set_caption("Simulation")
    
    spawn_preset(sim_type)
    
    # Game loop.
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return QUIT
                if event.key == pygame.K_b:
                    return BACK
                if event.key == pygame.K_r:
                    # Reset the simulation
                    spawn_preset(sim_type)  
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_held = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_held = False
            
            if mouse_held:
                pos = pygame.mouse.get_pos()
                velocity = (100, 0)
                acceleration = (0, 0)
                mass = 10000
                radius = 10
                is_star = False
                body_group.add(Body(pos, mass, velocity, acceleration, radius, dt, is_star, body_group))
                mouse_held = False

        # Update.
        dt = 1/fps
        update(dt)
        # Draw.
        draw(screen)
        
        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    pass