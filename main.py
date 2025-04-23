# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import random


# import everything from modules circleshape,
# constants.py, player.py, asteroid.py, shot.py
# and asteroidfield.py into the current file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    # Initial environment testing
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Initialize Pygame
    pygame.init()

    # Set the screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set Window Title
    pygame.display.set_caption('Asteroids')

    # importing star image
    star_surf = pygame.image.load('/home/sittingturtle/workspace/github.com/BlanahrAbarstyrn/asteroids/images/star.png').convert_alpha()
    star_positions = [(random.randint(0,SCREEN_WIDTH),random.randint(0,SCREEN_HEIGHT)) for i in range(40)]

    # Initializing for frames per second
    fps = pygame.time.Clock()
    dt = 0

    # Declaring groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Instantiating Player object
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Instantiating AsteroidField object
    asteroid_field = AsteroidField()

    # Instantiating Shot object


    # Initiating Game Loop Status
    run = True

    # -------GAME LOOP-------

    while run:

        try:
            # Turn on ability to close game window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # Define the screen color
            color = (0, 0, 0)
            # Fill the screen with color
            screen.fill(color)
            # Render each member in group drawable on screen each frame
            for member in drawable:
                member.draw(screen)
            # Update rotation for members of updatable group
            updatable.update(dt)
            # background stars
            for pos in star_positions:
                screen.blit(star_surf, pos)
            # Update the display
            pygame.display.flip()
            # Setting Frames Per Second
            fps.tick(60)
            # elapsed time between frames
            dt = (fps.get_time()) / 1000
            # cooldown timer between shots
            for member in updatable:
                if member == player:
                    Player.shot_timer -= dt
            # Test that dt returned a value
            #print(dt)
            # listen for collisions
            for asteroid in asteroids:
                if asteroid.is_colliding(player) == True:
                    raise Exception("Game Over")
                for shot in shots:
                    if shot.is_colliding(asteroid) == True:
                        asteroid.split()
                        shot.kill()
        except Exception as e:
            print(e)
            run = False
            


    # -------END GAME LOOP-------

if __name__ == "__main__":
    main()