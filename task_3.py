#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    pass
    for i in range(9):
        move_right()
        if wall_is_on_the_right():
            break
        


if __name__ == '__main__':
    run_tasks()
