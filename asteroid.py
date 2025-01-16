import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255,255,255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20° and 50°
        angle = random.uniform(20,50)

        # Rotate this asteroid's velocity vector by angle
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = velocity1
        a2.velocity = velocity2