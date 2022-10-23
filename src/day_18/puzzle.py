__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at
most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal
lighting configuration. With so few lights, he says, you'll have to resort to
animation.
"""

from src.utils.utils import print_puzzle_solution

STEPS = 100


################################################################################

class Lights(object):
    LIGHT_ON = "#"
    INPUT_FILE_PATH = "src/day_18/input.txt"

################################################################################

    def __init__(self, lights_are_stuck=False):
        """
        Creates a grid of lights from the input file. Stores the information
        whether the four corner lights are stuck on or not.
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._lights = [[light == self.LIGHT_ON
                             for light in line.strip()]
                            for line in f.readlines()]
            self._lights_are_stuck = lights_are_stuck

################################################################################

    @property
    def lit_lights(self) -> int:
        """
        :return: number of lights in the input grid which are turned on
        """

        return sum(line.count(True) for line in self._lights)

################################################################################

    def advance_grid(self) -> None:
        """
        Animates the grid in steps, where each step decides the next
        configuration based on the current one. Each light's next state (either
        on or off) depends on its current state and the current states of the
        eight lights adjacent to it.

        The state a light should have next is based on its current state (on or
        off) plus the number of neighbors that are on:

        A light which is on stays on when 2 or 3 neighbors are on, and turns off
        otherwise.
        A light which is off turns on if exactly 3 neighbors are on, and stays
        off otherwise.
        All of the lights update simultaneously; they all consider the same
        current state before moving to the next.
        """

        if self._lights_are_stuck:
            self._lights_stuck()

        self._lights = [[(self._lights[i][j] is True
                          and self._lit_neighbours(i, j) == 2
                          or self._lit_neighbours(i, j) == 3)
                         or (self._lights[i][j] is False
                             and self._lit_neighbours(i, j) == 3)
                         for j in range(len(self._lights[i]))]
                        for i in range(len(self._lights))]

        if self._lights_are_stuck:
            self._lights_stuck()

################################################################################

    def _lit_neighbours(self, row: int, column: int) -> int:
        """
        Gets the current states of the eight lights adjacent to it (including
        diagonals). Lights on the edge of the grid might have fewer than eight
        neighbors; the missing ones always count as "off".

        :param row: number of row that specifies the one light which neighbours
        state we need to get
        :param column: number of column that specifies the one light which
        neighbours state we need to get
        :return: number of lit neighbour lights of the specified light (by row,
        column arguments)
        """

        coords = tuple(filter(
            lambda coord: all(0 <= value < len(self._lights)
                              for value in coord),
            ((row - 1, column - 1),
             (row - 1, column),
             (row - 1, column + 1),
             (row, column - 1),
             (row, column + 1),
             (row + 1, column - 1),
             (row + 1, column),
             (row + 1, column + 1))))
        return tuple(self._lights[coord[0]][coord[1]]
                     for coord in coords).count(True)

################################################################################

    def _lights_stuck(self) -> None:
        """
        Four lights, one in each corner of the grid is stuck and cannot be
        turned off.
        """

        self._lights[0][0] = True
        self._lights[0][len(self._lights) - 1] = True
        self._lights[len(self._lights) - 1][0] = True
        self._lights[len(self._lights) - 1][len(self._lights) - 1] = True


################################################################################

def puzzle_01() -> None:
    """
    Start by setting your lights to the included initial configuration (your
    puzzle input). A # means "on", and a . means "off".

    Then, animate your grid in steps, where each step decides the next
    configuration based on the current one.

    In your grid of 100x100 lights, given your initial configuration, how many
    lights are on after 100 steps?

    :return: None; Answer should be 814.
    """

    lights = Lights()
    for _ in range(STEPS):
        lights.advance_grid()
    print_puzzle_solution(lights.lit_lights)


################################################################################

def puzzle_02() -> None:
    """
    You flip the instructions over; Santa goes on to point out that this is all
    just an implementation of Conway's Game of Life. At least, it was, until you
    notice that something's wrong with the grid of lights you bought: four
    lights, one in each corner, are stuck on and can't be turned off.

    In your grid of 100x100 lights, given your initial configuration, but with
    the four corners always in the on state, how many lights are on after 100
    steps?

    :return: None; Answer should be 924.
    """

    lights = Lights(lights_are_stuck=True)
    for _ in range(STEPS):
        lights.advance_grid()
    print_puzzle_solution(lights.lit_lights)

################################################################################
