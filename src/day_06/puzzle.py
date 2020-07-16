"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.
"""

TURN_ON = "turn on"
TURN_OFF = "turn off"
TOGGLE = "toggle"
CORNERS_DENOMINATOR = "through"
DIMENSIONS_DENOMINATOR = ","
SIZE = 1000
LIGHT_ON = True
LIGHT_OFF = False
LIGHTS = []
for _ in range(SIZE):
    row = []
    for __ in range(SIZE):
        row.append(LIGHT_OFF)
    LIGHTS.append(row)

################################################################################

def puzzle_01() -> None:
    """
    Lights in your grid are numbered from 0 to 999 in each direction; the lights
    at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions
    include whether to turn on, turn off, or toggle various inclusive ranges
    given as coordinate pairs. Each coordinate pair represents opposite corners
    of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore
    refers to 9 lights in a 3x3 square. The lights all start turned off.

    To defeat your neighbors this year, all you have to do is set up your lights
    by doing the instructions Santa sent you in order.

    After following the instructions, how many lights are lit?

    :return: None; Answer should be 543903.
    """

    with open("src/day_06/input.txt", "r") as f:
        instructions = f.readlines()

        for instruction in instructions:
            if instruction.startswith(TURN_ON):
                rest = instruction.split(TURN_ON)[1]
            elif instruction.startswith(TURN_OFF):
                rest = instruction.split(TURN_OFF)[1]
            elif instruction.startswith(TOGGLE):
                rest = instruction.split(TOGGLE)[1]
            else:
                rest = None

            corner_from = rest.split(CORNERS_DENOMINATOR)[0]
            corner_to = rest.split(CORNERS_DENOMINATOR)[1]
            corner_from_row = int(corner_from.split(DIMENSIONS_DENOMINATOR)[1])
            corner_from_column = int(corner_from.split(DIMENSIONS_DENOMINATOR)[0])
            corner_to_column = int(corner_to.split(DIMENSIONS_DENOMINATOR)[0])
            corner_to_row = int(corner_to.split(DIMENSIONS_DENOMINATOR)[1])

            for row_number in range(corner_from_row, corner_to_row + 1):
                row = LIGHTS[row_number]
                columns_range = corner_to_column - corner_from_column + 1

                if instruction.startswith(TURN_ON):
                    row[corner_from_column: corner_to_column + 1] \
                        = [LIGHT_ON] * columns_range
                elif instruction.startswith(TURN_OFF):
                    row[corner_from_column: corner_to_column + 1] \
                        = [LIGHT_OFF] * columns_range
                elif instruction.startswith(TOGGLE):
                    for column_number in range(corner_from_column, corner_to_column + 1):
                        row[column_number] = not row[column_number]

                LIGHTS[row_number] = row

        print(sum([LIGHTS[row].count(LIGHT_ON) for row in range(SIZE)]))

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################