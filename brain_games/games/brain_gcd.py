from brain_games.helpers import get_random_int
from brain_games.engine import start_game
from brain_games.engine import GAME_ROUNDS

description = 'Find the greatest common divisor of given numbers.'


def get_gcd(one, two):
    return get_gcd(two, one % two) if two > 0 else one


def prepare_round():
    number_one = get_random_int(20)
    number_two = get_random_int(20)
    question = f'{number_one} {number_two}'
    answer = str(get_gcd(number_one, number_two))
    return [question, answer]


def run_game():
    rounds = []
    for i in range(GAME_ROUNDS):
        rounds.append(prepare_round())
    start_game(description, rounds)
