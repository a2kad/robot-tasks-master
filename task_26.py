#!/usr/bin/python3
"""
move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)
wall_is_above()	если сверху стена, возвращает True, иначе — False
wall_is_beneath()	если снизу стена, возвращает True, иначе — False
wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
wall_is_on_the_right()	если справа стена, возвращает True, иначе — False
fill_cell()	Закрасить текущую клетку
cell_is_filled()	Возвращает True, если текущая клетка закрашена
mov(r, v)	Поместить значение v в регистр r
"""
from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    for i in range(5):
        paint_the_cross_10()
        if i == 4:
            break
        else:
            move_down(n=4)


def paint_the_cross():
    move_right()
    for i in range(2):
        fill_cell()
        move_down()
    fill_cell()
    move_right()
    move_up()
    for n in range(2):
        fill_cell()
        move_left()
    fill_cell()
    move_up()

def paint_the_cross_10():
    for x in range(10):
        paint_the_cross()
        if x == 9:
            break
        else:
            move_right(n=4)
    move_left(n=36)

if __name__ == '__main__':
    run_tasks()
