import pygame
import pygame_menu
#constant for the white background of the screen
SURFACE_COLOR = (255, 255, 255)
#not sure if these should be kept here or if we should have a seperate controller file
playerTurn = True
playerLetter = 'X'

#sprite class to streamline taking an image file and giving it a rect to define how much space it takes up
class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.height = self.image.get_height()
        self.width =self.image.get_width()
        self.rect = self.image.get_rect()

#initialize pygame object
pygame.init()
#set display to desired dimensions
surface = pygame.display.set_mode((600, 700))

#hold all current sprites in a group so that we can draw them all while running
SpritesList = pygame.sprite.Group()
#set up sprites
boardSprite =Sprite("assets/BoardSprite.png")
boardSprite.rect.x = 0
boardSprite.rect.y=100
SpritesList.add(boardSprite)

#might need clock to refresh the screen but not sure yet
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
    surface.fill(SURFACE_COLOR)
    SpritesList.draw(surface)
    pygame.display.flip()

pygame.quit()