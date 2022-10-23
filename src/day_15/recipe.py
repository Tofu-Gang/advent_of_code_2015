__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from itertools import product
from re import compile
from math import prod
from typing import Dict, Tuple


################################################################################

class Recipe(object):
    INPUT_FILE_PATH = "src/day_15/input.txt"
    CAPACITY_KEY = "capacity"
    DURABILITY_KEY = "durability"
    FLAVOR_KEY = "flavor"
    TEXTURE_KEY = "texture"
    CALORIES_KEY = "calories"
    PROPERTY_KEYS = (CAPACITY_KEY,
                     DURABILITY_KEY,
                     FLAVOR_KEY,
                     TEXTURE_KEY,
                     CALORIES_KEY)
    CALORIES = 500
    TEASPOONS = 100

################################################################################

    def __init__(self):
        """
        Initialize dict of ingredients from the input file.
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._ingredients = {
                compile(r"(.+):").findall(line)[0]: {
                    key: self._get_property(key, line)
                    for key in self.PROPERTY_KEYS
                }
                for line in f.readlines()
            }

################################################################################

    @staticmethod
    def _get_property(name: str, line: str) -> int:
        """
        :param name: property name in the line of ingredient
        :param line: line of ingredient from the input file
        :return: ingredient property value
        """

        return int(compile(r"{} (-*\d+)".format(name)).findall(line)[0])

################################################################################

    def score(self, teaspoons: Dict[str, int]):
        """
        :param teaspoons: dict in format ingredient name: number of teaspoons
        :return: recipe score
        """

        # self.PROPERTY_KEYS is used without CALORIES property
        return prod(max(sum(self._ingredients[name][key] * teaspoons[name]
                            for name in self.names), 0)
                    for key in self.PROPERTY_KEYS[:-1])

################################################################################

    def is_500_calories(self, teaspoons: Dict[str, int]):
        """
        :param teaspoons: dict in format ingredient name: number of teaspoons
        :return: True if the recipe is exactly 500 calories, False otherwise
        """

        return sum(
            teaspoons[name] * self._ingredients[name][self.CALORIES_KEY]
            for name in self.names) == self.CALORIES

################################################################################

    @property
    def names(self) -> Tuple[str, ...]:
        """
        :return: list of ingredients names
        """

        return tuple(self._ingredients.keys())

################################################################################

    @property
    def teaspoons(self):
        """
        Generator function that provides all possible combinations of number of
        teaspoons of all possible ingredients.

        :return: dict in format ingredient name: number of teaspoons
        """

        for values in product(range(self.TEASPOONS), repeat=len(self.names)):
            if sum(values) == self.TEASPOONS:
                yield {
                    self.names[i]: values[i] for i in range(len(self.names))
                }

################################################################################
