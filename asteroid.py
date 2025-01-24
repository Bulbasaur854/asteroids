import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", center, self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        
        # small asteroid, we are done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # spawn 2 new, smaller asteroids
        new_direction_angle = random.uniform(20, 50) 
        direction1 = self.velocity.rotate(new_direction_angle)
        direction2 = self.velocity.rotate(-new_direction_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = direction1 * 1.2
        asteroid2.velocity = direction2 * 1.2