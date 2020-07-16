"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or
nice.
"""

VOWELS = "aeiou"
FORBIDDEN = ("ab", "cd", "pq", "xy")

################################################################################

def _is_string_nice(input_string: str) -> bool:
    """
    A nice string is one with all of the following properties:
    -It contains at least three vowels (aeiou only),
     like aei, xazegov, or aeiouaeiouaeiou.
    -It contains at least one letter that appears twice in a row,
     like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    -It does not contain the strings ab, cd, pq, or xy, even if they are part of
     one of the other requirements.

    :param input_string: the naughty or nice input string
    :return: True if the input string is nice, False if it is naughty
    """

    vowels_count = sum([input_string.count(vowel) for vowel in VOWELS])
    condition_1 = vowels_count >= 3
    condition_2 = any([input_string[i] == input_string[i + 1]
                       for i in range(len(input_string) - 1)])
    condition_3 = all([forbidden not in input_string
                       for forbidden in FORBIDDEN])
    return condition_3 and condition_1 and condition_2

################################################################################

def puzzle_01() -> None:
    """
    How many strings in the input are nice?

    :return: None; Answer should be 258.
    """

    with open("src/day_05/input.txt", "r") as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if _is_string_nice(line.strip()):
                count += 1

    print(count)

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################