import pygame
import pygame_menu
from Opponent import Opponent
from Board import Board

# Constants
SURFACE_COLOR = (255, 255, 255)
GRID_POS = (0, 0)
CELL_SIZE = 200
WINDOW_SIZE = (600, 700)
pygame.display.set_mode(WINDOW_SIZE)
FEEDBACK_AREA_HEIGHT = 100
FEEDBACK_AREA_COLOR = (230, 230, 230)  # Light gray for visibility
TEXT_COLOR = (0, 0, 0)  # Black text
FONT_SIZE = 24
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
    player_turn = player_letter == 'X'
    turn_number = 1
    sprite_group = pygame.sprite.Group()
    
    # Initial display update
    update_display(board, sprite_group)
    draw_feedback(surface, turn_number, player_turn, "In Progress")  # Initial feedback
    pygame.display.flip()

    # If player is 'O', AI makes the first move
    if not player_turn:
        row, col = ai_opponent.playTurn(board)
        board.setLetter(ai_opponent.letter, row, col)
        player_turn = True  # Hand turn over to player
        update_display(board, sprite_group)  # Update display after AI's move
        draw_feedback(surface, turn_number, player_turn, "In Progress")
        pygame.display.flip()

    while running:
        game_status = board.isGameDone()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and player_turn and game_status == "In Progress":
                x, y = event.pos
                if y > FEEDBACK_AREA_HEIGHT:  # Ensure clicks are below the feedback area
                    col = (x - GRID_POS[0]) // CELL_SIZE
                    row = (y - FEEDBACK_AREA_HEIGHT - GRID_POS[1]) // CELL_SIZE
                    if 0 <= row < 3 and 0 <= col < 3 and board.boardArray[row][col] == '-':
                        if board.setLetter(player_letter, row, col):
                            player_turn = False
                            turn_number += 1
                            update_display(board, sprite_group)
                            draw_feedback(surface, turn_number, player_turn, "In Progress")
                            pygame.display.flip()

        if not player_turn and game_status == "In Progress":
            row, col = ai_opponent.playTurn(board)
            if board.setLetter(ai_opponent.letter, row, col):
                player_turn = True
                turn_number += 1
                update_display(board, sprite_group)
                draw_feedback(surface, turn_number, player_turn, "In Progress")
                pygame.display.flip()

        if game_status != "In Progress":
            running = False
            draw_feedback(surface, turn_number, player_turn, game_status)  # Display end game status
            pygame.display.flip()
            handle_end_game(surface, game_status)

    pygame.quit()


def draw_feedback(surface, turn_number, player_turn, game_status):
    pygame.draw.rect(surface, FEEDBACK_AREA_COLOR, (0, 0, 600, FEEDBACK_AREA_HEIGHT))
    font = pygame.font.Font(None, FONT_SIZE)
    if game_status == "In Progress":
        turn_info = f"Turn: {turn_number}, {'Player X' if player_turn else 'Player O'}'s turn"
    else:
        turn_info = f"Game Over! Result: {game_status}. Click to Return"

    text_surface = font.render(turn_info, True, TEXT_COLOR)
    surface.blit(text_surface, (10, FEEDBACK_AREA_HEIGHT // 2 - text_surface.get_height() // 2))

def handle_end_game(surface, game_status):
    font = pygame.font.Font(None, FONT_SIZE)
    #message = f"{game_status} - Click to return to menu"
    #text_surface = font.render(message, True, TEXT_COLOR)
    #surface.blit(text_surface, (10, FEEDBACK_AREA_HEIGHT + 10))
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the function and potentially the program
            elif event.type == pygame.MOUSEBUTTONUP:
                waiting_for_input = False
                # Reset or return to menu
                menu.mainloop(surface)


def update_display(board, sprite_group):
    sprite_group.empty()
    surface.fill(SURFACE_COLOR)

    # Draw board background first
    board_background = Sprite("assets/BoardSprite.png")
    board_background.rect.x = GRID_POS[0]
    board_background.rect.y = GRID_POS[1] + FEEDBACK_AREA_HEIGHT  # Shift board down
    sprite_group.add(board_background)

    # Draw X or O sprites on the board
    for row in range(board.size):
        for col in range(board.size):
            letter = board.boardArray[row][col]
            if letter in ['X', 'O']:  # Only draw 'X' or 'O'
                sprite = Sprite(SPRITE_PATHS[letter])
                sprite.rect.x = GRID_POS[0] + col * CELL_SIZE
                sprite.rect.y = GRID_POS[1] + row * CELL_SIZE + FEEDBACK_AREA_HEIGHT  # Shift sprites down
                sprite_group.add(sprite)
    sprite_group.draw(surface)

# Menu Setup
menu = pygame_menu.Menu('Welcome', 600, 600, theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Play as : ', [('X', 'X'), ('O', 'O')], onchange=set_player_letter)
menu.add.selector('Difficulty : ', [('Easy', 'easy'), ('Medium', 'med'), ('Hard', 'hard')], onchange=set_ai_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
