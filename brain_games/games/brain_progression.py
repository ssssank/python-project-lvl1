from brain_games.helpers import get_random_int
from brain_games.engine import start_game
from brain_games.engine import GAME_ROUNDS

description = 'What number is missing in the progression?'
progression_length = 10


def get_progression(start, step):
    progression = []
    i = 0
    while i < progression_length:
        progression.append(str(start + step * i))
        i += 1
    return progression


def prepare_round():
    start = get_random_int(30)
    step = get_random_int(20)
    hidden_position = get_random_int(progression_length - 1)
    progression = get_progression(start, step)
    answer = str(progression[hidden_position])
    progression[hidden_position] = '..'
    question = f'{" ".join(progression)}'
    return [question, answer]


def run_game():
    rounds = []
    for i in range(GAME_ROUNDS):
        rounds.append(prepare_round())
    start_game(description, rounds)
