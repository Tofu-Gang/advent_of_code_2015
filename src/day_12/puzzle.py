__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format. That's
where you come in.
"""

from re import compile
from json import loads
from typing import Dict, List
from src.utils.utils import print_puzzle_solution

RED = "red"
INPUT_FILE_PATH = "src/day_12/input.txt"


################################################################################

def _object_sum(input_object: [Dict, List], total_sum: int = 0) -> int:
    """
    Recursively goes through the input JSON object (arrays, objects, numbers and
    strings) and puts together a total sum of numbers in objects which do not
    contain string "red".

    :param input_object: input JSON object
    :return: total sum of numbers in objects that do not contain the string
    "red"
    """

    if type(input_object) == dict:
        if RED not in input_object and RED not in input_object.values():
            total_sum += sum(map(
                lambda key: _object_sum(input_object[key]),
                input_object))
    elif type(input_object) == list:
        total_sum += sum(map(
            lambda element: _object_sum(element),
            input_object))
    else:
        try:
            total_sum += int(input_object)
        except ValueError:
            # input object is not a number
            pass

    return total_sum


################################################################################

def puzzle_01() -> None:
    """
    The Accounting-Elves have a JSON document which contains a variety of
    things: arrays, objects, numbers, and strings. Your first job is to simply
    find all of the numbers throughout the document and add them together.

    :return: None; Answer should be 111754.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        document = f.read()
        pattern = compile(r'-*\d+')
        numbers = map(lambda match: int(match), pattern.findall(document))
        print_puzzle_solution(sum(numbers))


################################################################################

def puzzle_02() -> None:
    """
    Uh oh - the Accounting-Elves have realized that they double-counted
    everything red.

    Ignore any object (and all of its children) which has any property with the
    value "red". Do this only for objects ({...}), not arrays ([...]).

    :return: None; Answer should be 65402.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        document = loads(f.read())
        print_puzzle_solution(_object_sum(document))

################################################################################
