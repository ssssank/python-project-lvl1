from brain_games.helpers import get_random_int

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(one, two):
    return get_gcd(two, one % two) if two > 0 else one


def prepare_round():
    number_one = get_random_int(0, 20)
    number_two = get_random_int(0, 20)
    question = f'{number_one} {number_two}'
    answer = str(get_gcd(number_one, number_two))
    return (question, answer)
