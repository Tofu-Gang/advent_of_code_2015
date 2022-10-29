__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 21: RPG Simulator 20XX ---

Little Henry Case got a new video game for Christmas. It's an RPG, and he's 
stuck on a boss. He needs to know what equipment to buy at the shop. He hands 
you the controller.
"""

from re import compile
from itertools import product, permutations
from sys import maxsize
from typing import Dict, Tuple, Generator
from src.utils.utils import print_puzzle_solution

INPUT_FILE_PATH = "src/day_21/input.txt"
WEAPONS_FILE_PATH = "src/day_21/weapons.txt"
ARMOR_FILE_PATH = "src/day_21/armor.txt"
RINGS_FILE_PATH = "src/day_21/rings.txt"

KEY_NAME = "Name"
KEY_COST = "Cost"
KEY_DAMAGE = "Damage"
KEY_ARMOR = "Armor"
KEY_HIT_POINTS = "Hit Points"


################################################################################

def load_weapons() -> Tuple[Dict[str, int], ...]:
    """
    :return: weapons tuple; each weapon is a dict with weapon name, cost, damage
    and armor values
    """

    with open(WEAPONS_FILE_PATH, "r") as f:
        lines = f.readlines()
        return tuple({
            KEY_NAME: line.strip().split()[0],
            KEY_COST: int(line.strip().split()[1]),
            KEY_DAMAGE: int(line.strip().split()[2]),
            KEY_ARMOR: int(line.strip().split()[3])
        } for line in lines[1:])


################################################################################

def load_armor() -> Tuple[Dict[str, int], ...]:
    """
    :return: armor tuple; each armor is a dict with weapon name, cost, damage
    and armor values
    """

    with open(ARMOR_FILE_PATH, "r") as f:
        lines = f.readlines()
        return tuple({
            KEY_NAME: line.strip().split()[0],
            KEY_COST: int(line.strip().split()[1]),
            KEY_DAMAGE: int(line.strip().split()[2]),
            KEY_ARMOR: int(line.strip().split()[3])
        } for line in lines[1:])


################################################################################

def load_rings() -> Tuple[Dict[str, int], ...]:
    """
    :return: rings tuple; each ring is a dict with weapon name, cost, damage and
    armor values
    """

    with open(RINGS_FILE_PATH, "r") as f:
        lines = f.readlines()
        return tuple({
            KEY_NAME: line.strip().split()[0],
            KEY_COST: int(line.strip().split()[1]),
            KEY_DAMAGE: int(line.strip().split()[2]),
            KEY_ARMOR: int(line.strip().split()[3])
        } for line in lines[1:])


################################################################################

def load_boss() -> Dict[str, int]:
    """
    :return: boss dict with its hit points, damage and armor values
    """

    with open(INPUT_FILE_PATH, "r") as f:
        contents = f.read()
        hit_points = int(compile(r"Hit Points: (\d+)").findall(contents)[0])
        damage = int(compile(r"Damage: (\d+)").findall(contents)[0])
        armor = int(compile(r"Armor: (\d+)").findall(contents)[0])

        return {
            KEY_HIT_POINTS: hit_points,
            KEY_DAMAGE: damage,
            KEY_ARMOR: armor
        }


################################################################################

def load_player(equipment: Tuple[Dict[str, int]]) -> Dict[str, int]:
    """
    :param equipment: player equipment (weapon, armor, left hand ring, right
    hand ring)
    :return: player dict with its hit points, damage and armor values; the
    latter two are counted from equipment damage and armor values
    """

    return {
        KEY_HIT_POINTS: 100,
        KEY_DAMAGE: sum(item[KEY_DAMAGE] for item in equipment),
        KEY_ARMOR: sum(item[KEY_ARMOR] for item in equipment)
    }


################################################################################

def equipment_combinations() -> Generator[Tuple[Dict[str, int]], None, None]:
    """
    :return: equipment combinations generator; each equipment combination
    consists of a weapon, armor, left hand ring and right hand ring
    """

    weapons = load_weapons()
    armor = load_armor()
    rings = load_rings()

    for equipment in product(*(weapons, armor, permutations(rings, 2))):
        yield tuple([equipment[0], equipment[1], *equipment[2]])


################################################################################

def fight(player: Dict[str, int], boss: Dict[str, int]) -> bool:
    """
    Simulate player vs boss fight.

    :param player: player dict (hit points, damage, armor)
    :param boss: boss dict (hit points, damage, armor)
    :return: True if the player wins, False if the boss wins
    """

    while True:
        boss[KEY_HIT_POINTS] -= max(player[KEY_DAMAGE] - boss[KEY_ARMOR], 1)
        if boss[KEY_HIT_POINTS] <= 0:
            return True
        else:
            player[KEY_HIT_POINTS] -= max(boss[KEY_DAMAGE] - player[KEY_ARMOR], 1)
            if player[KEY_HIT_POINTS] <= 0:
                return False


################################################################################

def puzzle_01() -> None:
    """
    In this game, the player (you) and the enemy (the boss) take turns
    attacking. The player always goes first. Each attack reduces the opponent's
    hit points by at least 1. The first character at or below 0 hit points
    loses.

    Damage dealt by an attacker each turn is equal to the attacker's damage
    score minus the defender's armor score. An attacker always does at least 1
    damage. So, if the attacker has a damage score of 8, and the defender has an
    armor score of 3, the defender loses 5 hit points. If the defender had an
    armor score of 300, the defender would still lose 1 hit point.

    Your damage score and armor score both start at zero. They can be increased
    by buying items in exchange for gold. You start with no items and have as
    much gold as you need. Your total damage or armor is equal to the sum of
    those stats from all of your items. You have 100 hit points.

    Here is what the item shop is selling:

    Weapons:    Cost  Damage  Armor
    Dagger        8     4       0
    Shortsword   10     5       0
    Warhammer    25     6       0
    Longsword    40     7       0
    Greataxe     74     8       0

    Armor:      Cost  Damage  Armor
    Leather      13     0       1
    Chainmail    31     0       2
    Splintmail   53     0       3
    Bandedmail   75     0       4
    Platemail   102     0       5

    Rings:      Cost  Damage  Armor
    Damage +1    25     1       0
    Damage +2    50     2       0
    Damage +3   100     3       0
    Defense +1   20     0       1
    Defense +2   40     0       2
    Defense +3   80     0       3

    You must buy exactly one weapon; no dual-wielding. Armor is optional, but
    you can't use more than one. You can buy 0-2 rings (at most one for each
    hand). You must use any items you buy. The shop only has one of each item,
    so you can't buy, for example, two rings of Damage +3.

    You have 100 hit points. The boss's actual stats are in your puzzle input.
    What is the least amount of gold you can spend and still win the fight?

    :return: None; Answer should be 121.
    """

    min_equipment_cost = maxsize

    for equipment in equipment_combinations():
        player = load_player(equipment)
        boss = load_boss()
        equipment_cost = sum(item[KEY_COST] for item in equipment)

        if fight(player, boss) is True and equipment_cost < min_equipment_cost:
            min_equipment_cost = equipment_cost

    print_puzzle_solution(min_equipment_cost)


################################################################################

def puzzle_02() -> None:
    """
    Turns out the shopkeeper is working with the boss, and can persuade you to
    buy whatever items he wants. The other rules still apply, and he still only
    has one of each item.

    What is the most amount of gold you can spend and still lose the fight?

    :return: None; Answer should be 201.
    """

    max_equipment_cost = -maxsize - 1

    for equipment in equipment_combinations():
        player = load_player(equipment)
        boss = load_boss()
        equipment_cost = sum(item[KEY_COST] for item in equipment)

        if fight(player, boss) is False and equipment_cost > max_equipment_cost:
            max_equipment_cost = equipment_cost

    print_puzzle_solution(max_equipment_cost)

################################################################################
