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

################################################################################

def puzzle_01() -> None:
    """
    Use the puzzle input txt file. To what floor do the instructions take Santa?

    :return: None; Answer should be 232.
    """

    floor = 0
    with open("src/day_01/input.txt", "r") as f:
        for literal in f.read():
            if literal == "(":
                floor += 1
            elif literal == ")":
                floor -= 1
    print(floor)

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

    floor = 0
    with open("src/day_01/input.txt", "r") as f:
        input_string = f.read()
        for i in range(len(input_string)):
            literal = input_string[i]
            if literal == "(":
                floor += 1
            elif literal == ")":
                floor -= 1

            if floor < 0:
                print(i + 1)
                break
        else:
            print("Basement not reached.")

################################################################################