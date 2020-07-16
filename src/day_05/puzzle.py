"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or
nice.
"""

VOWELS = "aeiou"
FORBIDDEN = ("ab", "cd", "pq", "xy")

################################################################################

def _is_string_nice_part1(input_string: str) -> bool:
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

def _is_string_nice_part2(input_string: str) -> bool:
    """
    Now, a nice string is one with all of the following properties:
    -It contains a pair of any two letters that appears at least twice in the
     string without overlapping,
     like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    -It contains at least one letter which repeats with exactly one letter
     between them,
     like xyx, abcdefeghi (efe), or even aaa.

    :param input_string: the naughty or nice input string
    :return: True if the input string is nice, False if it is naughty
    """

    condition_1 = any([
        input_string.count(input_string[i]+input_string[i + 1]) > 1
        and (input_string[i] != input_string[i + 1]
             or input_string[i + 1] != input_string[i + 2])
        for i in range(len(input_string) - 2)])
    condition_2 = any([input_string[i] == input_string[i + 2]
                       for i in range(len(input_string) - 2)])
    return condition_1 and condition_2

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
            if _is_string_nice_part1(line):
                count += 1

    print(count)

################################################################################

def puzzle_02() -> None:
    """
    Realizing the error of his ways, Santa has switched to a better model of
    determining whether a string is naughty or nice. None of the old rules
    apply, as they are all clearly ridiculous. How many strings are nice under
    the new rules?

    :return: None; Answer should be 53.
    """

    with open("src/day_05/input.txt", "r") as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if _is_string_nice_part2(line):
                count += 1

    print(count)

################################################################################