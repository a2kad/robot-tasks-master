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


@task
def task_2_2():
    move_right()
    for z in range(4):
        paint_the_cross()
        move_right(n=5)
        move_up()
    paint_the_cross()

def paint_the_cross():
    for i in range(3):
        move_down()
        fill_cell()
    move_right()
    move_up()
    for n in range(2):
        fill_cell()
        move_left()
    fill_cell()    
    move_up()

if __name__ == '__main__':
    run_tasks()
