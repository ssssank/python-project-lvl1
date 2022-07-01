from random import choice
from brain_games.helpers import get_random_int

DESCRIPTION = 'What is the result of the expression?'

operations = ['+', '-', '*']


def calculate(number_one, operation, number_two):
    match operation:
        case '+':
            return int(number_one) + int(number_two)
        case '-':
            return int(number_one) - int(number_two)
        case '*':
            return int(number_one) * int(number_two)
        case _:
            raise Exception('Unknown operation!')


def prepare_round():
    number_one = get_random_int(0, 50)
    number_two = get_random_int(0, 10)
    operation = choice(operations)
    question = f'{number_one} {operation} {number_two}'
    answer = str(calculate(number_one, operation, number_two))
    return question, answer
