"""
--- Day 2: I Was Told There Would Be No Math ---
"""

################################################################################

def puzzle_01() -> None:
    """
    The elves are running low on wrapping paper, and so they need to submit an
    order for more. They have a list of the dimensions (length l, width w, and
    height h) of each present, and only want to order exactly as much as they
    need.

    Fortunately, every present is a box (a perfect right rectangular prism),
    which makes calculating the required wrapping paper for each gift a little
    easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    The elves also need a little extra paper for each present: the area of the
    smallest side.

    All numbers in the elves' list are in feet. How many total square feet of
    wrapping paper should they order?

    :return: None; Answer should be 1606483.
    """

    with open("src/day_02/input.txt", "r") as input:
        lines = input.readlines()
        total = 0
        for line in lines:
            stripped = line.strip()
            dimensions = stripped.split("x")
            l = int(dimensions[0])
            w = int(dimensions[1])
            h = int(dimensions[2])

            box_surface = 2*l*w + 2*w*h + 2*h*l
            extra = min((l*w, w*h, h*l))

            total += box_surface
            total += extra

    print(total)

################################################################################
