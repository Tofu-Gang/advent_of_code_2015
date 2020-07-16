from itertools import chain

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
# breaks if initialized like LIGHTS = [[LIGHT_OFF] * SIZE] * SIZE
# probably shallow copies of rows
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
            x_from = int(corner_from.split(DIMENSIONS_DENOMINATOR)[0])
            y_from = int(corner_from.split(DIMENSIONS_DENOMINATOR)[1])
            x_to = int(corner_to.split(DIMENSIONS_DENOMINATOR)[0])
            y_to = int(corner_to.split(DIMENSIONS_DENOMINATOR)[1])

            for y in range(y_from, y_to + 1):
                row = LIGHTS[y]
                x_range = x_to - x_from + 1

                if instruction.startswith(TURN_ON):
                    row[x_from: x_to + 1] = [LIGHT_ON] * x_range
                elif instruction.startswith(TURN_OFF):
                    row[x_from: x_to + 1] = [LIGHT_OFF] * x_range
                elif instruction.startswith(TOGGLE):
                    row = row[:x_from] \
                          + list([not row[x]
                                  for x in range(x_from, x_to + 1)]) \
                          + row[x_to + 1:]

                LIGHTS[y] = row

        print(sum([LIGHTS[row].count(LIGHT_ON) for row in range(SIZE)]))

################################################################################

def puzzle_02() -> None:
    """
    You just finish implementing your winning light pattern when you realize you
    mistranslated Santa's message from Ancient Nordic Elvish.

    The light grid you bought actually has individual brightness controls; each
    light can have a brightness of zero or more. The lights all start at zero.

    The phrase turn on actually means that you should increase the brightness of
    those lights by 1.

    The phrase turn off actually means that you should decrease the brightness
    of those lights by 1, to a minimum of zero.

    The phrase toggle actually means that you should increase the brightness of
    those lights by 2.

    What is the total brightness of all lights combined after following Santa's
    instructions?

    :return: None; Answer should be 14687245.
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
            x_from = int(corner_from.split(DIMENSIONS_DENOMINATOR)[0])
            y_from = int(corner_from.split(DIMENSIONS_DENOMINATOR)[1])
            x_to = int(corner_to.split(DIMENSIONS_DENOMINATOR)[0])
            y_to = int(corner_to.split(DIMENSIONS_DENOMINATOR)[1])

            for y in range(y_from, y_to + 1):
                row = LIGHTS[y]

                if instruction.startswith(TURN_ON):
                    row = row[:x_from] \
                          + list([row[x] + 1
                                  for x in range(x_from, x_to + 1)]) \
                          + row[x_to + 1:]
                elif instruction.startswith(TURN_OFF):
                    row = row[:x_from] \
                          + list([max(row[x] - 1, 0)
                                  for x in range(x_from, x_to + 1)]) \
                          + row[x_to + 1:]
                elif instruction.startswith(TOGGLE):
                    row = row[:x_from] \
                          + list([row[x] + 2
                                  for x in range(x_from, x_to + 1)]) \
                          + row[x_to + 1:]

                LIGHTS[y] = row

        print(sum(list(chain.from_iterable(LIGHTS))))

################################################################################