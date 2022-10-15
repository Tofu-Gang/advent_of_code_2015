__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided 
him the distances between every pair of locations. He can start and end at any 
two (different) locations he wants, but he must visit each location exactly 
once.
"""

from itertools import permutations
from typing import Dict
from src.utils.utils import print_puzzle_solution

LOCATIONS_DENOMINATOR = "to"
DISTANCE_DENOMINATOR = "="
INPUT_FILE_PATH = "src/day_09/input.txt"


################################################################################

def _load_distances() -> Dict[str, Dict[str, int]]:
    """
    Loads distances from the puzzle input to a dictionary. In this dictionary,
    keys are locations and values are dictionaries where keys are neighbour
    locations and value the distance to this neighbour location.

    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        distances = {}

        for line in lines:
            path = line.strip().split(LOCATIONS_DENOMINATOR)
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
        return distances


################################################################################

def puzzle_01() -> None:
    """
    What is the shortest distance Santa can travel to visit each location
    exactly once?

    :return: None; Answer should be 117.
    """

    distances = _load_distances()
    print_puzzle_solution(min([sum([distances[perm[i]][perm[i + 1]]
                                    for i in range(len(perm) - 1)])
                               for perm in permutations(distances.keys())]))


################################################################################

def puzzle_02() -> None:
    """
    The next year, just to show off, Santa decides to take the route with the
    longest distance instead.

    He can still start and end at any two (different) locations he wants, and he
    still must visit each location exactly once.

    What is the distance of the longest route?

    :return: None; Answer should be 909.
    """

    distances = _load_distances()
    print_puzzle_solution(max([sum([distances[perm[i]][perm[i + 1]]
                                    for i in range(len(perm) - 1)])
                               for perm in permutations(distances.keys())]))

################################################################################
