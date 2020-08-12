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
    While playing with all the containers in the kitchen, another load of eggnog
    arrives! The shipping and receiving department is requesting as many
    containers as you can spare.

    Find the minimum number of containers that can exactly fit all 150 liters of
    eggnog. How many different ways can you fill that number of containers and
    still hold exactly 150 litres?

    :return: None; Answer should be 18.
    """

    with open("src/day_17/input.txt", "r") as f:
        containers = tuple([int(line.strip()) for line in f.readlines()])

        for i in range(len(containers)):
            containers_combinations = \
                [combination
                 for combination in combinations(containers, i)
                 if sum(combination) == EGGNOG_LITRES]
            if len(containers_combinations) > 0:
                print(len(containers_combinations))
                break

################################################################################
