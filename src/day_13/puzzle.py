__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not
everyone gets along! This year, you resolve, will be different. You're going to
find the optimal seating arrangement and avoid all those awkward conversations.
"""

from re import compile
from typing import Tuple
from itertools import permutations
from src.utils.utils import print_puzzle_solution


################################################################################

class Happiness(object):
    GAIN = "gain"
    LOSE = "lose"
    HAPPINESS_FUNCTIONS = {
        GAIN: lambda value: value,
        LOSE: lambda value: -value
    }
    INPUT_FILE_PATH = "src/day_13/input.txt"
    MYSELF = "myself"

################################################################################

    def __init__(self):
        """
        Initializes a dictionary with info about everyone seated at the table
        with their happiness values changes according to their neighbour.
        """

        self._happiness_rules = {}

        with open(self.INPUT_FILE_PATH, "r") as f:
            lines = f.readlines()

            for line in lines:
                person_pattern = compile(r"(\D+) would")
                neighbour_pattern = compile(r"by sitting next to (\D+).")
                function_pattern = compile("{}|{}".format(self.GAIN, self.LOSE))
                value_pattern = compile(r"\d+")

                person = person_pattern.findall(line)[0]
                neighbour = neighbour_pattern.findall(line)[0]
                function = function_pattern.findall(line)[0]
                value = int(value_pattern.findall(line)[0])
                happiness = self.HAPPINESS_FUNCTIONS[function](value)

                self._happiness_rules.setdefault(person, {})
                self._happiness_rules[person][neighbour] = happiness

################################################################################

    def get_seating_happiness(self, seating: Tuple[str]) -> int:
        """
        :param seating: a combination of arrangement of people sitting around
        the table
        :return: total happiness of the given seating around the table
        """

        return sum(map(
            lambda i: self._happiness_rules[seating[i]][seating[i - 1]] +
                      self._happiness_rules[seating[i]][seating[i + 1]],
            range(len(seating) - 1)))

################################################################################

    @property
    def family(self) -> Tuple[str, ...]:
        """
        :return: tuple of the whole family
        """

        return tuple(self._happiness_rules.keys())

################################################################################

    def add_myself(self) -> None:
        """
        Add myself to the happiness rules. No happiness value is ever changed,
        regardless of my neighbours.
        """

        self._happiness_rules[self.MYSELF] = {}
        [self._happiness_rules[person].update({self.MYSELF: 0})
         for person in self.family]
        [self._happiness_rules[self.MYSELF].update({person: 0})
         for person in self.family]


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

    happiness = Happiness()
    print_puzzle_solution(max(map(
        lambda seating: happiness.get_seating_happiness(seating),
        permutations(happiness.family))))


################################################################################

def puzzle_02() -> None:
    """
    In all the commotion, you realize that you forgot to seat yourself. At this
    point, you're pretty apathetic toward the whole thing, and your happiness
    wouldn't really go up or down regardless of who you sit next to. You assume
    everyone else would be just as ambivalent about sitting next to you, too.

    So, add yourself to the list, and give all happiness relationships that
    involve you a score of 0.

    What is the total change in happiness for the optimal seating arrangement
    that actually includes yourself?

    :return: None; Answer should be 668.
    """

    happiness = Happiness()
    happiness.add_myself()
    print_puzzle_solution(max(map(
        lambda seating: happiness.get_seating_happiness(seating),
        permutations(happiness.family))))

################################################################################
