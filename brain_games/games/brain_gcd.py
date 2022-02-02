#!/usr/bin/env python

from random import randint


TASK_DESCRIPTION = ('Find the greatest common divisor of given numbers.')

FIRST_NUM = 1
SECOND_NUM = 10


def get_game_round():
    number1 = randint(FIRST_NUM, SECOND_NUM)
    number2 = randint(FIRST_NUM, SECOND_NUM)
    divisor = []
    question = (str(number1) + ' ' + str(number2))
    for i in range(1, 11):
        if number1 % i == 0 and number2 % i == 0:
            divisor.append(i)
    correct_answer = divisor[-1]
    return question, str(correct_answer)
