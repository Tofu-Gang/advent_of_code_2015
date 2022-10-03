__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 1: Not Quite Lisp ---

Santa is trying to deliver presents in a large apartment building, but he can't
find the right floor - the directions he got are a little confusing. He starts
on the ground floor (floor 0) and then follows the instructions one character at
a time.

An opening parenthesis, (, means he should go up one floor, and a closing
parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will
never find the top or bottom floors.
"""

from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_01/input.txt"
FLOOR_UP = "("
FLOOR_DOWN = ")"


################################################################################

def puzzle_01() -> None:
    """
    Use the puzzle input txt file. To what floor do the instructions take Santa?

    :return: None; Answer should be 232.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        contents = f.read()
        floor = contents.count(FLOOR_UP) - contents.count(FLOOR_DOWN)
        print_puzzle_solution(floor)


################################################################################

def puzzle_02() -> None:
    """
    Now, given the same instructions, find the position of the first character
    that causes him to enter the basement (floor -1). The first character in the
    instructions has position 1, the second character has position 2, and so on.

    What is the position of the character that causes Santa to first enter the
    basement?

    :return: None; Answer should be 1783.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        contents = f.read()
        # floor instructions translated to +1 or -1 integers
        instructions = [1 if literal == FLOOR_UP
                        else -1
                        for literal in contents]
        # what floor Santa will end up by following every instruction
        floors = [sum(instructions[:i]) for i in range(len(instructions))]
        # index of the first instruction that causes Santa to end up
        # in the basement
        first_basement_instruction = floors.index(
            next(floor for floor in floors if floor < 0))
        print_puzzle_solution(first_basement_instruction)

################################################################################
