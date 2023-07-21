"""Brain Games engine. Enjoy!"""

import prompt
from brain_games.cli import welcome_user

GAME_DURATION = 3
WELCOME_MESSAGE = "Welcome to the Brain Games!"


def play(game):
    """Common game logic."""
    name: str = welcome_user()
    print(game.DESCRIPTION)

    for score in range(GAME_DURATION):
        correct_answer, expression = game.get_expression_and_answer()
        print(f"Question: {expression}")
        answer: str = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(
                f"""'{answer}' is wrong answer ;(. """
                f"""Correct answer was '{correct_answer}'.\n"""
                f"""Let's try again, {name}!""")
            break
        print("Correct!")
    else:
        print(f"Congratulations, {name}!")