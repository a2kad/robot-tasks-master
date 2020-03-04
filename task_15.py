#!/usr/bin/python3
'''
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
'''
from pyrob.api import *


@task
def task_8_21():
    for i in range(1):
        if wall_is_on_the_right() and wall_is_beneath():
            move_up(n=9)
            move_left(n=9)
            break
        if  wall_is_on_the_right() and wall_is_above():
            move_left(n=9)
            move_down(n=9)
            break
        if wall_is_on_the_left() and wall_is_beneath():
            move_up(n=9)
            move_right(n=9)
            break
        if  wall_is_on_the_left() and wall_is_above():
            move_right(n=9)
            move_down(n=9)
            break
            

if __name__ == '__main__':
    run_tasks()
