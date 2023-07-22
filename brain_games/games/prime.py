"""Brain Prime Game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def correct_answer(bool):
    return 'yes' if bool else 'no'

def get_expression_and_answer() -> tuple:
    """Make game question and answer."""
    min_number = 1
    max_number = 42
    number = randint(min_number, max_number)
    question = str(number)
    return correct_answer(is_prime(number)), question
