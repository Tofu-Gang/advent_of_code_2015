__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as 
gifts for all the economically forward-thinking little girls and boys.
"""

from hashlib import md5
from itertools import count
from src.utils.utils import print_puzzle_solution

CODE = "yzbqklnj"
PREFIX_1 = "00000"
PREFIX_2 = "000000"

################################################################################

def _find_the_hash(prefix: str) -> int:
    """
    Finds the lowest positive number that, combined with the puzzle input,
    produces a hash that starts with the given prefix.

    :param prefix: requested prefix which the result hash should start with
    :return: puzzle solution
    """

    for i in count(start=0, step=1):
        if md5(bytes(CODE + str(i), encoding='utf-8')).hexdigest().startswith(prefix):
            return i
        else:
            i += 1


################################################################################

def puzzle_01() -> None:
    """
    To do the mining, Santa needs to find MD5 hashes which, in hexadecimal,
    start with at least five zeroes. The input to the MD5 hash is some secret
    key (the puzzle input) followed by a number in decimal. To mine AdventCoins,
    you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3,
    ...) that produces such a hash.

    :return: None; Answer should be 282749.
    """

    print_puzzle_solution(_find_the_hash(PREFIX_1))


################################################################################

def puzzle_02() -> None:
    """
    Now find one that starts with six zeroes.

    :return: None; Answer should be 9962624.
    """

    print_puzzle_solution(_find_the_hash(PREFIX_2))

################################################################################
