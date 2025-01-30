import pygame
import random
from circleshape import *
from constants import *
from particle import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        center = (self.position.x, self.position.y)
        pygame.draw.circle(screen, "white", center, self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        self.wrap_around()

    def wrap_around(self):
        border_x_min = 0 - ASTEROID_MAX_RADIUS - ASTEROID_WRAP_OFFSET
        border_x_max = SCREEN_WIDTH + ASTEROID_MAX_RADIUS + ASTEROID_WRAP_OFFSET
        border_y_min = 0 - ASTEROID_MAX_RADIUS - ASTEROID_WRAP_OFFSET
        border_y_max = SCREEN_HEIGHT + ASTEROID_MAX_RADIUS + ASTEROID_WRAP_OFFSET

        if self.position.x < border_x_min:
            self.position.x = border_x_max
        elif self.position.x > border_x_max:
            self.position.x = border_x_min
        
        if self.position.y < border_y_min:
            self.position.y = border_y_max
        elif self.position.y > border_y_max:
            self.position.y = border_y_min

    def split(self):
        self.spawn_particles(ASTEROID_PARTICLES_NUM)
        self.kill()
        
        # small asteroid, we are done
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.spawn_particles(ASTEROID_PARTICLES_NUM * 3)
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

    def spawn_particles(self, num):
        for _ in range(0, num):
            Particle(self.position.x, self.position.y)

    def score(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return SCORE_SMALL
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            return  SCORE_MEDIUM
        elif self.radius <= ASTEROID_MIN_RADIUS * 3:
            return  SCORE_LARGE
        