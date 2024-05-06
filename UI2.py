import pygame
import pygame_menu

# Constants
SURFACE_COLOR = (255, 255, 255)
GRID_POS = (0, 0)  # Adjust as needed to align with your board sprite
CELL_SIZE = 200  # Assuming each cell in your grid is 200x200 pixels

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode((600, 600))

# Sprite Handling
class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()

# Sprites
SpritesList = pygame.sprite.Group()
boardSprite = Sprite("assets/BoardSprite.png")
boardSprite.rect.x, boardSprite.rect.y = GRID_POS
SpritesList.add(boardSprite)

# Board State
board = [[None, None, None], [None, None, None], [None, None, None]]
playerTurn = True  # True if player X's turn, False for player O
playerLetter = 'X'

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            # Convert mouse position to board grid coordinates
            col = (x - GRID_POS[0]) // CELL_SIZE
            row = (y - GRID_POS[1]) // CELL_SIZE
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] is None:
                # Place player's letter in the board array
                board[row][col] = playerLetter
                # Toggle player turn
                playerTurn = not playerTurn
                playerLetter = 'O' if playerLetter == 'X' else 'X'

    # Drawing
    surface.fill(SURFACE_COLOR)
    SpritesList.draw(surface)
    # Draw Xs and Os
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
