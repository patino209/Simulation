from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, 20, 20)
        
    def update(self):
        eaten = set()
        for prey in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(prey.get_location()):
                eaten.add(prey)
                model.remove(prey)
        return eaten
        
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='black')
        
    def contains(self, xy):
        if self.distance((xy[0],xy[1])) < self.radius:
            return True
        return False