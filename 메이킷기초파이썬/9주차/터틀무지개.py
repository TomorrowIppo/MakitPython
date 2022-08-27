import turtle as t

t.bgcolor('lightblue')
t.speed(100000)
t.pensize(30)

clr=['red','orange','yellow','green','blue','navyBlue','purple']

def rainbow(x,color,R):
    t.up()
    t.setheading(90)
    t.goto(x,0)
    t.down()
    t.color(color)
    t.circle(R,180)
    
while True:
    rainbow(200,clr[0],200)
    rainbow(175,clr[1],175)
    rainbow(150,clr[2],150)
    rainbow(125,clr[3],125)
    rainbow(100,clr[4],100)
    rainbow(75,clr[5],75)
    rainbow(50,clr[6],50)
    t.clear()   #다 지워주는것 

def concat(str1, str2):
    return str1+str2

print(concat('빨주노초','파남보'))
 





