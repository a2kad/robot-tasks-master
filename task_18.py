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
def task_8_28():
    for i in range(8):
        if wall_is_above() == False or wall_is_on_the_right():
            break
        elif wall_is_above() == False and wall_is_on_the_right():
            break
        move_right()
    for i in range(8):
        if wall_is_above() == False or wall_is_on_the_left():
            break
        elif wall_is_above() == False and wall_is_on_the_left():
            break
        move_left()
    
    while wall_is_above() == False:
        move_up()
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == '__main__':
    run_tasks()
