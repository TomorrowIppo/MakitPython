import random

가위바위보 = ['가위','바위','보']

while True:
    player = input("가위/바위/보/끝 : ")
    com = random.choice(가위바위보)

    if player == '끝':
        print("게임 종료!")
        break

    print("나 :", player)
    print("컴퓨터 :", com)

    if player == com:
        print("비겼어요!")
    elif player == '가위':
        if com == '바위':
            print("졌어요 ㅠㅠ")
        else:
            print("이겼어요 ^^")
    elif player == '바위':
        if com == '보':
            print("졌어요 ㅠㅠ")
        else:
            print("이겼어요 ^^")
    elif player == '보':
        if com == '가위':
            print("졌어요 ㅠㅠ")
        else:
            print("이겼어요 ^^")
    '''else:
        print("목록에서 입력해주세요")'''

            
