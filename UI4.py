import pygame
import pygame_menu
from Opponent import Opponent
from Board import Board

# Constants
SURFACE_COLOR = (255, 255, 255)
GRID_POS = (0, 0)
CELL_SIZE = 200
WINDOW_SIZE = (600, 600)
SPRITE_PATHS = {
    'X': 'assets/XSprite.png',
    'O': 'assets/OSprite.png',
}

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode(WINDOW_SIZE)

# Sprite Handling
class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()

# Global variables
player_letter = 'X'
ai_difficulty = 'easy'
ai_opponent = None

def set_player_letter(value, letter):
    global player_letter
    player_letter = letter  # directly use the letter since it's passed correctly from the selector

def set_ai_difficulty(value, difficulty):
    global ai_difficulty
    ai_difficulty = difficulty[1]

def start_the_game():
    global ai_opponent
    ai_opponent = Opponent('O' if player_letter == 'X' else 'X', difficulty=ai_difficulty)
    run_game()

def run_game():
    global player_letter, ai_opponent
    board = Board()
    running = True
    player_turn = player_letter == 'X'  # Player starts if they chose 'X'
    sprite_group = pygame.sprite.Group()
    
    # Initialize the display once before the loop
    update_display(board, sprite_group)
    pygame.display.flip()

    # If player is 'O', AI makes the first move
    if not player_turn:
        row, col = ai_opponent.playTurn(board)
        board.setLetter(ai_opponent.letter, row, col)
        update_display(board, sprite_group)  # Update display after AI's move
        pygame.display.flip()
        player_turn = True

    while running:
        game_status = board.isGameDone()
        if game_status != "In Progress":
            print(f"Game Over: {game_status}")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and player_turn:
                x, y = event.pos
                col = (x - GRID_POS[0]) // CELL_SIZE
                row = (y - GRID_POS[1]) // CELL_SIZE
                if 0 <= row < 3 and 0 <= col < 3 and board.boardArray[row][col] == '-':
                    if board.setLetter(player_letter, row, col):
                        player_turn = False  # Switch turn to AI
                        update_display(board, sprite_group)
                        pygame.display.flip()

        if not player_turn and game_status == "In Progress":
            row, col = ai_opponent.playTurn(board)
            board.setLetter(ai_opponent.letter, row, col)
            player_turn = True  # Switch turn back to player
            update_display(board, sprite_group)
            pygame.display.flip()

    pygame.quit()


def update_display(board, sprite_group):
    sprite_group.empty()
    surface.fill(SURFACE_COLOR)

    # Draw board background first
    board_background = Sprite("assets/BoardSprite.png")
    board_background.rect.x, board_background.rect.y = GRID_POS
    sprite_group.add(board_background)

    # Draw X or O sprites only
    for row in range(board.size):
        for col in range(board.size):
            letter = board.boardArray[row][col]
            if letter in ['X', 'O']:  # Only add sprites for 'X' or 'O'
                sprite = Sprite(SPRITE_PATHS[letter])
                sprite.rect.x = GRID_POS[0] + col * CELL_SIZE
                sprite.rect.y = GRID_POS[1] + row * CELL_SIZE
                sprite_group.add(sprite)
    sprite_group.draw(surface)

# Menu Setup
menu = pygame_menu.Menu('Welcome', 600, 600, theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Play as :', [('X (go first)', 'X'), ('O (go second)', 'O')], onchange=set_player_letter)
menu.add.selector('Difficulty :', [('Easy', 'easy'), ('Medium', 'med'), ('Hard', 'hard')], onchange=set_ai_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
