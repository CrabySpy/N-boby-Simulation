import pygame
from button import Button

pygame.init()
#--------------------------
# Initialize constants
MENU = "menu"
SIMULATION = "simulation"
QUIT = "quit"

#--------------------------

clock = pygame.time.Clock()

def menu_loop(screen, fps):
    pygame.display.set_caption("Main Menu")
    font = pygame.font.Font("assets/font/font.ttf", 30)

    start_button = Button("Start Simulation", (300, 250), (300, 60), font)
    quit_button = Button("Quit", (300, 350), (300, 60), font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if start_button.is_clicked(event):
            #         return SIMULATION

            #     if quit_button.is_clicked(event):
            #         return QUIT

        screen.fill((20, 20, 30))

        start_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.flip()
        clock.tick(fps)