#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_above() and wall_is_on_the_right() and wall_is_beneath():
        move_left()
    elif wall_is_above() and wall_is_on_the_left() and wall_is_beneath():
        move_right()
    elif wall_is_on_the_left() and wall_is_above() and wall_is_on_the_right():
        move_down()
    else:
        move_up()


if __name__ == '__main__':
    run_tasks()
