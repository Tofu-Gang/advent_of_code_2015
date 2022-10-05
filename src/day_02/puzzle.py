__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order 
for more. They have a list of the dimensions (length l, width w, and height h) 
of each present, and only want to order exactly as much as they need.

The elves are also running low on ribbon. Ribbon is all the same width, so they 
only have to worry about the length they need to order, which they would again 
like to be exact.
"""

from numpy import prod
from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_02/input.txt"
DENOMINATOR = "x"


################################################################################

def _get_paper_area(length: int, width: int, height: int) -> int:
    """
    Calculates how many square feet of wrapping paper is needed to wrap a box
    specified by the params.

    :param length: box length
    :param width: box width
    :param height: box height
    :return: wrapping paper area (box surface area plus needed extra)
    """

    box_faces = (length * width, width * height, height * length)
    box_surface = 2 * sum(box_faces)
    extra = min(box_faces)
    return box_surface + extra


################################################################################

def _get_ribbon_length(length: int, width: int, height: int) -> int:
    """
    Calculates how many feet of ribbon is needed to wrap a box specified by the
    params.

    :param length: box length
    :param width: box width
    :param height: box height
    :return: ribbon length (the smallest perimeter of any box side plus some
    extra for the bow)
    """

    box_dimensions = sorted((length, width, height))
    ribbon_box = 2 * box_dimensions[0] + 2 * box_dimensions[1]
    ribbon_bow = prod(box_dimensions)
    return ribbon_box + ribbon_bow


################################################################################

def puzzle_01() -> None:
    """
    Fortunately, every present is a box (a perfect right rectangular prism),
    which makes calculating the required wrapping paper for each gift a little
    easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    The elves also need a little extra paper for each present: the area of the
    smallest side.

    All numbers in the elves' list are in feet. How many total square feet of
    wrapping paper should they order?

    :return: None; Answer should be 1606483.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        box_dimensions = f.readlines()
        total = sum(_get_paper_area(int(line.strip().split(DENOMINATOR)[0]),
                                    int(line.strip().split(DENOMINATOR)[1]),
                                    int(line.strip().split(DENOMINATOR)[2]))
                    for line in box_dimensions)
        print_puzzle_solution(total)


################################################################################

def puzzle_02() -> None:
    """
    The ribbon required to wrap a present is the shortest distance around its
    sides, or the smallest perimeter of any one face. Each present also requires
    a bow made out of ribbon as well; the feet of ribbon required for the
    perfect bow is equal to the cubic feet of volume of the present. Don't ask
    how they tie the bow, though; they'll never tell.

    :return: None; Answer should be 3842356.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        box_dimensions = f.readlines()
        total = sum(_get_ribbon_length(int(line.strip().split(DENOMINATOR)[0]),
                                       int(line.strip().split(DENOMINATOR)[1]),
                                       int(line.strip().split(DENOMINATOR)[2]))
                    for line in box_dimensions)
        print_puzzle_solution(total)

################################################################################
