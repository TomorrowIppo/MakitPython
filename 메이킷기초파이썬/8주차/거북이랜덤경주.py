import turtle as t
import random

t.up()
t.goto(-140,140)
t.speed(0)
t.hideturtle()

#경기장 만들기
for step in range(15):
    t.write(step, align = "center")
    t.right(90)
    t.forward(10)
    t.down()
    t.forward(150)
    t.up()
    t.backward(160)
    t.left(90)
    t.forward(20)

#거북이 선수 만들기
t_list = []
t_name = []
t_num = int(input("거북이 몇 마리?(최대5) :"))
for x in range(t_num):  #거북이 생성
    t_list.append(t.Turtle())
    
#거북이 속성 설정
for x in range(t_num):  
    t_name.append(input(str(x+1)+"번 거북이 이름은? :"))
    color = input(str(x+1)+"번 거북이 색깔은? :")
    t_list[x].color(color)
    t_list[x].shape("turtle")
    t_list[x].up()
    t_list[x].goto(-160, 100-(x*20))
    t_list[x].write(t_name[x], align = "center")
    t_list[x].down()



#경주 시작
input("경주를 시작하려면 엔터를 누르세요!")

for turn in range(100):
    for x in range(t_num):
        t_list[x].forward(random.randint(1,5))

    
#1등 거북이 구하기
dist = []
for x in range(t_num):
    dist.append(t_list[x].xcor())
first = max(dist)
result = dist.index(first)
print(t_name[result],"승리!!")




