# import everything from modules
# circleshape.py and constants.py into the current file
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
    
    # in the player class -- triangle function provided by Boot
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # in the player class - Overrides draw method of CircleShape
    def draw(self, screen):
        player_color = (255, 255, 255)
        points_list = self.triangle()
        pygame.draw.polygon(screen, player_color, points_list, width=2)

    # in the player class
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # in the player class - Overrides update method of CircleShape
    def update(self, dt):
        keys = pygame.key.get_pressed()
        negative_dt = dt * -1.0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt) # rotate left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(negative_dt) # rotate right
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt) # move forward
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(negative_dt) # move backward

    # in player class
    def move(self, dt):
        # these two lines of code provided by Boot
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt