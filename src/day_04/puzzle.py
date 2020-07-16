from hashlib import md5

"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as 
gifts for all the economically forward-thinking little girls and boys.
"""

################################################################################

def _find_the_hash(prefix: str) -> int:
    """
    Finds the lowest positive number that, combined with the puzzle input,
    produces a hash that starts with the given prefix.

    :param prefix: requested prefix which the result hash should start with
    :return: puzzle solution
    """

    with open("src/day_04/input.txt", "r") as f:
        code = f.read()
        i = 0

        while True:
            hashed = md5(bytes(code + str(i), encoding='utf-8')).hexdigest()
            if hashed.startswith(prefix):
                return i
            else:
                i += 1

################################################################################

def puzzle_01() -> None:
    """
    To do the mining, Santa needs to find MD5 hashes which, in hexadecimal,
    start with at least five zeroes. The input to the MD5 hash is some secret
    key (the puzzle input) followed by a number in decimal. To mine AdventCoins,
    you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3,
    ...) that produces such a hash.

    :return: None; Answer should be 282749.
    """

    print(_find_the_hash("00000"))

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################