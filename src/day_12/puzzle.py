from re import compile
from json import loads
from typing import Dict, List

"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order.
Unfortunately, their accounting software uses a peculiar storage format. That's
where you come in.
"""

RED = "red"

################################################################################

def _object_sum(input_object: [Dict, List], total_sum: int = 0) -> int:
    """
    Recursively goes through the input JSON object (lists, dicts, numbers and
    strings) and puts together a total sum of numbers in dicts which do not
    contain string "red".

    :param input_object: input JSON object
    :return: total sum of numbers in objects that do not contain the string
    "red"
    """

    if type(input_object) == dict:
        values = [input_object[key] for key in input_object]
        if RED not in input_object and RED not in values:
            for key in input_object:
                total_sum += _object_sum(input_object[key])
    elif type(input_object) == list:
        for element in input_object:
            total_sum += _object_sum(element)
    else:
        try:
            total_sum += int(input_object)
        except ValueError:
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

    with open("src/day_12/input.txt", "r") as f:
        document = f.read()
        regex = compile(r'-*\d+')
        print(sum([int(number) for number in regex.findall(document)]))

################################################################################

def puzzle_02() -> None:
    """
    Uh oh - the Accounting-Elves have realized that they double-counted
    everything red.

    Ignore any object (and all of its children) which has any property with the
    value "red". Do this only for objects ({...}), not arrays ([...]).

    :return: None; Answer should be 65402.
    """

    with open("src/day_12/input.txt", "r") as f:
        document = loads(f.read())
        print(_object_sum(document))

################################################################################