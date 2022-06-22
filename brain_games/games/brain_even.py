from brain_games.helpers import get_random_int
from brain_games.engine import start_game
from brain_games.engine import GAME_ROUNDS

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def prepare_round():
    number = get_random_int(100)
    answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return [question, answer]


def run_game():
    rounds = []
    for i in range(GAME_ROUNDS):
        rounds.append(prepare_round())
    start_game(description, rounds)
