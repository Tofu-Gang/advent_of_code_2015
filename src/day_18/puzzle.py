from typing import List

"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at
most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal
lighting configuration. With so few lights, he says, you'll have to resort to
animation.
"""

LIGHT_ON = "#"
LIGHT_OFF = "."
STEPS = 100

################################################################################

def _load_grid(lines: List[str]) -> List[List[bool]]:
    """
    Loads the initial grid of lights.

    :param lines: the initial grid of lights
    :return: grid of lights where bool True is light turned on and bool False
    light turned off
    """

    return [[light == LIGHT_ON for light in line] for line in lines]

################################################################################

def _number_of_lit_neighbours(grid: List[List[bool]],
                              row: int,
                              column: int) -> int:
    """
    Gets the current states of the eight lights adjacent to it (including
    diagonals). Lights on the edge of the grid might have fewer than eight
    neighbors; the missing ones always count as "off".

    :param grid: grid of lights
    :param row: number of row that specifies the one light which neighbours
    state we need to get
    :param column: number of column that specifies the one light which
    neighbours state we need to get
    :return: number of lit neighbour lights of the specified light (by row,
    column arguments)
    """

    lit_neighbours = 0

    if row > 0 and column > 0 and grid[row - 1][column - 1] == True:
        lit_neighbours += 1
    if row > 0 and grid[row - 1][column] == True:
        lit_neighbours += 1
    if row > 0 and column < len(grid) - 1 and grid[row - 1][column + 1] == True:
        lit_neighbours += 1
    if column > 0 and grid[row][column - 1] == True:
        lit_neighbours += 1
    if column < len(grid) - 1 and grid[row][column + 1] == True:
        lit_neighbours += 1
    if row < len(grid) - 1 and column > 0 and grid[row + 1][column - 1] == True:
        lit_neighbours += 1
    if row < len(grid) - 1 and grid[row + 1][column] == True:
        lit_neighbours += 1
    if row < len(grid) - 1 and column < len(grid) - 1 and grid[row + 1][column + 1] == True:
        lit_neighbours += 1

    return lit_neighbours

################################################################################

def _advance_grid(old_grid: List[List[bool]]) -> List[List[bool]]:
    """
    Animates the grid in steps, where each step decides the next configuration
    based on the current one. Each light's next state (either on or off) depends
    on its current state and the current states of the eight lights adjacent to
    it.

    The state a light should have next is based on its current state (on or off)
    plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off
    otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off
    otherwise.
    All of the lights update simultaneously; they all consider the same current
    state before moving to the next.

    :param old_grid: grid of lights in the current state
    :return: advanced grid of lights by one step
    """

    return [
        [(old_grid[i][j] == True
          and _number_of_lit_neighbours(old_grid, i, j) == 2
          or _number_of_lit_neighbours(old_grid, i, j) == 3)
         or (old_grid[i][j] == False
             and _number_of_lit_neighbours(old_grid, i, j) == 3)
         for j in range(len(old_grid[i]))]
        for i in range(len(old_grid))
    ]

################################################################################

def _lit_lights(grid: List[List[bool]]) -> int:
    """
    Counts the number of lights in the grid which are turned on.

    :param grid: grid of lights
    :return: number of lights in the input grid which are turned on
    """

    return sum([1
                for i in range(len(grid))
                for j in range(len(grid[i]))
                if grid[i][j] == True])

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

    with open("src/day_18/input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        grid = _load_grid(lines)

        for _ in range(STEPS):
            grid = _advance_grid(grid)

        print(_lit_lights(grid))

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################
