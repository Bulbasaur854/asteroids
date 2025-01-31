import pygame
import random
import pygame.gfxdraw

from circleshape import *
from constants import *

class Particle(CircleShape):
    def __init__(self, x, y):
        self.radius = random.uniform(PARTICLE_SIZE_MIN, PARTICLE_SIZE_MAX)
        super().__init__(x, y, self.radius)
        rotation = random.uniform(0, 360)
        speed = random.randint(PARTICLE_SPEED_MIN, PARTICLE_SPEED_MAX)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * speed

    def draw(self, screen):
        center = (self.position.x, self.position.y)
        color = pygame.Color(120, 120, 120)
        pygame.gfxdraw.filled_circle(screen, int(center[0]), int(center[1]), int(self.radius), color)
        
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        if (self.offscreen()):
            self.kill()
    
    def offscreen(self):
        return (self.position.x < 0 or   
                self.position.x > SCREEN_WIDTH or   
                self.position.y < 0 or   
                self.position.y > SCREEN_HEIGHT)