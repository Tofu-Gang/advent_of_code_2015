from sys import maxsize

"""
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank
you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".
"""

COMPOUNDS = (
    "children",
    "cats",
    "samoyeds",
    "pomeranians",
    "akitas",
    "vizslas",
    "goldfish",
    "trees",
    "cars",
    "perfumes"
)
MFCSAM_OUTPUT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
COLON = ":"
COMMA = ","
SUE = "Sue"

################################################################################

def puzzle_01() -> None:
    """
    So, to avoid sending the card to the wrong person, you need to figure out
    which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you
    the gift. You open the present and, as luck would have it, good ol' Aunt Sue
    got you a My First Crime Scene Analysis Machine! Just what you wanted. Or
    needed, as the case may be.

    The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a
    few specific compounds in a given sample, as well as how many distinct kinds
    of those compounds there are. According to the instructions, these are what
    the MFCSAM can detect:

    -children, by human DNA age analysis.
    -cats. It doesn't differentiate individual breeds.
    -Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and
     vizslas.
    -goldfish. No other kinds of fish.
    -trees, all in one group.
    -cars, presumably by exhaust or gasoline or something.
    -perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

    In fact, many of your Aunts Sue have many of these. You put the wrapping
    from the gift into the MFCSAM. It beeps inquisitively at you a few times and
    then prints out a message on ticker tape:

    children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1

    You make a list of the things you can remember about each Aunt Sue. Things
    missing from your list aren't zero - you simply don't remember the value.

    What is the number of the Sue that got you the gift?

    :return: None; Answer should be 40.
    """

    with open("src/day_16/input.txt", "r") as f:
        lines = f.readlines()
        max_hits = -maxsize - 1
        sue_number = None

        for line in lines:
            hits = len(
                [compound
                 for compound in COMPOUNDS
                 if compound in line
                 and MFCSAM_OUTPUT[compound]
                 == int(
                    line.strip()
                        .split(compound)[1]
                        .split(COLON)[1]
                        .split(COMMA)[0])])

            if hits > max_hits:
                max_hits = hits
                sue_number = line.strip().split(SUE)[1].split(COLON)[0].strip()

        print(sue_number)

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################
