# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (updatable, drawable, shots)
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2,y=SCREEN_HEIGHT / 2)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")    
            
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        
        
        poll_rate = clock.tick(60)
        dt = poll_rate/1000.0
    
if __name__ == "__main__":
    main()