import turtle as t

t.shape('turtle')
t.bgcolor('black')
t.color('yellow')
t.speed(0)

#n = int(input('원의 갯수 : '))
n = 50
for i in range(n):
    t.circle(100)
    t.left(360 / n)

t.mainloop()