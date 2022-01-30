from random import randint


def starting_sentence():
    return print('Answer "yes" if the number is even, otherwise answer "no".')


correct_answer = ['yes', 'yes', 'yes']

question = []


def random_num():
    for i in range(3):
        num = randint(1, 25)
        question.append(num)


random_num()

print(question)



def main():
    pass


if __name__ == '__main__':
    main()
