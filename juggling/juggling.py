#! /usr/bin/env python3
import pygame
import models
import config

def spawn_ball():
    pass

def main():
    # init window
    pygame.init()
    w = pygame.display.set_mode(config.WINDOW_SIZE) 

    puck = models.Puck()

    puck.set_position([config.WINDOW_SIZE[0]/2,config.WINDOW_SIZE[1]-25])


    # main game loop
    while True:
        # handle events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        # handle input
        # update game state

        # flip buffer
        puck.draw(w)
        pygame.display.flip()

if __name__ == '__main__':
    main()
