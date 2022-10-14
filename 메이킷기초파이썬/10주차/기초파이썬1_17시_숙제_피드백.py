# 1번 문제
print()
print('# ---------------------- 1번 문제 ----------------------')
print()

for i in range(1, 31):
    if i % 3 == 0:
        print(i)


# 2번 문제
print()
print('# ---------------------- 2번 문제 ----------------------')
print()

for i in range(99, 0, -1):
    print(i)


# 3번 문제
print()
print('# ---------------------- 3번 문제 ----------------------')
print()

for i in range(1, 10):
    print('0.{}'.format(i))


# 4번 문제
print()
print('# ---------------------- 4번 문제 ----------------------')
print()

for i in range(1, 10):
    if i % 2 != 0:
        print('{}x{} = {}'.format(3, i, 3*i))


# 5번 문제
print()
print('# ---------------------- 5번 문제 ----------------------')
print()

n = int(input('입력: '))
sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum += i
        print(sum)


# 6번 문제
print()
print('# ---------------------- 6번 문제 ----------------------')
print()

n = input('(1부터 100사이)수를 입력하세요: ')

if int(n) < 1 or int(n) > 99:
    print('범위에 맞는 수를 입력하세요!')
else:
    count = 0
    for digit in n:
        if digit == '3':
            count += 1
        if digit == '6':
            count += 1
        if digit == '9':
            count += 1

    for i in range(count):
        print('짝')
