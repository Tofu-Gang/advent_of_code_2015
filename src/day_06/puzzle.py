__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you
instructions on how to display the ideal lighting configuration.
"""

from typing import Dict
from itertools import chain
from re import compile, findall
from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_06/input.txt"


################################################################################

class Lights(object):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"
    DIMENSIONS_DENOMINATOR = ","
    SIZE = 1000
    KEY_LIGHT_OFF = "LIGHT_OFF"
    KEY_IS_LIT = "IS_LIT"

    KEY_TOP = "TOP"
    KEY_BOTTOM = "BOTTOM"
    KEY_LEFT = "LEFT"
    KEY_RIGHT = "RIGHT"

    KEY_PUZZLE_1 = "PUZZLE_1"
    KEY_PUZZLE_2 = "PUZZLE_2"

    # initial values for every light (KEY_LIGHT_OFF) and set of functions which
    # are applied to a single light and define instructions turn on, turn off
    # and toggle and a definition of a lit light for both puzzles
    LIGHTS = {
        KEY_PUZZLE_1: {
            KEY_LIGHT_OFF: False,
            TURN_ON: lambda light: True,
            TURN_OFF: lambda light: False,
            TOGGLE: lambda light: not light,
            KEY_IS_LIT: lambda light: light is True
        },
        KEY_PUZZLE_2: {
            KEY_LIGHT_OFF: 0,
            TURN_ON: lambda light: light + 1,
            TURN_OFF: lambda light: light - 1 if light >= 1 else 0,
            TOGGLE: lambda light: light + 2
        }
    }

################################################################################

    def __init__(self, puzzle):
        """
        Initialize the grid of lights. Store the information about which puzzle
        we are solving.
        """

        self._puzzle = puzzle

        # breaks if initialized like LIGHTS = [[LIGHT_OFF] * SIZE] * SIZE
        # probably because of shallow copies of rows
        self._lights = []
        for _ in range(self.SIZE):
            row = []
            for __ in range(self.SIZE):
                row.append(self.LIGHTS[self._puzzle][self.KEY_LIGHT_OFF])
            self._lights.append(row)

################################################################################

    def process_instruction(self, instruction: str) -> None:
        """
        Applies the instruction to the grid of lights.

        :param instruction: one instruction from the input file
        """

        instruction_type = self._get_instruction_type(instruction)
        function = self.LIGHTS[self._puzzle][instruction_type]
        borders = self._get_instruction_borders(instruction)
        top = borders[self.KEY_TOP]
        bottom = borders[self.KEY_BOTTOM]
        left = borders[self.KEY_LEFT]
        right = borders[self.KEY_RIGHT]

        for row_number in range(top, bottom + 1):
            # get the segment of the row which is affected by the instruction
            row_segment = self._lights[row_number][left: right + 1]
            # apply the instruction to the row segment
            row_segment_after = list(map(function, row_segment))
            self._lights[row_number][left: right + 1] = row_segment_after

################################################################################

    @property
    def lit_lights_count(self) -> int:
        """
        :return: number of lit lights in the grid
        """

        return len(tuple(filter(
            self.LIGHTS[self._puzzle][self.KEY_IS_LIT],
            chain.from_iterable(self._lights))))

################################################################################

    @property
    def total_brightness(self) -> int:
        """
        :return: total brightness of lights in the grid
        """

        return sum(chain.from_iterable(self._lights))

################################################################################

    def _get_instruction_type(self, instruction: str) -> str:
        """
        :param instruction: one instruction from the input file
        :return: either "turn on", "turn off" or "toggle"
        """

        return findall(compile("{}|{}|{}".format(
            self.TURN_ON, self.TURN_OFF, self.TOGGLE)), instruction)[0]

################################################################################

    def _get_instruction_borders(self, instruction: str) -> Dict[str, int]:
        """
        :param instruction: one instruction from the input file
        :return: top, bottom, left and right row/column numbers that surround
        the lights from the instruction
        """

        pattern = compile(r"\d+{}\d+".format(self.DIMENSIONS_DENOMINATOR))
        borders = tuple(map(
            lambda corner: [int(value) for value in corner.split(",")],
            findall(pattern, instruction)))
        return {
            self.KEY_TOP: borders[0][1],
            self.KEY_BOTTOM: borders[1][1],
            self.KEY_LEFT: borders[0][0],
            self.KEY_RIGHT: borders[1][0]
        }


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

    with open(INPUT_FILE_PATH, "r") as f:
        instructions = f.readlines()
        lights = Lights(Lights.KEY_PUZZLE_1)

        for instruction in instructions:
            lights.process_instruction(instruction)

        print_puzzle_solution(lights.lit_lights_count)


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

    with open(INPUT_FILE_PATH, "r") as f:
        instructions = f.readlines()
        lights = Lights(Lights.KEY_PUZZLE_2)

        for instruction in instructions:
            lights.process_instruction(instruction)

        print_puzzle_solution(lights.total_brightness)

################################################################################
