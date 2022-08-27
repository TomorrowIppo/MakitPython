import turtle as t
t.shape("turtle")
t.color("green")

shape = input("도형을 입력하세요(tri/rec):")

if shape == "tri":
    for i in range(3):
        t.forward(100)
        t.right(120)
elif shape == "rec":
    for i in range(4):
        t.forward(100)
        t.right(90)
else:
    t.write("다시 입력하세요!")

