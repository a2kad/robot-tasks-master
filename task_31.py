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

def serch_left():
    while not wall_is_on_the_left():
        move_left()
        if not wall_is_beneath():
            return True
            break
def serch_right():
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_beneath():
            return True
            break


@task(delay=0.01)
def task_8_30():
    
    while serch_left() or serch_right():
        serch_left()
        serch_right()
        if serch_left():
            while not wall_is_beneath():
                move_down()
                break
        elif serch_right():
            while not wall_is_beneath():
                move_down()
                break
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
