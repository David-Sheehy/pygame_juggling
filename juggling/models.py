import pygame
"""
The class definitions for various things
"""
class Entity:
    def __init__(self, position=[0,0]):
        self.pos = position
        self.speed = [0,0]

    def draw(self, screen):
        """
        Draws the entity to the screen. This should really be overwritten by
        the sub classes.
        """
        pass

# end Entity definition 

class Puck(Entity):
    """
    """

    def __init__(self, position=[0,0]):
        self.width = 50
        self.height= 25
        # top left, top right, bot left, bot right
        self.color = (255, 255, 255)
        self.pos = position
        self.points = (
                    self.pos,
                    (self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.pos[1]),
                    
                )

    def hello(self):
        print("hello world from a puck")

    def set_position(self, position):
        self.pos = position
        self.points = (
                    self.pos,
                    (self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.height+self.pos[1]),
                    (self.width+self.pos[0],self.pos[1]),
                    
                )

    def draw(self, screen):
        """
        """
        pygame.draw.polygon(screen,self.color,self.points)
        pass

# end Puck definition

class Ball(Entity):
    """
    The ball controlling class.
    pos - The position of the ball.
    """
    def __init__(self,position=[0,0]):
        self.pos = position
        self.speed = [0,-1]
        self.size = 10
        self.color = (255,0,0)


    def draw(self, screen):
        """
        Draws the ball at it's current position on the screen
        """
        pygame.draw.circle(screen, self.color, self.pos, self.size)

    def hello(self):
        print("hello world from a ball")

# end Ball definition
