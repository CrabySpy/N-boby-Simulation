import pygame
from simulation import simulation_loop
from menu import main_menu_loop, preset_loop

pygame.init()

#--------------------------
# Initialize constants
FPS = 60

WIDTH, HEIGHT = 1100, 800
DIMENSIONS = (WIDTH, HEIGHT)

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

clock = pygame.time.Clock()
screen = pygame.display.set_mode((DIMENSIONS))

def main():
    state = MENU
    sim_type = BASIC
    last_state = state
    

    running = True
    while running:
        if state == MENU:
            last_state = state
            state = main_menu_loop(screen, FPS)

        elif state == BACK:
            state = last_state

        elif state == PRESET:
            last_state = state
            sim_type = preset_loop(screen, FPS)

            if sim_type == QUIT:
                state = QUIT
            elif sim_type == BACK:
                state = MENU
            else:
                state = SIMULATION

        elif state == SIMULATION:
            state = simulation_loop(screen, sim_type, FPS)
        
        elif state == QUIT:
            running = False
        

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()