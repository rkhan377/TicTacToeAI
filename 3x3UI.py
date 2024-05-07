import pygame
import pygame_menu
from Opponent import Opponent
from Board import Board

SURFACE_COLOR = (255, 255, 255)
GRID_POS = (0, 0)
CELL_SIZE = 200
WINDOW_SIZE = (600, 700)
pygame.display.set_mode(WINDOW_SIZE)
FEEDBACK_AREA_HEIGHT = 100
FEEDBACK_AREA_COLOR = (230, 230, 230)
TEXT_COLOR = (0, 0, 0)
FONT_SIZE = 24
SPRITE_PATHS = {
    'X': 'assets/XSprite.png',
    'O': 'assets/OSprite.png',
}

pygame.init()
surface = pygame.display.set_mode(WINDOW_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()

player_letter = 'X'
ai_difficulty = 'easy'
ai_opponent = None

def set_player_letter(value, letter):
    global player_letter
    player_letter = letter 

def set_ai_difficulty(value, difficulty):
    global ai_difficulty
    ai_difficulty = difficulty

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
    
    update_display(board, sprite_group)
    draw_feedback(surface, turn_number, player_turn, "In Progress") 
    pygame.display.flip()

    if not player_turn:
        row, col = ai_opponent.playTurn(board)
        board.setLetter(ai_opponent.letter, row, col)
        player_turn = True 
        turn_number = 2  
        update_display(board, sprite_group)  
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
                if y > FEEDBACK_AREA_HEIGHT: 
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
            draw_feedback(surface, turn_number, player_turn, game_status) 
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
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            elif event.type == pygame.MOUSEBUTTONUP:
                waiting_for_input = False
                menu.mainloop(surface)


def update_display(board, sprite_group):
    sprite_group.empty()
    surface.fill(SURFACE_COLOR)

    board_background = Sprite("assets/BoardSprite.png")
    board_background.rect.x = GRID_POS[0]
    board_background.rect.y = GRID_POS[1] + FEEDBACK_AREA_HEIGHT
    sprite_group.add(board_background)

    for row in range(board.size):
        for col in range(board.size):
            letter = board.boardArray[row][col]
            if letter in ['X', 'O']:
                sprite = Sprite(SPRITE_PATHS[letter])
                sprite.rect.x = GRID_POS[0] + col * CELL_SIZE
                sprite.rect.y = GRID_POS[1] + row * CELL_SIZE + FEEDBACK_AREA_HEIGHT
                sprite_group.add(sprite)
    sprite_group.draw(surface)

menu = pygame_menu.Menu('Welcome', 600, 700, theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Play as : ', [('X', 'X'), ('O', 'O')], onchange=set_player_letter)
menu.add.selector('Difficulty : ', [('Easy', 'easy'), ('Medium', 'med'), ('Hard', 'hard')], onchange=set_ai_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
