import sys

import pygame

from asteroid import Asteroid
from player import Player
from constants import *
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over!", True, (255,255,255))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField.containers = (updatable,)
    AsteroidField()

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color)
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                screen.blit(game_over_text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                pygame.display.flip()
                pygame.time.wait(2000)
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()