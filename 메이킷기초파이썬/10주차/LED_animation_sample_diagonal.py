from microbit import *

# 0 : LED off
# 1~9 : Control LED Brightness

diagonal = [
    '00000',
    'x0000',
    'xx000',
    'xxx00',
    'xxxx0',
    'xxxxx',
    '0xxxx',
    '00xxx',
    '000xx',
    '0000x'
]

# 8x8 초기화 (0으로 채워짐)
diagonal_stack = [
    '00000',
    '00000',
    '00000',
    '00000',
    '00000'
]


# bright 변경 함수
def change_bright(diagonal, brightness=1):
    return_diag = []
    for diag in diagonal:
        return_diag.append(diag.replace('x', str(brightness)))

    return return_diag


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
# change_bright()


# 메인 루프
diagonal = change_bright(diagonal, 9)
while True:
    # diagonal_stack = del_index(diagonal_stack, 0)
    del diagonal_stack[0]
    if idx == len(diagonal):
        idx = 0
    diagonal_stack.append(diagonal[idx])
    idx += 1
    img_str = ''
    for i, _str in enumerate(diagonal_stack):
        if i != len(diagonal_stack) - 1:
            _str += ':'
        img_str += _str
        print(_str)
    img = Image(img_str)
    # print(img_str)
    display.show(img)
    sleep(500)

