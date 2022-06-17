from prompt import string
from brain_games.helpers import get_random_int
from brain_games.engine import start_game
from brain_games.engine import GAME_ROUNDS

description = 'What is the result of the expression?'

operations = ['+', '-', '*']

def calculate(expression):
    [number_one, operation, number_two] = expression.split()
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
    number_one = get_random_int(50)
    number_two = get_random_int(10)
    operation = operations[get_random_int(len(operations) - 1)]
    question = f'{number_one} {operation} {number_two}'
    answer = str(calculate(question))
    return [question, answer]

def run_game():
    rounds = []
    for i in range(GAME_ROUNDS):
        rounds.append(prepare_round())
    start_game(description, rounds)
