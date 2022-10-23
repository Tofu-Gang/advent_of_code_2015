__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank
you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".
"""

from re import compile
from src.utils.utils import print_puzzle_solution

MFCSAM_OUTPUT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
COMPOUNDS = {
    "children": lambda value: MFCSAM_OUTPUT["children"] == value,
    "cats": lambda value: MFCSAM_OUTPUT["cats"] < value,
    "samoyeds": lambda value: MFCSAM_OUTPUT["samoyeds"] == value,
    "pomeranians": lambda value: MFCSAM_OUTPUT["pomeranians"] > value,
    "akitas": lambda value: MFCSAM_OUTPUT["akitas"] == value,
    "vizslas": lambda value: MFCSAM_OUTPUT["vizslas"] == value,
    "goldfish": lambda value: MFCSAM_OUTPUT["goldfish"] > value,
    "trees": lambda value: MFCSAM_OUTPUT["trees"] < value,
    "cars": lambda value: MFCSAM_OUTPUT["cars"] == value,
    "perfumes": lambda value: MFCSAM_OUTPUT["perfumes"] == value
}
INPUT_FILE_PATH = "src/day_16/input.txt"


################################################################################

def get_compound_count(compound: str, line: str) -> int:
    """
    :param compound: compound name
    :param line: one aunt line from the input
    :return: compound count
    """

    return int(compile(r"{}: (\d+)".format(compound)).findall(line)[0])


################################################################################

def puzzle_01() -> None:
    """
    So, to avoid sending the card to the wrong person, you need to figure out
    which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you
    the gift. You open the present and, as luck would have it, good ol' Aunt Sue
    got you a My First Crime Scene Analysis Machine! Just what you wanted. Or
    needed, as the case may be.

    The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a
    few specific compounds in a given sample, as well as how many distinct kinds
    of those compounds there are. According to the instructions, these are what
    the MFCSAM can detect:

    -children, by human DNA age analysis.
    -cats. It doesn't differentiate individual breeds.
    -Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and
     vizslas.
    -goldfish. No other kinds of fish.
    -trees, all in one group.
    -cars, presumably by exhaust or gasoline or something.
    -perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

    In fact, many of your Aunts Sue have many of these. You put the wrapping
    from the gift into the MFCSAM. It beeps inquisitively at you a few times and
    then prints out a message on ticker tape:

    children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1

    You make a list of the things you can remember about each Aunt Sue. Things
    missing from your list aren't zero - you simply don't remember the value.

    What is the number of the Sue that got you the gift?

    :return: None; Answer should be 40.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        hits = tuple(len(tuple(filter(
            lambda compound:
            compound in line
            and MFCSAM_OUTPUT[compound] == get_compound_count(compound, line),
            COMPOUNDS))) for line in lines)
        print_puzzle_solution(hits.index(max(hits)) + 1)


################################################################################

def puzzle_02() -> None:
    """
    As you're about to send the thank you note, something in the MFCSAM's
    instructions catches your eye. Apparently, it has an outdated
    retroencabulator, and so the output from the machine isn't exact values -
    some of them indicate ranges.

    In particular, the cats and trees readings indicates that there are greater
    than that many (due to the unpredictable nuclear decay of cat dander and
    tree pollen), while the pomeranians and goldfish readings indicate that
    there are fewer than that many (due to the modial interaction of
    magnetoreluctance).

    What is the number of the real Aunt Sue?

    :return: None; Answer should be 241.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        hits = tuple(len(tuple(filter(
            lambda compound:
            compound in line
            and COMPOUNDS[compound](get_compound_count(compound, line)),
            COMPOUNDS))) for line in lines)
        print_puzzle_solution(hits.index(max(hits)) + 1)

################################################################################
