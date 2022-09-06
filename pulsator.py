from blackhole import Black_Hole
import model


class Pulsator(Black_Hole): 
    counter = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self, x, y)
        
    def update(self):
        self.counter -= 1
        for _ in super().update():
            super().change_dimension(1, 1)
            self.radius += .5
            self.counter = 30
            
        if self.counter == 0:
            super().change_dimension(-1, -1)
            self.radius -= .5
            self.counter = 30
            
        if self.get_dimension()[0] == 0:
            model.remove(self)
