"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.
"""

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

    i = len(password) - 1
    while password[i] == "z":
        i -= 1

    incremented = ord(password[i]) + 1
    password = password[:i] + chr(incremented) + password[i + 1:]
    i += 1

    while i < len(password):
        password = password[:i] + "a" + password[i + 1:]
        i += 1

    return password

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
    condition2 = "i" not in password \
                 and "o" not in password \
                 and "l" not in password
    # contain at least two different, non-overlapping pairs of letters
    condition3 = len(set([password[i]
                          for i in range(len(password) - 1)
                          if password[i] == password[i + 1]])) >= 2
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

    with open("src/day_11/input.txt", "r") as f:
        password = f.read()

        while not _is_password_valid(password):
            password = _increment_password(password)

        print(password)

################################################################################

def puzzle_02() -> None:
    """
    Santa's password expired again. What's the next one?

    :return: None; Answer should be vzcaabcc.
    """

    with open("src/day_11/input.txt", "r") as f:
        password = f.read()

        while not _is_password_valid(password):
            password = _increment_password(password)
        password = _increment_password(password)
        while not _is_password_valid(password):
            password = _increment_password(password)

        print(password)

################################################################################