import pygame
from simulation import simulation_loop
from menu import menu_loop

pygame.init()

#--------------------------
# Initialize constants
FPS = 60
WIDTH, HEIGHT = 1100, 800
DIMENSIONS = (WIDTH, HEIGHT)
MENU = "menu"
SIMULATION = "simulation"
QUIT = "quit"
#--------------------------

clock = pygame.time.Clock()
screen = pygame.display.set_mode((DIMENSIONS))

def main():
    state = SIMULATION
    running = True
    while running:
        if state == MENU:
            state = menu_loop(screen, FPS)

        elif state == SIMULATION:
            state = simulation_loop(screen, FPS)

        elif state == QUIT:
            running = False

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()