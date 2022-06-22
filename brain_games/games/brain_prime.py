from brain_games.helpers import get_random_int
from brain_games.engine import start_game
from brain_games.engine import GAME_ROUNDS

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i < number / 2:
        if number % i == 0:
            return False
        i += 1
    return True


def prepare_round():
    number = get_random_int(100)
    answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return [question, answer]


def run_game():
    rounds = []
    for i in range(GAME_ROUNDS):
        rounds.append(prepare_round())
    start_game(description, rounds)
