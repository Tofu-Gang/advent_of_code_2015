__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, 
and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is 
going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry 
isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission 
plant, capable of constructing any Red-Nosed Reindeer molecule you need. It 
works by starting with some input molecule and then doing a series of 
replacements, one per step, until it has the right molecule.
"""

from typing import Dict, Tuple
from re import compile
from random import sample
from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_19/input.txt"
ELECTRON = "e"


################################################################################

def get_rules() -> Dict[str, Tuple[str, ...]]:
    """
    Loads the replacement rules from the input file in the original direction,
    from one electron to a medicine molecule. There is usually more than one
    possibility to one left side of a rule, so the keys of the dict are strings
    and values are tuples of replacement possibilities.

    :return: replacement rules dict (1:N)
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        rules = dict()

        for line in lines[:-2]:
            key = compile(r"(.+) =>").findall(line.strip())[0]
            value = compile(r"=> (.+)").findall(line.strip())[0]
            rules.setdefault(key, [])
            rules[key].append(value)
        return rules


################################################################################

def get_rules_reversed() -> Dict[str, str]:
    """
    Loads the replacement rules from the input file in the reversed direction,
    from a medicine molecule to one electron. There is always only one possible
    replacement for every left side of a rule, so both keys and values of the
    dict are just strings.

    :return: replacement rules dict (1:1)
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        return {
            compile(r"=> (.+)").findall(line.strip())[0]:
                compile(r"(.+) =>").findall(line.strip())[0]
            for line in lines[:-2]
        }


################################################################################

def get_molecule() -> str:
    """
    Loads the medicine molecule from the input file.

    :return: medicine molecule
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        return lines[-1].strip()


################################################################################

def apply_rule(left: str, right: str, index: int, molecule: str) -> str:
    """
    Applies a replacement rule to a molecule string in the specified place.

    :param left: left side of the replacement rule
    :param right: right side of the replacement rule
    :param index: position of the left side substring in the molecule string
    :param molecule: molecule string before the rule application
    :return: molecule string after the rule application
    """

    return molecule[:index] + right + molecule[index + len(left):]


################################################################################

def puzzle_01() -> None:
    """
    However, the machine has to be calibrated before it can be used. Calibration
    involves determining the number of molecules that can be generated in one
    step from a given starting point.

    Your puzzle input describes all of the possible replacements and, at the
    bottom, the medicine molecule for which you need to calibrate the machine.
    How many distinct molecules can be created after all the different ways you
    can do one replacement on the medicine molecule?

    :return: None; Answer should be 509.
    """

    rules = get_rules()
    molecule = get_molecule()
    results = set(apply_rule(key, value, index, molecule)
                  for key in rules
                  for value in rules[key]
                  for index in [m.start()
                                for m in compile(key).finditer(molecule)])
    print_puzzle_solution(len(results))


################################################################################

def puzzle_02() -> None:
    """
    Now that the machine is calibrated, you're ready to begin molecule
    fabrication.

    Molecule fabrication always begins with just a single electron, e, and
    applying replacements one at a time, just like the ones during calibration.

    How long will it take to make the medicine? Given the available replacements
    and the medicine molecule in your puzzle input, what is the fewest number of
    steps to go from e to the medicine molecule?

    :return: None; Answer should be 195.
    """

    rules = get_rules_reversed()
    start_molecule = get_molecule()
    goal_molecule = ELECTRON

    while True:
        # start with the medicine molecule and try to reduce it to one electron
        molecule = start_molecule
        # count the number of applied rules
        count = 0

        while True:
            rule_was_applied = False
            # shuffle all the rules
            keys = sample(rules.keys(), k=len(rules.keys()))

            for key in keys:
                # try to apply all the rules, one by one

                while True:
                    # try to find the rule left side in the molecule
                    index = molecule.find(key)

                    if index == -1:
                        # no rule left side occurrence in the molecule, move on
                        # to another rule
                        break
                    else:
                        # apply the rule
                        molecule = apply_rule(key, rules[key], index, molecule)
                        rule_was_applied = True
                        count += 1

            if not rule_was_applied:
                # we went through all the rules without being able to apply a
                # single one
                break

        if molecule == goal_molecule:
            # the medicine molecule was successfully reduced to one electron
            print_puzzle_solution(count)
            break
        else:
            # the reduction result is different to one electron, start over
            continue

################################################################################
