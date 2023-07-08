"""Brain-GCD Game."""

from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_expression_and_answer() -> tuple:
    """Make game question and answer."""
    min_number = 1
    max_number = 99
    number_first = randint(min_number, max_number)
    number_second = randint(min_number, max_number)
    question = f'{number_first} {number_second}'
    correct_answer = gcd(number_first, number_second)
    return str(correct_answer), question
