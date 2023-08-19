"""Brain Games engine. Enjoy!"""

import prompt


GAME_DURATION = 3


def play(game):
    """Common game logic."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(game.DESCRIPTION)

    for _ in range(GAME_DURATION):
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
