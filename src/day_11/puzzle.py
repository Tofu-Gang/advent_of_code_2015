__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.
"""

from re import compile
from src.utils.utils import print_puzzle_solution

CURRENT_PASSWORD = "vzbxkghb"


################################################################################

def _increment_password(password: str) -> str:
    """
    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so
    on. Increase the rightmost letter one step; if it was z, it wraps around to
    a, and repeat with the next letter to the left until one doesn't wrap
    around.

    :param password: password to increment
    :return: incremented password
    """

    # get the last index in the password where the character is not "z"
    i = max(i for i in range(len(password)) if password[i] != "z")
    # increment this character
    incremented = ord(password[i]) + 1
    # the password stays the same up to the index i, which is replaced by the
    # incremented character; the rest of the password is "z" so it is replaced
    # by "a"
    return password[:i] + chr(incremented) + "a" * (len(password) - i - 1)


################################################################################

def _is_password_valid(password: str) -> bool:
    """
    Unfortunately for Santa, a new Security-Elf recently started, and he has
    imposed some additional password requirements:

    -Passwords must include one increasing straight of at least three letters,
     like abc, bcd, cde, and so on, up to xyz.
     They cannot skip letters; abd doesn't count.
    -Passwords may not contain the letters i, o, or l, as these letters can be
     mistaken for other characters and are therefore confusing.
    -Passwords must contain at least two different, non-overlapping pairs of
     letters, like aa, bb, or zz.

    :param password: password to check for validity
    :return: True if the password is valid, False otherwise
    """

    # include one increasing straight of at least three letters
    condition1 = any([ord(password[i + 2]) - ord(password[i + 1]) == 1
                      and ord(password[i + 1]) - ord(password[i]) == 1
                      for i in range(len(password) - 2)])

    # do not include the letters i, o, or l
    condition2 = all(forbidden not in password for forbidden in "iol")

    # contain at least two different, non-overlapping pairs of letters
    pattern = compile(r"(.)\1*")
    groups = tuple(filter(
        lambda match: len(match) >= 2,
        (match.group() for match in pattern.finditer(password))))
    condition3 = len(groups) >= 2 or any(len(group) >= 4 for group in groups)

    return condition1 and condition2 and condition3


################################################################################

def puzzle_01() -> None:
    """
    To help Santa remember his new password after the old one expires, he has
    devised a method of coming up with a password based on the previous one.
    Corporate policy dictates that passwords must be exactly eight lowercase
    letters (for security reasons), so he finds his new password by incrementing
    his old password string repeatedly until it is valid.

    Given Santa's current password (the puzzle input), what should his next
    password be?

    :return: None; Answer should be vzbxxyzz.
    """

    password = CURRENT_PASSWORD

    while not _is_password_valid(password):
        password = _increment_password(password)

    print_puzzle_solution(password)


################################################################################

def puzzle_02() -> None:
    """
    Santa's password expired again. What's the next one?

    :return: None; Answer should be vzcaabcc.
    """

    password = CURRENT_PASSWORD

    while not _is_password_valid(password):
        password = _increment_password(password)
    password = _increment_password(password)
    while not _is_password_valid(password):
        password = _increment_password(password)

    print_puzzle_solution(password)

################################################################################
