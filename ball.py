from prey import Prey
import math
from random import random


class Ball(Prey): 
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self, x, y, 10, 10, 2*math.pi*random(), 5)
        
    def update(self):
        super().move()
        super().wall_bounce()
        
    def display(self, canvas):
        canvas.create_oval(self._x-Ball.radius      , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill='blue')
