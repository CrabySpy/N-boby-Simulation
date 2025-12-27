import pygame
from button import Button

pygame.init()
#--------------------------
# Initialize constants
WIDTH, HEIGHT = 1100, 800

M_BUTTON_W, M_BUTTON_H = 300, 70 # Main menu button
P_BUTTON_W, P_BUTTON_H = 200, 200 # Preset button
SPACING = 40

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
def get_font(size):
    """Return font with the given size."""
    return pygame.font.Font("assets/font/main_menu_font.otf", size)
def main_menu_loop(screen, fps):

    pygame.display.set_caption("Main Menu")
    
    menu_title = get_font(100).render("N-Body Simulation", True, "white")
    menu_tit_rect = menu_title.get_rect(center=(WIDTH / 2, 200))

    button_font = get_font(30)

    start_button = Button(
        "Start Simulation",
        (WIDTH // 2 - M_BUTTON_W // 2, HEIGHT // 2 + M_BUTTON_H // 2),
        (M_BUTTON_W, M_BUTTON_H),
        button_font
    )
    preset_button = Button(
        "Presets",
        (WIDTH // 2 - M_BUTTON_W // 2, (HEIGHT // 2 + M_BUTTON_H // 2) + 100),
        (M_BUTTON_W, M_BUTTON_H),
        button_font
    )
    quit_button = Button(
        "Quit",
        (WIDTH // 2 - M_BUTTON_W // 2, (HEIGHT // 2 + M_BUTTON_H // 2) + 200),
        (M_BUTTON_W, M_BUTTON_H),
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
                    return PRESET
                if quit_button.is_clicked(event):
                    return QUIT

        screen.fill((0, 0, 0))

        start_button.draw(screen)
        preset_button.draw(screen)
        quit_button.draw(screen)

        screen.blit(menu_title, menu_tit_rect)

        pygame.display.flip()
        clock.tick(fps)

def preset_loop(screen, fps):
    pygame.display.set_caption("Preset Menu")

    menu_title = get_font(100).render("Preset", True, "white")
    menu_title_rect = menu_title.get_rect(center=(WIDTH // 2, 200))

    button_font = get_font(30)

    # Total width of button row
    total_width = 3 * P_BUTTON_W + 2 * SPACING
    start_x = WIDTH // 2 - total_width // 2
    y_pos = HEIGHT // 2

    circ_button = Button(
        "Two-Body:\nCircular Orbit",
        (start_x, y_pos),
        (P_BUTTON_W, P_BUTTON_H),
        button_font
    )

    ellip_button = Button(
        "Two-Body:\nElliptical Orbit",
        (start_x + P_BUTTON_W + SPACING, y_pos),
        (P_BUTTON_W, P_BUTTON_H),
        button_font
    )

    grav_button = Button(
        "Gravitational\nCollapse",
        (start_x + 2 * (P_BUTTON_W + SPACING), y_pos),
        (P_BUTTON_W, P_BUTTON_H),
        button_font
    )

    back_button = Button(
        "Back",
        (WIDTH // 2 - M_BUTTON_W // 2, y_pos + P_BUTTON_H + 60),
        (M_BUTTON_W, M_BUTTON_H), 
        button_font
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                if circ_button.is_clicked(event):
                    return CIRCULAR
                if ellip_button.is_clicked(event):
                    return ELLIPTICAL
                if grav_button.is_clicked(event):
                    return GRAV_COLLAPSE
                if back_button.is_clicked(event):
                    return BACK

        screen.fill((0, 0, 0))

        screen.blit(menu_title, menu_title_rect)

        circ_button.draw(screen)
        ellip_button.draw(screen)
        grav_button.draw(screen)
        back_button.draw(screen)

        pygame.display.flip()
        clock.tick(fps)