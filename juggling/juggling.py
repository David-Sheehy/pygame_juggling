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
    ball.pos = [300,32]
    clock = pygame.time.Clock()


    # main game loop
    MOVE_RIGHT = MOVE_LEFT = False
    MOVE_UP = MOVE_DOWN = False
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
                    # do nothing
                    pass
            elif e.type == pygame.KEYUP:
                if e.key == 275:
                    MOVE_RIGHT = False
                elif e.key == 276:
                    MOVE_LEFT = False
                else:
                    # do nothing
                    pass
            else:
                # do nothing
                pass

        # update game state
        # move the puck
        if MOVE_RIGHT and puck.pos[0] < config.WIDTH - puck.width:
            puck.move(w,config.PUCK_SPEED,0)
        if MOVE_LEFT and puck.pos[0] > 0:
            puck.move(w,-config.PUCK_SPEED,0)

        # check if the ball should bounce (ie collides with the walls, ceiling
        # or puck.)
        
        if (ball.pos[1] >= config.HEIGHT - puck.height) and (puck.pos[0] <= ball.pos[0] and ball.pos[0] <= puck.pos[0] + puck.width):
            # paddle
            ball.bounce((1,-1))
        elif ball.pos[0] <= 0: 
            # left wall
            ball.bounce((-1,1))
        elif ball.pos[0] >= config.WIDTH:
            ball.bounce((-1,1))

        elif ball.pos[1] <= 0:
            ball.bounce(-1,-1)

        elif ball.pos[1] >= config.HEIGHT:
            # ball lost
            ball.stop()

        ball.update(w)
        # draw stuff
        puck.draw(w)
        ball.draw(w)


        # flip buffer
        pygame.display.flip()

if __name__ == '__main__':
    main()
