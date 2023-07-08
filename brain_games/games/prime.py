"""Brain Prime Game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return "no"
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return "no"
    return "yes"


def get_expression_and_answer() -> tuple:
    """Make game question and answer."""
    min_number = 1
    max_number = 42
    number = randint(min_number, max_number)
    question = str(number)
    return is_prime(number), question
