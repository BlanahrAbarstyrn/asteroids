# import everything from module
# circleshape.py into the current file
from circleshape import *
from constants import *

# A shot (bullet) class that inherits from CircleShape
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS

    # in the Shot class - overrides draw method of CircleShape
    def draw(self, screen):
        shot_color = (255,255,0) # yellow
        pygame.draw.circle(screen, shot_color, self.position, self.radius, width=5)
    
    
    # in shot class - overrides update method in CircleShape
    def update(self, dt):
        self.position += (self.velocity * dt)