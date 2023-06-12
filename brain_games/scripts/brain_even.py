#!/usr/bin/env python3

import prompt
from brain_games.cli import welcome_user
import random


GAME_DURATION = 3
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


def play(game):
    """Common game logic."""
    name: str = welcome_user()
    score: int = 0
    print(DESCRIPTION)
    while True:
        correct_answer, expression = get_expression_and_answer()
        print(f"Question: {expression}")
        answer: str = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(
                f"""'{answer}' is wrong answer ;(. """
                f"""Correct answer was '{correct_answer}'.\n"""
                f"""Let's try again, {name}!"""
            )
            break
        if score == GAME_DURATION:
            print(f"Congratulations, {name}!")
            break


def main():
    """Play brain even game."""
    play(is_even)


if __name__ == "__main__":
    main()
