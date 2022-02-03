#!/usr/bin/env python

from random import randint


TASK_DESCRIPTION = ('What number is missing in the progression?')

FIRST_NUM = 1
SECOND_NUM = 100


def build_progression(first_element, step):
    member = first_element
    progression = [first_element]
    for i in range(10):
        member += step
        progression.append(member)
    return progression


def get_string_progression(progression, hidden_number):
    progression_string = []
    for index in range(0, 10):
        progression_string.append(str(progression[index]))
    progression_string[hidden_number] = '..'
    return " ".join(progression_string)


def get_game_round():
    first_element = randint(FIRST_NUM, SECOND_NUM)
    step = randint(1, 10)
    hidden_number = randint(1, 9)
    progression = build_progression(first_element, step)
    return (get_string_progression(progression, hidden_number),
            str(progression[hidden_number]))
