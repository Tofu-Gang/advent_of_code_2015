from itertools import combinations

"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all
into your refrigerator, you'll need to move it into smaller containers. You take
an inventory of the capacities of the available containers.
"""

EGGNOG_LITRES = 150

################################################################################

def puzzle_01() -> None:
    """
    Filling all containers entirely, how many different combinations of containers
    can exactly fit all 150 liters of eggnog?

    :return: None; Answer should be 1304.
    """

    with open("src/day_17/input.txt", "r") as f:
        containers = tuple([int(line.strip()) for line in f.readlines()])
        print(len([combination
                   for i in range(len(containers))
                   for combination in combinations(containers, i)
                   if sum(combination) == EGGNOG_LITRES]))

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################
