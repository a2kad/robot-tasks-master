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

def walk_upstairs():
    n = 0
    while not wall_is_above():
        move_up()
        if cell_is_filled():
            n += 1
        else:
            fill_cell()
    while not wall_is_beneath():
        move_down()
    return n
  
@task
def task_8_18():
    n = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            n += 1
        if wall_is_above():
            if not cell_is_filled():
                fill_cell()
        else:
            n += walk_upstairs()
        move_right()
    mov('ax', n)

'''@task(delay=0.01)
def task_8_18():
    i = 0
    ax = 0
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
            move_right()
        
        elif not wall_is_above():
            while not wall_is_above():
                if cell_is_filled():
                    i += 1
                    
                    move_up()
                elif not cell_is_filled():
                    fill_cell()
                    move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
            move_right()
    mov('ax',i)  '''          
            


if __name__ == '__main__':
    run_tasks()
