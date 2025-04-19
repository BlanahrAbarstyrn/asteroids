# import everything from module
# circleshape.py into the current file
from circleshape import *

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