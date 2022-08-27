import turtle as t

t.shape("turtle")

t.color("black", "red")
t.pensize(3)

t.circle(100, 90)
t.begin_fill()
t.circle(100, -90)
t.left(180)
t.circle(100, 90)

t.end_fill()

t.mainloop()