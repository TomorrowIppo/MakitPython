from microbit import *
import random

while True:
    if button_a.is_pressed():
        n = str(random.randint(1, 6))
        display.show()
        sleep(3000)
    else:
        display.clear()