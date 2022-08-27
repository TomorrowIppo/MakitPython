import turtle as t

t.shape("turtle")

t.setpos(0, 0)

t.color("black", "red")
t.pensize(3)

t.circle(100, 90)
#t.begin_fill()
t.circle(100, -90)
t.left(180)
t.circle(100, 90)

t.goto(100, 100)

#t.end_fill()

t.mainloop()