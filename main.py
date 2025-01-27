import sys
import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *
from score import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score_board = Score(screen)    

    dt = 0

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game closed!")
                sys.exit(0)

        screen.fill("black")

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                player.dies()
                if player.lives > 0:
                    main()
                else:
                    print("Game over!")
                    print(f"Final Score: {score_board.get_score()}")
                    sys.exit(0)

            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    score_board.update_score(asteroid.score())
                    asteroid.split()

        for object in drawable:
            object.draw(screen)  

        score_board.draw_score()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()