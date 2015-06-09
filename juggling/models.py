import pygame
import config
import random
"""
The class definitions for various things
"""


class Entity:
    """
    The super class for most of the objects in this group.
    """



    def __init__(self, position=[0,0]):
        self.pos = position
        self.speed = [0,0]

    def set_position(self, position):
        self.pos = position
        self.bounds = position

    def draw(self, screen, color = None):
        """
        Draws the entity to the screen. This should really be overwritten by
        the sub classes.
        """
        pass


    def update(self):
        """
        This action should be called whenever the game state updates. In most
        cases it should move the game pieces.

        It needs to be overwritten by the derived class.
        """
        self.color = random.choice(config.COLORS)
        pass

# end Entity definition 

class Puck(Entity):
    """
    """

    def __init__(self, position=[0,0]):
        self.width = config.PUCK_WIDTH
        self.height= config.PUCK_HEIGHT
        # top left, top right, bot left, bot right
        self.color = config.WHITE
        self.pos = position
        self.bounds = (
                    self.pos,
                    (self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.pos[1]),
                    
                )

    def set_position(self, position):
        self.pos = position
        self.bounds = (
                    self.pos,
                    (self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.pos[1]),
                    
                )


    def move(self,screen, x, y):
        """
        Moves the puck by an amount of pixels either x or y. and erases the
        image at the previous location.
        """
        self.draw(screen,config.BLACK)
        self.set_position((self.pos[0] + x, self.pos[1] - y))

    def update(self, screen):
        pass

    def draw(self, screen,color=None):
        """
        """
        if not color:
            color = self.color

        pygame.draw.polygon(screen,color,self.bounds)

# end Puck definition

class Ball(Entity):
    """
    The ball controlling class.
    pos - The position of the ball.
    """
    def __init__(self,position=[0,0]):
        self.pos = position
        self.speed = [0,config.BALL_FALL_SPEED]
        self.size = 10
        self.color = config.RED

    def draw(self, screen, color = None):
        """
        Draws the ball at it's current position on the screen
        """
        if not color:
            color = self.color
        pygame.draw.circle(screen, color, self.pos, self.size)

    def move(self,screen, x, y):
        # cover up previous position
        self.draw(screen,config.BLACK)
        self.set_position((self.pos[0] + x, self.pos[1] - y))

    def update(self, screen):
        self.move(screen, self.speed[0], self.speed[1])

    def bounce(self, angle):
        """
        reverses the balls velocity. Should probaly vary based on which
        part of the puck actually hit it.
        """
        pass
# end Ball definition
