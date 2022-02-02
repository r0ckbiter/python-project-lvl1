#!/usr/bin/env python

import operator
from random import randint, choice

TASK_DESCRIPTION = 'What is the result of the exspression?'
FIRST_NUM = 1
SECOND_NUM = 10

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

operator_symbols = list(operators.keys())


def get_game_round():
    number1 = randint(FIRST_NUM, SECOND_NUM)
    number2 = randint(FIRST_NUM, SECOND_NUM)
    operator = choice(operator_symbols)
    current_operator = operators.get(operator)
    question = (str(number1) + ' ' + operator + ' ' + str(number2))
    correct_answer = (current_operator(number1, number2))
    return question, str(correct_answer)
