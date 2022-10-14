from microbit import *

# 0 : LED off
# 1~9 : Control LED Brightness

matrix_arrow = [
    '00000',
    '00x00',
    '0xxx0',
    'xxxxx',
    '00000',
    '00x00',
    '0xxx0',
    'xxxxx'
]

# 8x8 초기화 (0으로 채워짐)
matrix_stack = [
    '00000',
    '00000',
    '00000',
    '00000',
    '00000'
]


# matrix 초기화
def reset_matrix():
    return_mt = []
    for i in range(5):
        return_mt.append('00000')

    return return_mt


# bright 변경 함수
def change_bright(matrix, brightness=1):
    return_mt = []
    for mt in matrix:
        return_mt.append(mt.replace('x', str(brightness)))

    return return_mt


# del 기능이 안먹힐 걸 대비해서
def del_index(_list, _idx):
    result_list = []
    for i in range(len(_list)):
        if i == _idx:
            continue
        result_list.append(_list[i])

    return result_list


# 초기화 단계
idx = 0
interval = 70
# change_bright()


# 메인 루프
matrix = change_bright(matrix_arrow, 9)
while True:
    # diagonal_stack = del_index(diagonal_stack, 0)
    if button_a.is_pressed():
        del matrix_stack[0]
        if idx == len(matrix):
            idx = 0
        matrix_stack.append(matrix[idx])
        idx += 1
        img_str = ''
        for i, _str in enumerate(matrix_stack):
            if i != len(matrix_stack) - 1:
                _str += ':'
            img_str += _str
            print(_str)
        img = Image(img_str)
        # print(img_str)
        display.show(img)
        sleep(interval)
    elif button_b.is_pressed():
        del matrix_stack[len(matrix_stack) - 1]
        if idx == len(matrix):
            idx = 0
        matrix_stack.insert(0, matrix[idx])
        idx += 1
        img_str = ''
        for i, _str in enumerate(matrix_stack):
            if i != len(matrix_stack) - 1:
                _str += ':'
            img_str += _str
            print(_str)
        img = Image(img_str)
        # print(img_str)
        display.show(img)
        sleep(interval)
    else:
        idx = 0
        img_str = ''
        matrix_stack = reset_matrix()
        for i, _str in enumerate(matrix_stack):
            if i != len(matrix_stack) - 1:
                _str += ':'
            img_str += _str
            print(_str)
        display.show(Image(img_str))
        sleep(interval)
