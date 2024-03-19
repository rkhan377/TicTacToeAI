#separated title screen UI from main game UI for now
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def set_letter(value, letter):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.selector('Play as :', [('X (go first)', 1), ('O (go second)', 2)], onchange=set_letter)
menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)