from brain_games.helpers import get_random_int

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(str(start + step * i))
    return progression


def prepare_round():
    start = get_random_int(0, 30)
    step = get_random_int(0, 20)
    hidden_position = get_random_int(0, PROGRESSION_LENGTH - 1)
    progression = get_progression(start, step, PROGRESSION_LENGTH)
    answer = str(progression[hidden_position])
    progression[hidden_position] = '..'
    question = " ".join(progression)
    return question, answer
