import turtle as t

# 첫번째 사각형
t.color("yellow", "yellow")
t.pensize(3)
t.begin_fill()

side = 100

t.forward(side)
t.right(90)
t.forward(side)
t.right(90)
t.forward(side)
t.right(90)
t.forward(side)
t.right(90)
t.end_fill()

# 두번째 사각형
t.color("blue", "blue")
t.pensize(3)
t.begin_fill()

t.forward(side/2)
t.right(90)
t.forward(side/2)
t.right(90)
t.forward(side/2)
t.right(90)
t.forward(side/2)
t.right(90)
t.end_fill()

# 세번째 사각형
t.color("red", "red")
t.pensize(3)
t.begin_fill()

t.forward(side/4)
t.right(90)
t.forward(side/4)
t.right(90)
t.forward(side/4)
t.right(90)
t.forward(side/4)
t.right(90)
t.end_fill()

t.mainloop()

