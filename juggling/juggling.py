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
    MOVE_RIGHT = MOVE_LEFT = False
    while True:
        clock.tick(60)

        # handle events
        # handle input
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            elif e.type == pygame.KEYDOWN:
                if e.key == 275:
                    MOVE_RIGHT = True
                    # move right
                elif e.key == 276:
                    MOVE_LEFT = True
                    # move left
                else:
                    pass
            elif e.type == pygame.KEYUP:
                MOVE_RIGHT = MOVE_LEFT = False
            else:
                # do nothing
                pass

        # update game state
        # move the puck
        if MOVE_RIGHT:
            puck.move(w,1,0)
        elif MOVE_LEFT:
            puck.move(w,-1,0)
        else:
            pass


        # move the ball
        ball.update()
        
        # draw stuff
        puck.draw(w)
        ball.draw(w)


        # flip buffer
        pygame.display.flip()

if __name__ == '__main__':
    main()
