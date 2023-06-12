"""Brain-Even Game."""

import random

DESCRIPTION = """Answer "yes" if the number is even, otherwise answer "no"."""

def is_even(number: int) -> bool:
    """Checks if given number is even."""
    return number % 2 == 0


def get_expression_and_answer() -> tuple:
    """Creates task expression and correct answer."""
    answers = ["no", "yes"]
    number = random.randint(1, 100)
    correct_answer = answers[is_even(number)]
    return correct_answer, number