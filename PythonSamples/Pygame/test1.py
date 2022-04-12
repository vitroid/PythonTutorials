import pygame

pygame.init()

black=[ 0, 0, 0]
white = [255,255,255]
blue = [ 0, 0,255]
green = [ 0,255, 0]
red = [255, 0, 0]

# Set the height and width of the screen
size=[400,400]
screen=pygame.display.set_mode(size)
#Loop until the user clicks the close button.
done=False
#Create a timer used to control how often the
clock = pygame.time.Clock()

while done==False:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
