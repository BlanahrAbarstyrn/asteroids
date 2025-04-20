# Throughout this project, some code was provided by Boot, like the inital code
# of the class below (comment added for where my code begins).
# The learning focus is on specific parts and Boot has pre-written the stuff that
# isn't related to the concepts Boot is trying to teach.

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    # ----------Code below this point is created by me-----------
    
    # detect if two objects are colliding with each other
    def is_colliding(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        if distance <= self.radius + other.radius:
            return True