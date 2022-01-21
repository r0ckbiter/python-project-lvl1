#!/usr/bin/env python

import prompt
from random import randint


print("Welcome to the Brain Games!")


def name():
    name = prompt.string('May I have your name? ')
    return name


name = name()


def random_num():
    number = randint(1, 25)
    return number


def wrong():
    return print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                 f"\nLet's try again, {name.title()}!")


def is_even():
    score = 0
    while score < 3:
        num = random_num()
        print(f'Question: {num}')
        answr = prompt.string('Your answer: ')
        if answr == 'yes' and num % 2 == 0:
            print('Correct!')
            score += 1
        elif answr == 'no' and num % 2 != 0:
            print('Correct!')
            score += 1
        elif answr == 'yes' and num % 2 != 0 or answr == 'no' and num % 2 == 0:
            wrong()
            score == 0
        else:
            print("You must type only 'yes' or 'no' if you want to win."
                  "\nLet's take another try!")
            score == 0
        if score == 3:
            print(f"Congratulations, {name.title()}!")


def main():
    print(f'Hello, {name.title()}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_even()


if __name__ == '__main__':
    main()
