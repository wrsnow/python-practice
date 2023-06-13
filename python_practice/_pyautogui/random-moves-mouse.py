import pyautogui as pag
from random import randrange
from time import sleep

size = pag.getInfo()[4]
max_width = size.width
max_height = size.height


def random_x(): return randrange(0, max_width)
def random_y(): return randrange(0, max_height)


for i in range(4):
    sleep(1)
    pag.moveTo(random_x(), random_y(), 0.15)
