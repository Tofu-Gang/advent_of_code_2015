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

    with open("src/day_02/input.txt", "r") as f:
        lines = f.readlines()
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

def puzzle_02() -> None:
    """
    The elves are also running low on ribbon. Ribbon is all the same width, so
    they only have to worry about the length they need to order, which they
    would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its
    sides, or the smallest perimeter of any one face. Each present also requires
    a bow made out of ribbon as well; the feet of ribbon required for the
    perfect bow is equal to the cubic feet of volume of the present. Don't ask
    how they tie the bow, though; they'll never tell.

    :return: None; Answer should be 3842356.
    """

    with open("src/day_02/input.txt", "r") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            stripped = line.strip()
            dimensions = stripped.split("x")
            l = int(dimensions[0])
            w = int(dimensions[1])
            h = int(dimensions[2])

            dimensions = [l, w, h]
            min1 = min(dimensions)
            dimensions.remove(min1)
            min2 = min(dimensions)

            total += 2*min1 + 2*min2
            total += l*w*h

    print(total)

################################################################################