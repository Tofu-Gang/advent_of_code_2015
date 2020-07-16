from typing import List, Tuple

"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
"""

################################################################################

def _make_a_houses_run(
        directions: str,
        houses: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Uses the directions string to make a run around houses, delivering a present
    to each visited one. Visited houses are stored and returned for later use.

    :param directions: input of the puzzle; directions in which the houses are
    visited
    :param houses: list of houses (their position in the grid)
    :return: visited houses; multiple visits not stored
    """

    # position of the last visited house; when a house is revisited it is not
    # stored again, so in this case we need to have this information stored in
    # these variables; start in the first house (x=0, y=0)
    last_x = 0
    last_y = 0

    for direction in directions:
        # visit the house in the specified direction
        if direction == "^":
            new_x = last_x
            new_y = last_y - 1
        elif direction == ">":
            new_x = last_x + 1
            new_y = last_y
        elif direction == "v":
            new_x = last_x
            new_y = last_y + 1
        elif direction == "<":
            new_x = last_x - 1
            new_y = last_y
        else:
            new_x = None
            new_y = None

        # A new visited house gets present!
        new_house = (new_x, new_y)
        if new_house not in houses:
            # this house hasn't yet been visited, store it
            houses.append(new_house)

        # save the position of the last visited house regardless if it was
        # already visited
        last_x = new_x
        last_y = new_y

    return houses

################################################################################

def puzzle_01() -> None:
    """
    Santa is delivering presents to an infinite two-dimensional grid of houses.

    He begins by delivering a present to the house at his starting location, and
    then an elf at the North Pole calls him via radio and tells him where to
    move next. Moves are always exactly one house to the north (^), south (v),
    east (>), or west (<). After each move, he delivers another present to the
    house at his new location.

    However, the elf back at the north pole has had a little too much eggnog,
    and so his directions are a little off, and Santa ends up visiting some
    houses more than once. How many houses receive at least one present?

    :return: None; Answer should be 2081.
    """

    with open("src/day_03/input.txt", "r") as f:
        directions = f.read()
        houses = [(0, 0)]
        houses = _make_a_houses_run(directions, houses)
        print(len(houses))

################################################################################

def puzzle_02() -> None:
    """
    The next year, to speed up the process, Santa creates a robot version of
    himself, Robo-Santa, to deliver presents with him.

    Santa and Robo-Santa start at the same location (delivering two presents to
    the same starting house), then take turns moving based on instructions from
    the elf, who is eggnoggedly reading from the same script as the previous
    year.

    This year, how many houses receive at least one present?

    :return: None; Answer should be 2341.
    """

    with open("src/day_03/input.txt", "r") as f:
        directions = f.read()
        human_directions = directions[0::2]
        robo_directions = directions[1::2]

        houses = [(0, 0)]
        houses = _make_a_houses_run(human_directions, houses)
        houses = _make_a_houses_run(robo_directions, houses)
        print(len(houses))

################################################################################