#! /usr/bin/env python3
import pygame
import models
import config

balls_in_play = []   # The balls currently in the game
balls_out_play = []  # The balls which, exist, but aren't used

def spawn_ball():
    """
    Add a ball to the game.
    in_play - The amount of balls currently in play.
    """
    balls_in_play.append(models.Ball())

def main():
    # init window
    pygame.init()

    pygame.display.set_caption("juggling")
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
        for i,b in enumerate(balls_in_play):
            if (b.pos[1] >= config.HEIGHT - puck.height)\
                and (puck.pos[0] <= b.pos[0] \
                and b.pos[0] <= puck.pos[0] + puck.width):
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
            elif b.pos[0] + config.BALL_RADIUS >= config.WIDTH - 2:
                # right wall
                b.bounce((-1,1))

            elif b.pos[1] - config.BALL_RADIUS <= 2:
                # top
                b.bounce((1,-1))

            elif b.pos[1] >= config.HEIGHT - 2:
                # b has been lost
                # stop the motion
                b.stop()

                # clear the counter
                counter.erase(w)
                counter.reset()

                if len(balls_in_play) > 1:
                    # remove ball from play
                    b.erase(w)
                    # keep it slightly off screen
                    b.set_position(
                                   ( -config.BALL_RADIUS * (i + 1),
                                    -config.BALL_RADIUS)
                                  )
                    balls_in_play.remove(b)
                    balls_out_play.append(b)
                else:
                    # move the only ball back into play.
                    b.erase(w)
                    b.set_position(config.BALL_START)
                    b.start()

                # remove that ball from play
            
            # see if it's colliding with any other balls
            for ob in balls_in_play:
                if b != ob and\
                    ((abs(b.pos[0] - ob.pos[0]) <= config.BALL_RADIUS)\
                    and (abs(b.pos[1] - ob.pos[1]) <= config.BALL_RADIUS)):

                    b.bounce((-1,1),(1,0))
                    ob.bounce((-1,1),(0,1))

            b.update(w)

        # check if we should add balls, or put one back into play.
        if( counter.count >= (2<<(len(balls_in_play)))):
            if len(balls_out_play) <= 0:
                spawn_ball()
            else:
                # move a ball back into play
                b = balls_out_play.pop()
                balls_in_play.append(b)
                b.set_position(config.BALL_START)
                b.start()
                pass

        # draw stuff
        counter.display(w)

        puck.draw(w)
        for b in balls_in_play:
            b.draw(w)

        # flip buffer
        pygame.display.flip()

if __name__ == '__main__':
    main()
