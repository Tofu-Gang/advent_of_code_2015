from itertools import permutations
from sys import maxsize

"""
--- Day 9: All in a Single Night ---
"""

LOCATIONS_DENOMINATOR = "to"
DISTANCE_DENOMINATOR = "="

################################################################################

def puzzle_01() -> None:
    """
    Every year, Santa manages to deliver all of his presents in a single night.

    This year, however, he has some new locations to visit; his elves have
    provided him the distances between every pair of locations. He can start and
    end at any two (different) locations he wants, but he must visit each
    location exactly once. What is the shortest distance he can travel to
    achieve this?

    :return: None; Answer should be 117.
    """

    with open("src/day_09/input.txt", "r") as f:
        lines = f.readlines()
        distances = {}

        for line in lines:
            stripped = line.strip()
            path = stripped.split(LOCATIONS_DENOMINATOR)
            location1 = path[0].strip()
            location2 = path[1].split(DISTANCE_DENOMINATOR)[0].strip()
            distance = int(path[1].split(DISTANCE_DENOMINATOR)[1])

            try:
                distances[location1].update({location2: distance})
            except KeyError:
                distances[location1] = {location2: distance}
            try:
                distances[location2].update({location1: distance})
            except KeyError:
                distances[location2] = {location1: distance}

        print(min([sum([distances[perm[i]][perm[i + 1]]
                        for i in range(len(perm) - 1)])
                   for perm in permutations(distances.keys())]))

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################