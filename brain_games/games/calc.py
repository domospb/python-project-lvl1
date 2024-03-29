from random import choice, randint
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def get_expression_and_answer() -> tuple:
    """Make game question and answer."""
    min_number = 1
    max_number = 100
    operand_first = randint(min_number, max_number)
    operand_second = randint(min_number, max_number)
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    correct_answer = operation(operand_first, operand_second)
    question = f"{operand_first} {operator} {operand_second}"
    return str(correct_answer), question
