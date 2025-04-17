from circleshape import *
from constants import *

# A Player class that inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
    
    # in the player class -- this function provided by Boot
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Overrides draw method of CircleShape
    def draw(self, screen):
        player_color = (255, 255, 255)
        points_list = self.triangle()
        pygame.draw.polygon(screen, player_color, points_list, width=2)