__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand,
door-to-door.
"""

from itertools import count
from src.utils.utils import print_puzzle_solution

PUZZLE_INPUT = 29000000
# generators can be sped up by skipping houses; checking only every 10th house
# seems to be reasonable enough while speeding up the process enormously
STEP = 10


################################################################################

def house_presents():
    """
    Generator of house numbers and number of presents delivered to that house.
    Rules from puzzle 1 applied.

    :return: house number and number of presents delivered to the house
    """

    for house_number in count(start=0, step=STEP):
        presents = sum(
            elf_number * 10
            for elf_number in range(1, house_number + 1)
            if house_number % elf_number == 0)
        yield house_number, presents


################################################################################

def house_presents_2():
    """
    Generator of house numbers and number of presents delivered to that house.
    Rules from puzzle 2 applied.

    :return: house number and number of presents delivered to the house
    """

    for house_number in count(start=0, step=STEP):
        presents = sum(
            elf_number * 11
            for elf_number in range(1, house_number + 1)
            if house_number % elf_number == 0
            and elf_number * 50 >= house_number)
        yield house_number, presents


################################################################################

def puzzle_01() -> None:
    """
    He sends them down a street with infinite houses numbered sequentially: 1,
    2, 3, 4, 5, and so on.

    Each Elf is assigned a number, too, and delivers presents to houses based on
    that number:

    The first Elf (number 1) delivers presents to every house:
    1, 2, 3, 4, 5, ....
    The second Elf (number 2) delivers presents to every second house:
    2, 4, 6, 8, 10, ....
    Elf number 3 delivers presents to every third house:
    3, 6, 9, 12, 15, ....
    There are infinitely many Elves, numbered starting with 1. Each Elf delivers
    presents equal to ten times his or her number at each house.

    What is the lowest house number of the house to get at least as many
    presents as the number in your puzzle input?

    :return: None; Answer should be 665280.
    """

    house_presents_generator = house_presents()
    while True:
        house_number, presents = next(house_presents_generator)

        if presents >= PUZZLE_INPUT:
            print_puzzle_solution(house_number)
            break


################################################################################

def puzzle_02() -> None:
    """
    The Elves decide they don't want to visit an infinite number of houses.
    Instead, each Elf will stop after delivering presents to 50 houses. To make
    up for it, they decide to deliver presents equal to eleven times their
    number at each house.

    With these changes, what is the new lowest house number of the house to get
    at least as many presents as the number in your puzzle input?

    :return: None; Answer should be 705600.
    """

    house_presents_generator = house_presents_2()
    while True:
        house_number, presents = next(house_presents_generator)

        if presents >= PUZZLE_INPUT:
            print_puzzle_solution(house_number)
            break

################################################################################
