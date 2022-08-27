'''
#1
name = input("가장 친한 친구 이름은?")
nickname = input("그 친구의 별명은?")
print(name+"은 "+nickname+"이다!")

#2
num1 = int(input("첫 번째 숫자를 입력하세요."))
num2 = int(input("두 번째 숫자를 입력하세요."))

if num1 > num2 :
    print("첫 번째 숫자가 더 큽니다.")
elif num1 < num2 :
    print("두 번째 숫자가 더 큽니다.")
else:
    print("두 수의 크기가 같다.")

#3
num = int(input("숫자를 입력하세요."))

for i in range(1,num+1):
    print( i )


#4
import random

floor = int(input("몇 층에 가세요?"))

p = random.randint(1,12)
print(p ,"명 탑승했습니다.")

if p>=8:
    print("정원 초과입니다.")
else:
    for i in range(1,floor):
        print(i ,"층 입니다.")
    print(floor ,"층에 도착했습니다.")
'''






    
