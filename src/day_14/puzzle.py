__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must
rest occasionally to recover their energy. Santa would like to know which of his
reindeer is fastest, and so he has them race.
"""

from re import compile
from typing import Tuple
from src.day_14.reindeer import Reindeer
from src.utils.utils import print_puzzle_solution

RACE_DURATION = 2503
INPUT_FILE_PATH = "src/day_14/input.txt"


################################################################################

def _load_reindeer_stats() -> Tuple[Reindeer]:
    """
    Load reindeer stats from the input file. Store it in a tuple of Reindeer
    objects.

    :return: reindeer stats
    """

    with open(INPUT_FILE_PATH, "r") as f:
        pattern = compile(r'\d+')
        lines = f.readlines()
        return tuple(Reindeer(line.split(" ")[0],
                              int(pattern.findall(line)[0]),
                              int(pattern.findall(line)[1]),
                              int(pattern.findall(line)[2]))
                     for line in lines)


################################################################################

def puzzle_01() -> None:
    """
    Given the descriptions of each reindeer (in the puzzle input), after exactly
    2503 seconds, what distance has the winning reindeer traveled?

    :return: None; Answer should be 2640.
    """

    reindeer = _load_reindeer_stats()
    [a_reindeer.start() for a_reindeer in reindeer]
    [a_reindeer.advance()
     for _ in range(RACE_DURATION)
     for a_reindeer in reindeer]
    print_puzzle_solution(max([a_reindeer.distance for a_reindeer in reindeer]))


################################################################################

def puzzle_02() -> None:
    """
    Seeing how reindeer move in bursts, Santa decides he's not pleased with the
    old scoring system.

    Instead, at the end of each second, he awards one point to the reindeer
    currently in the lead. (If there are multiple reindeer tied for the lead,
    they each get one point.) He keeps the traditional 2503 second time limit,
    of course, as doing otherwise would be entirely ridiculous.

    Again given the descriptions of each reindeer (in the puzzle input), after
    exactly 2503 seconds, how many points does the winning reindeer have?

    :return: None; Answer should be 1102.
    """

    reindeer = _load_reindeer_stats()
    [a_reindeer.start() for a_reindeer in reindeer]

    for _ in range(RACE_DURATION):
        for a_reindeer in reindeer:
            a_reindeer.advance()

        max_distance = max([a_reindeer.distance for a_reindeer in reindeer])
        [a_reindeer.award_point() for a_reindeer in reindeer
         if a_reindeer.distance == max_distance]

    print_puzzle_solution(max([a_reindeer.points for a_reindeer in reindeer]))

################################################################################
