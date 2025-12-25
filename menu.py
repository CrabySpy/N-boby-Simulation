import pygame
from button import Button

pygame.init()
#--------------------------
# Initialize constants
WIDTH, HEIGHT = 1100, 800
BUTTON_W, BUTTON_H = 300, 70
MENU = "menu"
SIMULATION = "simulation"
QUIT = "quit"

#--------------------------

clock = pygame.time.Clock()
def get_font(size):
    """Return font with the given size."""
    return pygame.font.Font("assets/font/main_menu_font.otf", size)
def menu_loop(screen, fps):
    pygame.display.set_caption("Main Menu")
    

    menu_title = get_font(100).render("N-Body Simulation", True, "white")
    menu_tit_rect = menu_title.get_rect(center=(WIDTH / 2, 200))

    # start_button = Button("Start Simulation", (WIDTH // 2 + 300, 250), (300, 60), font)
    # quit_button = Button("Quit", (300, 350), (300, 60), font)
    button_font = get_font(30)
    start_button = Button(
        "Start Simulation",
        (WIDTH // 2 - BUTTON_W // 2, HEIGHT // 2 + BUTTON_H // 2),
        (BUTTON_W, BUTTON_H),
        button_font
    )
    preset_button = Button(
        "Presets",
        (WIDTH // 2 - BUTTON_W // 2, (HEIGHT // 2 + BUTTON_H // 2) + 100),
        (BUTTON_W, BUTTON_H),
        button_font
    )
    quit_button = Button(
        "Quit",
        (WIDTH // 2 - BUTTON_W // 2, (HEIGHT // 2 + BUTTON_H // 2) + 200),
        (BUTTON_W, BUTTON_H),
        button_font
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event):
                    return SIMULATION
                if preset_button.is_clicked(event):
                    print("preset is clicked")
                if quit_button.is_clicked(event):
                    return QUIT

        screen.fill((0, 0, 0))

        start_button.draw(screen)
        preset_button.draw(screen)
        quit_button.draw(screen)

        screen.blit(menu_title, menu_tit_rect)

        pygame.display.flip()
        clock.tick(fps)
