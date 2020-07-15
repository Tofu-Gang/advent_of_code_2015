"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
"""

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
        last_x = 0
        last_y = 0

        for direction in directions:
            new_x = last_x
            new_y = last_y

            if direction == "^":
                new_y -= 1
            elif direction == ">":
                new_x += 1
            elif direction == "v":
                new_y += 1
            elif direction == "<":
                new_x -= 1
            else:
                new_x = None
                new_y = None

            new_house = (new_x, new_y)
            if new_house not in houses:
                houses.append(new_house)

            last_x = new_x
            last_y = new_y

        print(len(houses))

################################################################################

def puzzle_02() -> None:
    """
    
    :return: None
    """

    pass

################################################################################