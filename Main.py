import pygame
from sys import exit

pygame.init()

#It creates a screen surface.
screen = pygame.display.set_mode((800, 400))

#It changes the title to the title wanted.
pygame.display.set_caption("My First Game")
#Controlling FPS.
clock = pygame.time.Clock()

while True:
    # Checking for any input.
    for event in pygame.event.get():
        # Checking for the input quit.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Update the display of pygame.
    pygame.display.update()
    # Gives a maximum frame rate.
    clock.tick(60)
