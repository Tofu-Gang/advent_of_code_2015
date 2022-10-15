__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 8: Matchsticks ---

Space on the sleigh is limited this year, and so Santa will be bringing his list
as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special
characters in strings. For example, C, JavaScript, Perl, Python, and even PHP
handle special characters in very similar ways.

However, it is important to realize the difference between the number of
characters in the code representation of the string literal and the number of
characters in the in-memory string itself.
"""

from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_08/input.txt"


################################################################################

def puzzle_01() -> None:
    """
    Santa's list is a file that contains many double-quoted string literals, one
    on each line. The only escape sequences used are \\ (which represents a
    single backslash), \" (which represents a lone double-quote character), and
    \ x plus two hexadecimal characters (which represents a single character
    with that ASCII code).

    Disregarding the whitespace in the file, what is the number of characters of
    code for string literals minus the number of characters in memory for the
    values of the strings in total for the entire file?

    :return: None; Answer should be 1350.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        print_puzzle_solution(sum([len(line.strip()) - len(eval(line.strip()))
                                   for line in lines]))

################################################################################


def puzzle_02() -> None:
    """
    Now, let's go the other way. In addition to finding the number of characters
    of code, you should now encode each code representation as a new string and
    find the number of characters of the new encoded representation, including
    the surrounding double quotes.

    Your task is to find the total number of characters to represent the newly
    encoded strings minus the number of characters of code in each original
    string literal.

    :return: None; Answer should be 2085.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        print_puzzle_solution(sum([2 + line.strip().count('\\')
                                   + line.strip().count('"')
                                   for line in lines]))

################################################################################
