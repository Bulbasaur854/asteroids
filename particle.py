import pygame
import random
from circleshape import *

class Particle(CircleShape):
    def __init__(self, x, y):
        self.radius = random.uniform(0.1, 0.5)
        super().__init__(x, y, self.radius)
        self.direction = self.velocity.rotate(random.uniform(0, 360))
        self.velocity = self.direction * 2

    def draw(self, screen):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", center, self.radius, 2)
        
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt