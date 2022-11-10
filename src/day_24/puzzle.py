__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple

"""
--- Day 24: It Hangs in the Balance ---

It's Christmas Eve, and Santa is loading up the sleigh for this year's 
deliveries. However, there's one small problem: he can't get the sleigh to 
balance. If it isn't balanced, he can't defy physics, and nobody gets presents 
this year.

No pressure.
"""

from numpy import prod
from sys import maxsize
from random import sample, randint
from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_24/input.txt"


################################################################################

def quantum_entanglement_random(weights: Tuple[int],
                                compartments: int,
                                loop_count: int = 10000000,
                                quantum_entanglement_bound: int = maxsize) \
        -> int:
    """
    Take random sample from the provided list of weights. Find the one that has
    the minimum quantum entanglement value. This combination of weights must
    have the desired sum (sum of all the weights divided by the number of sleigh
    compartments) and the least possible number of packages.

    :param weights: list of package weights
    :param compartments: number of sleigh compartments
    :param loop_count: number of attempts to find the minimum quantum
    entanglement value
    :param quantum_entanglement_bound: discard all the found quantum
    entanglements values that are over this value
    :return: minimum quantum entanglement value
    """

    min_passenger_compartment_size = maxsize
    min_quantum_entanglement = quantum_entanglement_bound
    desired_weight = sum(weights) / compartments

    for _ in range(loop_count):
        sample_size = randint(1, len(weights) - 1)
        packages = sample(weights, sample_size)

        if sum(packages) == desired_weight:
            if len(packages) <= min_passenger_compartment_size:
                min_passenger_compartment_size = len(packages)
                quantum_entanglement = prod(packages)

                if quantum_entanglement < min_quantum_entanglement:
                    min_quantum_entanglement = quantum_entanglement

    return min_quantum_entanglement


################################################################################

def puzzle_01() -> None:
    """
    Santa has provided you a list of the weights of every package he needs to
    fit on the sleigh. The packages need to be split into three groups of
    exactly the same weight, and every package has to fit. The first group goes
    in the passenger compartment of the sleigh, and the second and third go in
    containers on either side. Only when all three groups weigh exactly the same
    amount will the sleigh be able to fly. Defying physics has rules, you know!

    Of course, that's not the only problem. The first group - the one going in
    the passenger compartment - needs as few packages as possible so that Santa
    has some legroom left over. It doesn't matter how many packages are in
    either of the other two groups, so long as all of the groups weigh the same.

    Furthermore, Santa tells you, if there are multiple ways to arrange the
    packages such that the fewest possible are in the first group, you need to
    choose the way where the first group has the smallest quantum entanglement
    to reduce the chance of any "complications". The quantum entanglement of a
    group of packages is the product of their weights, that is, the value you
    get when you multiply their weights together. Only consider quantum
    entanglement if the first group has the fewest possible number of packages
    in it and all groups weigh the same amount.

    What is the quantum entanglement of the first group of packages in the ideal
    configuration?

    :return: None; Answer should be 10439961859.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        weights = tuple(int(line.strip()) for line in f.readlines())
        min_quantum_entanglement = quantum_entanglement_random(weights, 3)
        print_puzzle_solution(min_quantum_entanglement)


################################################################################

def puzzle_02() -> None:
    """
    That's weird... the sleigh still isn't balancing.

    "Ho ho ho", Santa muses to himself. "I forgot the trunk".

    Balance the sleigh again, but this time, separate the packages into four
    groups instead of three. The other constraints still apply.

    :return: None; Answer should be 72050269.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        weights = tuple(int(line.strip()) for line in f.readlines())
        min_quantum_entanglement = quantum_entanglement_random(weights, 4)
        print_puzzle_solution(min_quantum_entanglement)

################################################################################
