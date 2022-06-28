from brain_games.helpers import get_random_int

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


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
    number = get_random_int(0, 100)
    answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return (question, answer)
