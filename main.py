# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from the module
# constants.py into the current file
from constants import *

from player import *

def main():
    # Initial environment testing
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Initialize Pygame
    pygame.init()

    # Set the screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initializing for frames per second
    fps = pygame.time.Clock()
    dt = 0

    # Instantiating Player object
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)


    # -------GAME LOOP-------

    while True:
        # Turn on ability to close game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Define the screen color
        color = (0, 0, 0)
        # Fill the screen with color
        screen.fill(color)
        # Render player on screen each frame
        player.draw(screen)
        # Update the display
        pygame.display.flip()
        # Setting Frames Per Second
        fps.tick(60)
        # Run time from start of game
        dt = (pygame.time.get_ticks()) / 1000
        # Test that dt returned a value
        #print(dt)

    # -------END GAME LOOP-------

if __name__ == "__main__":
    main()