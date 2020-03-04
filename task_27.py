#!/usr/bin/python3
"""
move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)
wall_is_above()	если сверху стена, возвращает True, иначе — False
wall_is_beneath()	если снизу стена, возвращает True, иначе — False
wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
	если справа стена, возвращает True, иначе — False
fill_cell()	Закрасить текущую клетку
cell_is_filled()	Возвращает True, если текущая клетка закрашена
mov(r, v)	Поместить значение v в регистр r
"""
from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    n = 0
    nn = n
    while not wall_is_on_the_right():
        if n < nn:
            
            n += 1
            move_right()
        else:
            
            n = 0
            nn += 1
            move_right()
            if not wall_is_on_the_right():
                
                fill_cell()
"""
    global i
    
    i=1
    while wall_is_on_the_right() == False:
        move_right()
        i = i + 1
        print(i)
        if wall_is_on_the_right():
            break
            
    while not wall_is_on_the_left():
        move_left()
    
    x=1
    n=0
    move_right()
    while x < 10:
        fill_cell()
        move_right(n=x)
        x = x + 1
        print(x)
        i = i-x
        print('i= ')
        print(i)
        if i<0:
            z = x-i
            fill_cell()
            move_right(n=(z-1))
            break
            """
        
        


if __name__ == '__main__':
    run_tasks()
