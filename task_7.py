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
def task_5_4():
    for i in range (19):
        move_down()
        if wall_is_beneath():
            break
    for i in range (19):    
        move_right()
        if  wall_is_beneath() == False:
            break
    move_down()
    for i in range (19):
        move_left()
        if wall_is_on_the_left():
            break

if __name__ == '__main__':
    run_tasks()
