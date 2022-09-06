from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from random import random
from math import atan2
import math
import model


class Hunter(Pulsator, Mobile_Simulton):
    visible = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, 2*math.pi*random(), 5)
        
    def update(self):
        self.move()
        self.wall_bounce()
        Pulsator.update(self)
        for prey in sorted(model.find(lambda x: isinstance(x, Prey)), key=lambda x : x.distance((self.get_location()[0],self.get_location()[1])), reverse=True):
            if self.distance((prey.get_location()[0],prey.get_location()[1])) < self.visible:
                self.set_angle(atan2(prey.get_location()[1]-self.get_location()[1], prey.get_location()[0]-self.get_location()[0]))
            if self.contains(prey.get_location()):
                model.remove(prey)
