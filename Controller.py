import pygame
import pygame_menu
from Opponent import Opponent
from Board import Board

# Constants
SURFACE_COLOR = (255, 255, 255)
CELL_SIZE = 200
WINDOW_SIZE = (800, 900)
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
bg_file ="assets/BoardSprite.png"
grid_size =3
grid_pos = (0,100)

def set_game_mode(value, board):
    global grid_pos, grid_size, bg_file
    if board == '3x3':
        grid_size = 3
        bg_file = "assets/BoardSprite.png"
    else:
        grid_size = 4
        bg_file ="assets/4x4Sprite.png"

def set_player_letter(value, letter):
    global player_letter
    player_letter = letter  # directly use the letter since it's passed correctly from the selector

def set_ai_difficulty(value, difficulty):
    global ai_difficulty
    ai_difficulty = difficulty

def start_the_game():
    global ai_opponent
    ai_opponent = Opponent('O' if player_letter == 'X' else 'X', difficulty=ai_difficulty)
    run_game()

def run_game():
    global player_letter, ai_opponent
    board = Board(grid_size)
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
        turn_number = 2  # Since AI made the first move
        update_display(board, sprite_group)  # Update display after AI's move
        draw_feedback(surface, turn_number, player_turn, "In Progress")
        pygame.display.flip()

    while running:
        game_status = board.isGameDone()
        draw_feedback(surface, turn_number, player_turn, game_status)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and player_turn and game_status == "In Progress":
                x, y = event.pos
                if y > FEEDBACK_AREA_HEIGHT:  # Ensure clicks are below the feedback area
                    col = (x - grid_pos[0]) // CELL_SIZE
                    row = (y - FEEDBACK_AREA_HEIGHT) // CELL_SIZE
                    if 0 <= row < grid_size and 0 <= col < grid_size and board.boardArray[row][col] == '-':
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
        if player_letter == "X":
            current_player = 'Player X' if player_turn else 'Computer O'
        else:
            current_player = 'Player O' if player_turn else 'Computer X'
        turn_info = f"Turn: {turn_number}, {current_player}'s turn"
    else:
        turn_info = f"Game Over: {game_status}. Click to Return"

    text_surface = font.render(turn_info, True, TEXT_COLOR)
    surface.blit(text_surface, (10, FEEDBACK_AREA_HEIGHT // 2 - text_surface.get_height() // 2))
    pygame.display.flip()

def handle_end_game(surface, game_status):
    font = pygame.font.Font(None, FONT_SIZE)
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                waiting_for_input = False
                # Reset or return to menu
                menu.mainloop(surface)


def update_display(board, sprite_group):
    sprite_group.empty()
    surface.fill(SURFACE_COLOR)

    # Draw board background
    board_background = Sprite(bg_file)
    board_background.rect.x, board_background.rect.y = grid_pos
    sprite_group.add(board_background)

    # Draw X or O sprites on the board
    for row in range(grid_size):
        for col in range(grid_size):
            letter = board.boardArray[row][col]
            if letter in ['X', 'O']: 
                sprite = Sprite(SPRITE_PATHS[letter])
                sprite.rect.x = grid_pos[0] + col * CELL_SIZE
                sprite.rect.y = grid_pos[1] + row * CELL_SIZE
                sprite_group.add(sprite)
    sprite_group.draw(surface)


# Menu Setup
menu = pygame_menu.Menu('Welcome', 800, 900, theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Game Board : ', [('3x3', '3x3'), ('4x4', '4x4')], onchange=set_game_mode)
menu.add.selector('Play as : ', [('X', 'X'), ('O', 'O')], onchange=set_player_letter)
menu.add.selector('Difficulty : ', [('Easy', 'easy'), ('Medium', 'med'), ('Hard', 'hard')], onchange=set_ai_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
