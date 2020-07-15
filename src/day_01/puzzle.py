"""
Santa is trying to deliver presents in a large apartment building, but he can't
find the right floor - the directions he got are a little confusing. He starts
on the ground floor (floor 0) and then follows the instructions one character at
a time.

An opening parenthesis, (, means he should go up one floor, and a closing
parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will
never find the top or bottom floors.
"""

################################################################################

def puzzle_01() -> None:
    """
    Use the puzzle input txt file. To what floor do the instructions take Santa?
    Answer should be 232.

    :return: None
    """

    floor = 0
    with open("src/day_01/input.txt", "r") as input:
        for literal in input.read():
            if literal == "(":
                floor += 1
            elif literal == ")":
                floor -= 1
    print(floor)

################################################################################