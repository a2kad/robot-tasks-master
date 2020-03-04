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
def task_8_29():
    for i in range (9):
        if wall_is_on_the_left() == False and wall_is_above() == False:
            break
        move_left()
        if wall_is_on_the_left() and wall_is_above() == False:
            break
        if wall_is_on_the_left():
            break
        
    
    for i in range (9):
        if wall_is_on_the_right() == False and wall_is_above() == False:
            break
        move_right()
        if wall_is_on_the_right() and wall_is_above() == False:
            break
        if wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
            break
        if wall_is_on_the_right():
            break
        
    while wall_is_above() == False:
        move_up()
    while wall_is_on_the_left() == False:
        if wall_is_beneath():
            break
        move_left()         
    
if __name__ == '__main__':
    run_tasks()
