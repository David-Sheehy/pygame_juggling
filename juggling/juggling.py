#! /usr/bin/env python3
import pygame
import models
import config


balls = []
def spawn_ball():
    """
    Add a ball to the game.
    """
    balls.append(models.Ball())

def main():
    # init window
    pygame.init()

    w = pygame.display.set_mode(config.WINDOW_SIZE) 

    # set up various objects
    counter = models.Counter()
    puck = models.Puck()
    puck.set_position([config.WINDOW_SIZE[0]/2,config.WINDOW_SIZE[1]-25])
    clock = pygame.time.Clock()

    spawn_ball()

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
        for b in balls:    
            if (b.pos[1] >= config.HEIGHT - puck.height) and (puck.pos[0] <= b.pos[0] and b.pos[0] <= puck.pos[0] + puck.width):
                # paddle
                if b.pos[0] - puck.pos[0] < puck.width/2:
                    b.bounce((1, -1), english=(-2,0))
                else:
                    b.bounce((1, -1), english=(2,0))
                # counter stuff
                counter.erase(w)
                counter.increment()

            elif b.pos[0] - config.BALL_RADIUS <= 0: 
                # left wall
                b.bounce(angle=(-1,1))
            elif b.pos[0] + config.BALL_RADIUS >= config.WIDTH:
                # right wall
                b.bounce((-1,1))

            elif b.pos[1] - config.BALL_RADIUS <= 0:
                # top
                b.bounce((1,-1))

            elif b.pos[1] >= config.HEIGHT:
                # b lost
                b.stop()
                counter.erase(w)
                counter.reset()
                # move b to start
                b.erase(w)
                b.set_position(config.BALL_START)
                b.start()
            

            b.update(w)
        # draw stuff
        counter.display(w)
        puck.draw(w)
        for b in balls:
            b.draw(w)

        # flip buffer
        pygame.display.flip()

if __name__ == '__main__':
    main()
