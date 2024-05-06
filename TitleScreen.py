import pygame
import pygame_menu

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode((600, 700))

# Variables to control game states
in_menu = True  # Controls whether the menu is active

# Game setup (assuming you have functions like this set up)
def start_the_game():
    global in_menu
    in_menu = False
    game_loop()

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Add your game event handling logic here

        # Update game display and logic
        pygame.display.flip()

# Main Menu Setup
def setup_menu():
    global in_menu
    in_menu = True
    menu = pygame_menu.Menu('Welcome', 600, 600, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Play as :', [('X (go first)', 1), ('O (go second)', 2)])
    menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)])
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)

# Main application loop
while True:
    if in_menu:
        setup_menu()
    else:
        game_loop()

pygame.quit()
