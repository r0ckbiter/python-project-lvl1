#!/usr/bin/env python

from random import randint


TASK_DESCRIPTION = ('Answer "yes" if the number is even, '
                    'otherwise answer "no".')

FIRST_NUM = 1
SECOND_NUM = 10


def get_game_round():
    random_num = randint(FIRST_NUM, SECOND_NUM)
    if random_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(random_num), str(correct_answer)
