from random import random
from prompt import string


GAME_ROUNDS = 3
description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def getRandomInt():
    return round(random() * 100)


def run_game():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}')
    print(description)
    i = 0
    while i < GAME_ROUNDS:
        randomNumber = getRandomInt()
        answer = 'yes' if is_even(randomNumber) else 'no'
        question = str(randomNumber)

        print(f'Question: {question}')
        userAnswer = string('Your answer: ')

        if (userAnswer == answer):
            print('Correct')
        else:
            print(f"'{userAnswer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}! ')
            return
        i += 1
    print(f'Congratulations, {name}!')
