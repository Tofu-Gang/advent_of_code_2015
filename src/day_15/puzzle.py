from typing import Tuple
from sys import maxsize
from src.day_15.ingredient import Ingredient

"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe.
All you have to do is find the right balance of ingredients.
"""

TEASPOONS_SUM = 100
CALORIES = 500

################################################################################

def _load_ingredients_stats() -> Tuple[Ingredient]:
    """

    :return:
    """

    with open("src/day_15/input.txt", "r") as f:
        return tuple([Ingredient(line) for line in f.readlines()])

################################################################################

def _recipe_score(ingredients: Tuple[Ingredient],
                  teaspoons: Tuple[int, int, int, int]) -> int:
    """
    Counts the recipe score.

    :param ingredients: tuple of all ingredients
    :param teaspoons: tuple of teaspoon amounts of all ingredients
    :return: the recipe score
    """

    capacity_score = max(sum(ingredients[i].capacity * teaspoons[i]
                             for i in range(len(ingredients))), 0)
    durability_score = max(sum(ingredients[i].durability * teaspoons[i]
                               for i in range(len(ingredients))), 0)
    flavor_score = max(sum(ingredients[i].flavor * teaspoons[i]
                           for i in range(len(ingredients))), 0)
    texture_score = max(sum(ingredients[i].texture * teaspoons[i]
                            for i in range(len(ingredients))), 0)
    return capacity_score * durability_score * flavor_score * texture_score

################################################################################

def _is_recipe_500_calories(ingredients: Tuple[Ingredient],
                            teaspoons: Tuple[int, int, int, int]) -> bool:
    """
    Decides if the recipe is exactly 500 calories.

    :param ingredients: tuple of all ingredients
    :param teaspoons: tuple of teaspoon amounts of all ingredients
    :return: True if the recipe is exactly 500 calories, False otherwise
    """

    return sum([teaspoons[i] * ingredients[i].calories
                for i in range(len(ingredients))]) == CALORIES

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

    ingredients = _load_ingredients_stats()
    max_score = -maxsize - 1

    for i in range(TEASPOONS_SUM):
        for j in range(TEASPOONS_SUM - i):
            for k in range(TEASPOONS_SUM - sum((i, j))):
                l = TEASPOONS_SUM - sum((i, j, k))
                teaspoons = (i, j, k, l)
                max_score = max(_recipe_score(ingredients, teaspoons),
                                max_score)

    print(max_score)

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

    ingredients = _load_ingredients_stats()
    max_score = -maxsize - 1

    for i in range(TEASPOONS_SUM):
        for j in range(TEASPOONS_SUM - i):
            for k in range(TEASPOONS_SUM - sum((i, j))):
                l = TEASPOONS_SUM - sum((i, j, k))
                teaspoons = (i, j, k, l)
                if _is_recipe_500_calories(ingredients, teaspoons):
                    max_score = max(_recipe_score(ingredients, teaspoons),
                                    max_score)

    print(max_score)

################################################################################
