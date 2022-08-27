import turtle as t
import time

t.shape("turtle")
t.color("green")
t.turtlesize(10)
angle = 0

while angle<=360:
    t.setheading(angle)
    time.sleep(0.0001)
    angle=angle+1

    
