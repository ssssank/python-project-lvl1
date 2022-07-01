from brain_games.helpers import get_random_int

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def prepare_round():
    number = get_random_int(0, 100)
    answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return question, answer
