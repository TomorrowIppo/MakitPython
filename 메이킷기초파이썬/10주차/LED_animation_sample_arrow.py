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

matrix_none = [
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
idx = 0  # idx를 통해 matrix_arrow를 순회
interval = 70
# change_bright()


# 메인 루프
matrix = change_bright(matrix_arrow, 9)
while True:
    # diagonal_stack = del_index(diagonal_stack, 0)

    # a 버튼을 눌렀을 때
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
            # print(_str)
        img = Image(img_str)
        # print(img_str)
        display.show(img)
        sleep(interval)

    # b 버튼을 눌렀을 때
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
            # print(_str)
        img = Image(img_str)
        # print(img_str)
        display.show(img)
        sleep(interval)

    # 아무것도 누르지 않았을 때
    else:
        idx = 0
        # 26번째 줄에 만들어놓은 matrix_none을 사용해서
        # matrix_stack = matrix_none으로 스택을 초기화 하면 안되는 이유
        # 위의 코드가 의미하는 것은 matrix_stack이 의미하는 주소를
        # matrix_none이 의미하는 주소로 바꾼다는 것이다.
        # 이 상태에서 list를 del 하고 append 해봤자 matrix_none이 의미하는
        # 리스트의 상태가 변하는 것이기에 처음엔 [00000 ... ]이었지만
        # [aaaaa, bbbbb, ... ] 등으로 변형되어 나중에
        # matrix_stack = matrix_none이 호출 되어도 초기화의 기능을 수행하지 못 한다.

        # 그렇기 때문에 따로 함수를 만들거나 하여 새로운 초기화 리스트를 만들어
        # 대입해줘야 한다.
        matrix_stack = reset_matrix()
        display.clear()
