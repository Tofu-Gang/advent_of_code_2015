__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all
into your refrigerator, you'll need to move it into smaller containers. You take
an inventory of the capacities of the available containers.
"""

from typing import Tuple
from itertools import combinations
from src.utils.utils import print_puzzle_solution

EGGNOG_LITRES = 150
INPUT_FILE_PATH = "src/day_17/input.txt"


################################################################################

def load_containers() -> Tuple[int]:
    """
    :return: list of all containers capacities
    """

    with open(INPUT_FILE_PATH, "r") as f:
        return tuple([int(line.strip()) for line in f.readlines()])


################################################################################

def puzzle_01() -> None:
    """
    Filling all containers entirely, how many different combinations of
    containers can exactly fit all 150 liters of eggnog?

    :return: None; Answer should be 1304.
    """

    containers = load_containers()
    print_puzzle_solution(len(tuple(filter(
        lambda combination: sum(combination) == EGGNOG_LITRES,
        [combination
         for i in range(len(containers))
         for combination in combinations(containers, i)]))))


################################################################################

def puzzle_02() -> None:
    """
    While playing with all the containers in the kitchen, another load of eggnog
    arrives! The shipping and receiving department is requesting as many
    containers as you can spare.

    Find the minimum number of containers that can exactly fit all 150 liters of
    eggnog. How many different ways can you fill that number of containers and
    still hold exactly 150 litres?

    :return: None; Answer should be 18.
    """

    containers = load_containers()
    combinations_lengths = tuple(map(
        lambda combination: len(combination),
        filter(lambda combination: sum(combination) == EGGNOG_LITRES,
               [combination
                for i in range(len(containers))
                for combination in combinations(containers, i)])))
    print_puzzle_solution(combinations_lengths.count(min(combinations_lengths)))

################################################################################
