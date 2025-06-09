# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2,y=SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        
        poll_rate = clock.tick(60)
        dt = poll_rate/1000.0
    
if __name__ == "__main__":
    main()