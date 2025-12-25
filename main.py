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
BASIC = "basic"
CIRCULAR = "basic"
ELLIPTICAL = "elliptical"
GRAV_COLLAPSE = "gravitational collapse"
PRESET = 'preset'
SIMULATION = "simulation"
QUIT = "quit"
#--------------------------

clock = pygame.time.Clock()
screen = pygame.display.set_mode((DIMENSIONS))

def main():
    state = MENU
    running = True
    sim_type = "basic"
    while running:
        if state == MENU:
            state = main_menu_loop(screen, FPS)        
        elif state == PRESET:
            sim_type = preset_loop(screen, FPS)
            state = simulation_loop(screen, sim_type, FPS)
        elif state == SIMULATION:
            sim_type = "basic"
            state = simulation_loop(screen, sim_type, FPS)

        elif state == QUIT:
            running = False

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()