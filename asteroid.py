# import everything from module
# circleshape.py into the current file
from circleshape import *

# An Asteroid class that inherits from CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        #super().__init__(x, y, radius)
    
    
    # in the Asteroid class - overrides draw method of CircleShape
    def draw(self, screen):
        asteroid_color = (255,255,255)
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, asteroid_color, center, self.radius, width=2)
    
    
    # in Asteroid class - overrides update method in CircleShape
    def update(self, dt):
        self.position += (self.velocity * dt)