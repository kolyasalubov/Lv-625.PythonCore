import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Fly')


 
clock = pygame.time.Clock()

#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load(r"C:\Users\zet\Desktop\python course\1.png").convert()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    #Fill the creen with black color
    screen.fill(BLACK)
 
    # Copy image to screen:
#копіює картинку на екран
    screen.blit(player_image, [x, y])
 
#обновляємо екран
    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()