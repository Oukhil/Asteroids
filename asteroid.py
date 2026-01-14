import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        split_angle = random.uniform(20, 50)
        split_vector_first = self.velocity.rotate(split_angle)
        split_vector_second = self.velocity.rotate(-split_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_first = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_second = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_first.velocity = split_vector_first * 1.2
        split_asteroid_second.velocity = split_vector_second * 1.2





