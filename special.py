from prey import Prey
import math
from random import random
import model
from hunter import Hunter
from math import atan2

#
#
# This special class inherits from the Prey class
# Its special ability is that it will get a speed boost for 30 cycles while getting chased by a hunter
# After its speed boost, it will be exhausted for 90 cycles and will be at normal speed until it is no longer exhausted
#
#


class Special(Prey):
    radius = 5
    cycles = 30
    exhaustion = 0
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 2*math.pi*random(), 5)
        
    def update(self):
        super().move()
        super().wall_bounce()
        for hunter in sorted(model.find(lambda x: isinstance(x, Hunter)), key=lambda x : x.distance((self.get_location()[0],self.get_location()[1])), reverse=True):
            if self.distance((hunter.get_location()[0],hunter.get_location()[1])) < 200:
                self.set_angle(atan2(self.get_location()[1]-hunter.get_location()[1], self.get_location()[0]-hunter.get_location()[0]))
                
                if self.exhaustion == 0:
                    self.set_speed(10)
                    self.cycles -= 1
                    if self.cycles == 0:
                        self.exhaustion = 90
                        self.set_speed(5)
                        self.cycles = 30
                else:
                    self.exhaustion -= 1
        
    def display(self, canvas):
        canvas.create_oval(self._x-Special.radius      , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill='purple')