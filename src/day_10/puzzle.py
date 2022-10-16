__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
John Horton Conway (1937-2020)

--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making
sequences by reading aloud the previous sequence and using that reading as the
next sequence.
"""

from re import compile
from src.utils.utils import print_puzzle_solution

PUZZLE_INPUT = "1113122113"


################################################################################

def _look_and_say(look: str) -> str:
    """
    Take the input and use it to generate the next look-and-say sequence.

    :param look: input to use in generation of the next look-and-say sequence
    :return: next look-and-say sequence
    """

    pattern = compile(r"(.)\1*")
    return "".join([
        str(len(match.group())) + match.group()[0]
        for match in pattern.finditer(look)])


################################################################################

def puzzle_01() -> None:
    """
    Look-and-say sequences are generated iteratively, using the previous value
    as input for the next step. For each step, take the previous value, and
    replace each run of digits (like 111) with the number of digits (3) followed
    by the digit itself (1).

    Starting with the digits in your puzzle input, apply this process 40 times.
    What is the length of the result?

    :return: None; Answer should be 360154.
    """

    look = PUZZLE_INPUT

    for _ in range(40):
        look = _look_and_say(look)

    print_puzzle_solution(len(look))


################################################################################

def puzzle_02() -> None:
    """
    Neat, right? You might also enjoy hearing John Conway talking about this
    sequence (that's Conway of Conway's Game of Life fame).

    https://www.youtube.com/watch?v=ea7lJkEhytA

    Now, starting again with the digits in your puzzle input, apply this process
    50 times. What is the length of the new result?

    :return: None; Answer should be 5103798.
    """

    look = PUZZLE_INPUT

    for _ in range(50):
        look = _look_and_say(look)

    print_puzzle_solution(len(look))

################################################################################
