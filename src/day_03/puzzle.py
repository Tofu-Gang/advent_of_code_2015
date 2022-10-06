__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

The next year, to speed up the process, Santa creates a robot version of 
himself, Robo-Santa, to deliver presents with him.
"""

from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_03/input.txt"
DIRECTION_NORTH = "^"
DIRECTION_SOUTH = "v"
DIRECTION_WEST = "<"
DIRECTION_EAST = ">"
KEY_COORD_X = "X"
KEY_COORD_Y = "Y"

# how coordinates change according to the direction
DIRECTIONS = {
    DIRECTION_NORTH: {
        KEY_COORD_X: lambda x: x,
        KEY_COORD_Y: lambda y: y - 1
    },
    DIRECTION_SOUTH: {
        KEY_COORD_X: lambda x: x,
        KEY_COORD_Y: lambda y: y + 1
    },
    DIRECTION_WEST: {
        KEY_COORD_X: lambda x: x - 1,
        KEY_COORD_Y: lambda y: y
    },
    DIRECTION_EAST: {
        KEY_COORD_X: lambda x: x + 1,
        KEY_COORD_Y: lambda y: y
    }
}


################################################################################

def puzzle_01() -> None:
    """
    Santa begins by delivering a present to the house at his starting location,
    and then an elf at the North Pole calls him via radio and tells him where to
    move next. Moves are always exactly one house to the north (^), south (v),
    east (>), or west (<). After each move, he delivers another present to the
    house at his new location.

    However, the elf back at the North Pole has had a little too much eggnog,
    and so his directions are a little off, and Santa ends up visiting some
    houses more than once. How many houses receive at least one present?

    :return: None; Answer should be 2081.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        directions = f.read().strip()
        houses = [(0, 0)]

        for direction in directions:
            # look at the previously visited house;
            # change the coordinates according to the direction;
            # append the visited house
            houses.append((
                DIRECTIONS[direction][KEY_COORD_X](houses[-1][0]),
                DIRECTIONS[direction][KEY_COORD_Y](houses[-1][1])))

        # eliminate duplicities by using set
        print_puzzle_solution(len(set(houses)))

################################################################################


def puzzle_02() -> None:
    """
    Santa and Robo-Santa start at the same location (delivering two presents to
    the same starting house), then take turns moving based on instructions from
    the elf, who is eggnoggedly reading from the same script as the previous
    year.

    This year, how many houses receive at least one present?

    :return: None; Answer should be 2341.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        directions = f.read()
        # one starting house for the human Santa and the other for the
        # Robo-Santa
        houses = [(0, 0), (0, 0)]

        for direction in directions:
            # since human Santa and Robo-Santa are taking turns, the previous
            # visited house for each Santa is now second to last

            # look at the previously visited house;
            # change the coordinates according to the direction;
            # append the visited house
            houses.append((
                DIRECTIONS[direction][KEY_COORD_X](houses[-2][0]),
                DIRECTIONS[direction][KEY_COORD_Y](houses[-2][1])))

        # eliminate duplicities by using set
        print_puzzle_solution(len(set(houses)))

################################################################################
