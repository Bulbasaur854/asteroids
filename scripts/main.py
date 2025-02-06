import sys
import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *
from particle import *
from text import *

_lives = PLAYER_LIVES
_score = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 

    run_menu(screen, clock)   

def run_menu(screen, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game closed!")
                sys.exit(0) 

        screen.fill("black")

        draw_menu_text(screen)

        keys = pygame.key.get_pressed()    
        if keys[pygame.K_q]:
            print("Game closed!")
            sys.exit(0)        
        if keys[pygame.K_p]:
            play_game(screen, clock)

        pygame.display.flip()

def play_game(screen, clock):
    global _lives, _score

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Particle.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ui_score_board = Text(24, 24, screen, f"Score: {_score}")
    ui_player_lives = Text(24, 60, screen, f"Lives: {_lives}")

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game closed!")
                sys.exit(0)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]:
            print("Game closed!")
            sys.exit(0) 
        if pressed[pygame.K_m]:
            run_menu(screen, clock)

        screen.fill("black")

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                _lives -= 1
                ui_player_lives.update(f"Lives: {_lives}")
                player.kill()
                if _lives > 0:
                    play_game(screen, clock)
                else:
                    print("Game over!")
                    print(f"Final Score: {_score}")
                    _lives = 3
                    _score = 0
                    run_menu(screen, clock)

            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    _score += asteroid.score()
                    ui_score_board.update(f"Score: {_score}")
                    asteroid.split()

        for object in drawable:
            object.draw(screen)  
        ui_score_board.draw()
        ui_player_lives.draw()
        player.draw(screen) # in order to draw player over the projectile

        pygame.display.flip()

        dt = clock.tick(60) / 1000

def draw_menu_text(screen):
    Text(24, MENU_LINE_HEIGHT, screen, "> Welcome to Asteroids", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 2, screen, "> --------------------", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 3, screen, "> play", 18).draw()
    Text(224, MENU_LINE_HEIGHT * 3, screen, "[P]", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 4, screen, "> menu", 18).draw()
    Text(224, MENU_LINE_HEIGHT * 4, screen, "[M]", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 5, screen, "> quit", 18).draw()
    Text(224, MENU_LINE_HEIGHT * 5, screen, "[Q]", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 7, screen, "> Controls", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 8, screen, "> --------", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 9, screen, "> move", 18).draw()
    Text(224, MENU_LINE_HEIGHT * 9, screen, "[W] = fwd / [S] = bwd", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 10, screen, "> rotate", 18).draw()
    Text(224, MENU_LINE_HEIGHT * 10, screen, "[A] = lft / [D] = rgt", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 11, screen, "> shoot", 18).draw()
    Text(224, MENU_LINE_HEIGHT * 11, screen, "[Spc]", 18).draw()
    Text(24, MENU_LINE_HEIGHT * 13 , screen, "> Created by - Bul8a54ur", 18).draw()

if __name__ == "__main__":
    main()