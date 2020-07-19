"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making
sequences by reading aloud the previous sequence and using that reading as the
next sequence.
"""

################################################################################

def _look_and_say(look: str) -> str:
    """
    Take the input and use it to generate the next look-and-say sequence.

    :param look: input to use in generation of the next look-and-say sequence
    :return: next look-and-say sequence
    """

    say = ""
    i = 0

    while i < len(look):
        number = look[i]
        count = 1
        j = i + 1

        while j < len(look) and look[j] == number:
            j += 1
            count += 1

        say += str(count)+number
        i += count

    return say

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

    with open("src/day_10/input.txt", "r") as f:
        look = f.read()

        for _ in range(40):
            look = _look_and_say(look)

        print(len(look))


################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################