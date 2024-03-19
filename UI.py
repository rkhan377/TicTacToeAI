import pygame
import pygame_menu
SURFACE_COLOR = (255, 255, 255)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        super().__init__()
        self.image = pygame.image.load(imagePath)#.convert()
        self.height = self.image.get_height()
        self.width =self.image.get_width()
        self.rect = self.image.get_rect()

pygame.init()
surface = pygame.display.set_mode((600, 700))

all_sprites_list = pygame.sprite.Group()
#set up sprites
boardSprite =Sprite("assets/BoardSprite.png")
boardSprite.rect.x = 0
boardSprite.rect.y=100
all_sprites_list.add(boardSprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    surface.fill(SURFACE_COLOR)
    all_sprites_list.draw(surface)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()