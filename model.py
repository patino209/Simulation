import controller
import model   

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from special    import Special

import math,random

running     = False
cycle_count = 0
balls       = set()

def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count
    global running
    if running:
        cycle_count += 1
        for b in balls:
            b.update()
        running = False
    else:
        cycle_count += 1
        for b in balls:
            b.update()


def select_object(kind):
    global object_kind
    object_kind = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if object_kind == 'Remove':
        for b in balls.copy():
            if b.contains((x,y)):
                balls.remove(b)
    else:
        balls.add(eval(object_kind)(x,y))


#add simulton s to the simulation
def add(s):
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    s = set()
    for b in balls:
        if p(b):
            s.add(b)
    return s
            

def reverse():
    for b in balls:
        b.reverse() 

def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in balls.copy():
            b.update()

def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
