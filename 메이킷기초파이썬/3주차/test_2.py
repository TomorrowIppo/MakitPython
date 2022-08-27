import turtle as t

t.shape("turtle")

t.color("yellow", "yellowgreen")
t.pensize(3)

t.begin_fill()

t.left(270)
t.circle(50, -180)
t.right(150)
t.forward(100)
t.left(120)
t.forward(100)

t.end_fill()

t.mainloop()