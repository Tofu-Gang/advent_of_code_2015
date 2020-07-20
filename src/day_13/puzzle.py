from re import compile
from typing import Dict, Tuple
from itertools import permutations

"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not
everyone gets along! This year, you resolve, will be different. You're going to
find the optimal seating arrangement and avoid all those awkward conversations.
"""

WOULD_DENOMINATOR = "would"
GAIN = "gain"
LOSE = "lose"
HAPPINESS_DENOMINATOR = "happiness units by sitting next to"

################################################################################

def _get_happiness_info() -> Dict[str, Dict[str, int]]:
    """
    Creates a dictionary with info about everyone seated at the table with their
    happiness values changes according to their neighbour.

    :return: everyone's happiness info
    """

    happiness_info = {}

    with open("src/day_13/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            person = line.split(WOULD_DENOMINATOR)[0].strip()
            neighbour = line.split(HAPPINESS_DENOMINATOR)[1].strip()[:-1]
            regex = compile(r'\d+')

            if GAIN in line:
                happiness = int(regex.findall(line)[0])
            elif LOSE in line:
                happiness = int("-" + regex.findall(line)[0])
            else:
                happiness = None

            if person not in happiness_info:
                happiness_info.update({person: {neighbour: happiness}})
            else:
                happiness_info[person].update({neighbour: happiness})

        return happiness_info

################################################################################

def _get_seating_happiness(seating: Tuple,
                           happiness_info: Dict[str, Dict[str, int]]) -> int:
    """
    Returns a total happiness of the given seating around the table.

    :param seating: a combination of arrangement of people sitting around the
    table
    :return: a total happiness of this seating arrangement
    """

    return sum([happiness_info[seating[i]][seating[i - 1]]
                for i in range(len(seating))]) \
           + sum([happiness_info[seating[i]][seating[i + 1]]
                  for i in range(len(seating) - 1)]) \
           + happiness_info[seating[-1]][seating[0]]

################################################################################

def puzzle_01() -> None:
    """
    You start by writing up a list of everyone invited and the amount their
    happiness would increase or decrease if they were to find themselves sitting
    next to each other person. You have a circular table that will be just big
    enough to fit everyone comfortably, and so each person will have exactly two
    neighbors.

    What is the total change in happiness for the optimal seating arrangement of
    the actual guest list?

    :return: None; Answer should be 709.
    """

    happiness_info = _get_happiness_info()
    print(max([_get_seating_happiness(perm, happiness_info)
               for perm in permutations(happiness_info.keys())]))

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################
