import turtle

color = ["red", "orange", "yellow", "green", "skyblue", "black", "pink"]
shape = ["turtle", "circle", "square", "triangle"]

t1 = turtle.Turtle(shape[1])
t2 = turtle.Turtle(shape[1])
t3 = turtle.Turtle(shape[1])
t4 = turtle.Turtle(shape[3])

t1.up()
t2.up()
t3.up()
t4.up()

t1.turtlesize(20)
t1.color(color[3])

t2.goto(-100,15)
t2.turtlesize(3)
t2.color(color[5])

t3.goto(100,15)
t3.turtlesize(3)
t3.color(color[5])

t4.goto(0,-85)
t4.turtlesize(2,8)
t4.color(color[2])

turtle.mainloop()