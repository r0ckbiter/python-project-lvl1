#!/usr/bin/env python

from random import randint


TASK_DESCRIPTION = ('Answer "yes" if given number is prime, '
                    'otherwise answer "no".')

FIRST_NUM = 3
SECOND_NUM = 50


def get_game_round():
    random_num = randint(FIRST_NUM, SECOND_NUM)
    divider = 2
    while divider <= random_num / 2:
        if random_num % divider == 0:
            correct_answer = "no"
            break
        divider += 1
    else:
        correct_answer = "yes"
    return str(random_num), correct_answer
