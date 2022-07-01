from prompt import string


ROUNDS_COUNT = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.DESCRIPTION)

    for i in range(ROUNDS_COUNT):
        question, answer = game.prepare_round()

        print(f'Question: {question}')
        userAnswer = string('Your answer: ')

        if (userAnswer == answer):
            print('Correct')
        else:
            print(f"'{userAnswer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}! ')
            return

    print(f'Congratulations, {name}!')
