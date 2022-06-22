from prompt import string


GAME_ROUNDS = 3


def start_game(description, rounds):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}')
    print(description)

    for round in rounds:
        [question, answer] = round

        print(f'Question: {question}')
        userAnswer = string('Your answer: ')

        if (userAnswer == answer):
            print('Correct')
        else:
            print(f"'{userAnswer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}! ')
            return

    print(f'Congratulations, {name}!')
