import pygame
import random
from circleshape import *

class Particle(CircleShape):
    def __init__(self, x, y):
        self.radius = random.uniform(2, 8)
        super().__init__(x, y, self.radius)
        rotation = random.uniform(0, 360)
        speed = random.randint(400, 600)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * speed

    def draw(self, screen):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", center, self.radius, 2)
        
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt