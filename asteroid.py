from constants import *
from circleshape import *
from logger import log_event
import random

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        direction = random.uniform(20, 50)
        new_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid.velocity = self.velocity.rotate(direction) * 1.2
        second_new_asteroid.velocity = self.velocity.rotate(-(direction)) * 1.2