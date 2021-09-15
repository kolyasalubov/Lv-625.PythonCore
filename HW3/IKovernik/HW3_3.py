import pygame

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)
PI = 3.14

pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY))

pygame.display.set_caption("Draw primitives")

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    
    #функції lines і aalines малюють ламані
    # лінії, а параметр True означає замкнуті ламані,
    # False не замикати
    # 
    pygame.draw.lines(screen, YELLOW_COLOR, True, [[10, 10], [140, 70], [280, 20]], 12)
    pygame.draw.aalines(screen, YELLOW_COLOR, False, [[10, 100], [140, 170], [280, 110]])


    pygame.display.update()