from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            deviation = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            unit_vector = self.velocity

            for i in range(0, 2):
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                rotated_vector = unit_vector.rotate(deviation)
                rotated_with_speed_vector = rotated_vector * 1.2
                asteroid.velocity = rotated_with_speed_vector
                deviation *= -1

