# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the module
# constants.py into the current file
from constants import *

def main():
    # Initial environment testing
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Initialize Pygame
    pygame.init()

    # Set the screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Define the screen color
        color = (0, 0, 0)
        # Fill the screen with color
        screen.fill(color)
        # Update the display
        pygame.display.flip()



if __name__ == "__main__":
    main()