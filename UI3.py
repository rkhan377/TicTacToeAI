import pygame
import pygame_menu

# Constants
SURFACE_COLOR = (255, 255, 255)
GRID_POS = (0, 0)
CELL_SIZE = 200
WINDOW_SIZE = (600, 600)

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode(WINDOW_SIZE)

# Sprite Handling
class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()

# Setup the board and game states
SpritesList = pygame.sprite.Group()
boardSprite = Sprite("assets/BoardSprite.png")
boardSprite.rect.x, boardSprite.rect.y = GRID_POS
SpritesList.add(boardSprite)
board = [[None, None, None], [None, None, None], [None, None, None]]
playerTurn = True
playerLetter = 'X'

def run_game():
    global playerTurn, playerLetter  # Declare the use of global variables
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                col = (x - GRID_POS[0]) // CELL_SIZE
                row = (y - GRID_POS[1]) // CELL_SIZE
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] is None:
                    board[row][col] = playerLetter
                    playerTurn = not playerTurn  # Toggle player turn
                    playerLetter = 'O' if playerLetter == 'X' else 'X'  # Switch player letter

        surface.fill(SURFACE_COLOR)
        SpritesList.draw(surface)
        for row in range(3):
            for col in range(3):
                letter = board[row][col]
                if letter:
                    letter_path = f"assets/{letter}Sprite.png"
                    letter_sprite = Sprite(letter_path)
                    letter_sprite.rect.x = GRID_POS[0] + col * CELL_SIZE
                    letter_sprite.rect.y = GRID_POS[1] + row * CELL_SIZE
                    surface.blit(letter_sprite.image, letter_sprite.rect)
        pygame.display.flip()
    pygame.quit()

# Menu Setup
def start_the_game():
    menu.disable()
    run_game()

menu = pygame_menu.Menu('Welcome', 600, 600, theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Play as :', [('X (go first)', 1), ('O (go second)', 2)])
menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)])
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
