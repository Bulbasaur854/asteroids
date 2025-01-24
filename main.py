import sys
import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    asteroid_field = AsteroidField()

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     

        screen.fill("black")

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit(0)

        for object in drawable:
            object.draw(screen)  


        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()