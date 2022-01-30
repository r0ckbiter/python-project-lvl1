#!/usr/bin/env python

import prompt
import operator
from random import randint
from random import choice


print("Welcome to the Brain Games!")



name = get_name()


opr = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def calc():
    score = 0
    while score < 3:
        number1 = randint(5, 10)
        number2 = randint(1, 5)
        x = opr.keys()
        x = list(x)
        operator = choice(x)
        print(f"Question: {number1} {operator} {number2}")
        result = opr.get(operator)
        answer = prompt.integer('Your answer: ')
        correct_answer = (result(number1, number2))
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name.title()}!")
            break
        if score == 3:
            print(f"Congratulations, {name.title()}!")


def main():
    print(f'Hello, {name.title()}!')
    print('What is the result of the expression?')
    calc()


if __name__ == '__main__':
    main()
