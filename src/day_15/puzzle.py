__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.
"""

from src.day_15.recipe import Recipe
from src.utils.utils import print_puzzle_solution


################################################################################

def puzzle_01() -> None:
    """
    Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a
    list of the remaining ingredients you could use to finish the recipe (the
    puzzle input) and their properties per teaspoon:

    -capacity (how well it helps the cookie absorb milk)
    -durability (how well it keeps the cookie intact when full of milk)
    -flavor (how tasty it makes the cookie)
    -texture (how it improves the feel of the cookie)
    -calories (how many calories it adds to the cookie)

    You can only measure ingredients in whole-teaspoon amounts accurately, and
    you have to be accurate so you can reproduce your results in the future. The
    total score of a cookie can be found by adding up each of the properties
    (negative totals become 0) and then multiplying together everything except
    calories.

    Given the ingredients in your kitchen and their properties, what is the
    total score of the highest-scoring cookie you can make?

    :return: None; Answer should be 222870.
    """

    recipe = Recipe()
    print_puzzle_solution(max(recipe.score(values)
                              for values in recipe.teaspoons))


################################################################################

def puzzle_02() -> None:
    """
    Your cookie recipe becomes wildly popular! Someone asks if you can make
    another recipe that has exactly 500 calories per cookie (so they can use it
    as a meal replacement). Keep the rest of your award-winning process the same
    (100 teaspoons, same ingredients, same scoring system).

    Given the ingredients in your kitchen and their properties, what is the
    total score of the highest-scoring cookie you can make with a calorie total
    of 500?

    :return: None; Answer should be 117936.
    """

    recipe = Recipe()
    print_puzzle_solution(max(recipe.score(values)
                              for values in recipe.teaspoons
                              if recipe.is_500_calories(values)))

################################################################################
