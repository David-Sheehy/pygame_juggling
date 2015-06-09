#! /usr/bin/env python3
import pygame
import models
import config
import sys

def spawn_ball():
    pass

def main():
    # init window
    pygame.init()
    w = pygame.display.set_mode(config.WINDOW_SIZE) 

    puck = models.Puck()
    ball = models.Ball()
    puck.set_position([config.WINDOW_SIZE[0]/2,config.WINDOW_SIZE[1]-25])
    ball.pos = [32,32]
    clock = pygame.time.Clock()


    # main game loop
    while True:
        clock.tick(60)

        # handle events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        # handle input
        # update game state
        puck.update(w)
        ball.update()
        
        # draw stuff
        puck.draw(w)
        ball.draw(w)


        # flip buffer
        pygame.display.flip()

if __name__ == '__main__':
    main()
