# import everything from module
# circleshape.py into the current file
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

import random
import pygame

# An Asteroid class that inherits from CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # no additonal declarations needed here
    
    # in the Asteroid class - overrides draw method of CircleShape
    def draw(self, screen):
        asteroid_color = (255,165,0) # orange
        # with unneeded declarations removed from def __init__, self.position
        # now works in pygame.draw circle without needing to do headstands
        pygame.draw.circle(screen, asteroid_color, self.position, self.radius, width=2)
    
    
    # in Asteroid class - overrides update method in CircleShape
    def update(self, dt):
        self.position += (self.velocity * dt)

    
    # in Asteroid class - method to split asteroids into smaller
    # pieces when hit by bullets
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        generated_angle = random.uniform(20, 50)
        angle_1 = self.velocity.rotate(generated_angle)
        angle_2 = self.velocity.rotate(-generated_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_1.velocity = angle_1 * 1.2
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2.velocity = angle_2 * 1.2