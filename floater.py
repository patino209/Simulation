from prey import Prey
from random import random
import math


class Floater(Prey): 
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self, x, y, 10, 10, 2*math.pi*random(), 5)
        
    def update(self):
        super().move()
        super().wall_bounce()
        
        if random() < .30:
            super().set_angle(super().get_angle() + (random() - .5))
            super().set_speed(super().get_speed() + (random() - .5))
            if super().get_speed() > 7:
                super().set_speed(super().get_speed() - .5)
            if super().get_speed() < 5:
                super().set_speed(super().get_speed() + .5)
        
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='red')
