from re import compile
from typing import Tuple
from src.day_14.reindeer import Reindeer

"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must
rest occasionally to recover their energy. Santa would like to know which of his
reindeer is fastest, and so he has them race.
"""

RACE_DURATION = 2503

################################################################################

def _load_reindeer_stats() -> Tuple[Reindeer]:
    """
    Load reindeer stats from the input file. Store it in a tuple of Reindeer
    objects.

    :return: reindeer stats
    """

    with open("src/day_14/input.txt", "r") as f:
        reindeer = []
        regex = compile(r'\d+')
        lines = f.readlines()

        for line in lines:
            name = line.split(" ")[0]
            numbers = regex.findall(line)
            speed = int(numbers[0])
            fly_time = int(numbers[1])
            rest_time = int(numbers[2])
            reindeer.append(Reindeer(name, speed, fly_time, rest_time))

        return tuple(reindeer)

################################################################################

def puzzle_01() -> None:
    """
    Given the descriptions of each reindeer (in the puzzle input), after exactly
    2503 seconds, what distance has the winning reindeer traveled?

    :return: None; Answer should be 2640.
    """

    reindeer = _load_reindeer_stats()
    [a_reindeer.start() for a_reindeer in reindeer]
    [a_reindeer.advance() for _ in range(RACE_DURATION) for a_reindeer in reindeer]
    print(max([a_reindeer.distance for a_reindeer in reindeer]))

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

    :return: None; Wrong answers: 1151, 2585-too high
    """

    # reindeer = _load_reindeer_stats()
    # for a_reindeer in reindeer:
    #     a_reindeer.start()
    #
    # for _ in range(RACE_DURATION):
    #     for a_reindeer in reindeer:
    #         a_reindeer.advance()
    #     max_distance = max([a_reindeer.distance for a_reindeer in reindeer])
    #     for a_reindeer in reindeer:
    #         if a_reindeer.distance == max_distance:
    #             a_reindeer.award_point()
    #
    # max_points = max([a_reindeer.points for a_reindeer in reindeer])
    # print([a_reindeer.distance for a_reindeer in reindeer if a_reindeer.points == max_points][0])
    pass

################################################################################
