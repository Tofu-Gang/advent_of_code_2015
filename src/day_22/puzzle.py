__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 22: Wizard Simulator 20XX ---

Little Henry Case decides that defeating bosses with swords and stuff is boring. 
Now he's playing the game with a wizard. Of course, he gets stuck on another 
boss and needs your help again.
"""

from typing import Callable, Tuple, Union
from re import compile
from logging import basicConfig, INFO, info, WARNING, root
from sys import maxsize
from random import choice
from src.utils.utils import print_puzzle_solution

RANDOM_FIGHTS_COUNT = 1000000


################################################################################

class Game(object):
    INPUT_FILE_PATH = "src/day_22/input.txt"

    MAGIC_MISSILE_MANA_COST = 53
    MAGIC_MISSILE_DAMAGE = 4

    DRAIN_MANA_COST = 73
    DRAIN_DAMAGE = 2
    DRAIN_HEAL = 2

    SHIELD_MANA_COST = 113
    SHIELD_TIMER = 6
    SHIELD_ARMOR = 7

    POISON_MANA_COST = 173
    POISON_TIMER = 6
    POISON_DAMAGE = 3

    RECHARGE_MANA_COST = 229
    RECHARGE_TIMER = 5
    RECHARGE_MANA = 101

    MANA_COSTS = (MAGIC_MISSILE_MANA_COST,
                  DRAIN_MANA_COST,
                  POISON_MANA_COST,
                  SHIELD_MANA_COST,
                  RECHARGE_MANA_COST)

    PLAYER_INIT_HIT_POINTS = 50
    PLAYER_INIT_MANA = 500
    PLAYER_INIT_ARMOR = 0

################################################################################

    def __init__(self):
        """
        All instance variables initialized to None because new_game() method is
        used to load the starting values. Loads boss hit points and damage from
        the input file.
        """

        self._player_hit_points = None
        self._mana = None
        self._armor = None
        self._shield_timer = None
        self._poison_timer = None
        self._recharge_timer = None
        self._total_mana_cost = None
        self._hard_difficulty = None
        self._history = None
        self._boss_hit_points = None

        with open(self.INPUT_FILE_PATH, "r") as f:
            contents = f.read()
            self.BOSS_INIT_HIT_POINTS = int(
                compile(r"Hit Points: (\d+)").findall(contents)[0])
            self._BOSS_DAMAGE = int(
                compile(r"Damage: (\d+)").findall(contents)[0])

################################################################################

    @property
    def history(self) -> Tuple[str]:
        """
        :return: spells used in the fight
        """

        return tuple(self._history)

################################################################################

    def fight_easy(self, logging_on: bool = False) -> int:
        """
        Game simulation with easy difficulty - puzzle 1. Spells sequence taken
        from random fights with the best result (win with the lowest mana cost).

        :param logging_on: if True, additional logging messages are printed
        :return: total mana cost of the fight in case of win; -1 in case of a
        loss (shouldn't happen as the spells are prepared for a win)
        """

        self._new_game(hard_difficulty=False, logging_on=logging_on)

        self._turn(self._poison)
        self._turn(self._magic_missile)
        self._turn(self._recharge)
        self._turn(self._poison)
        self._turn(self._shield)
        self._turn(self._magic_missile)
        self._turn(self._magic_missile)
        self._turn(self._magic_missile)
        self._turn(self._magic_missile)

        return self._total_mana_cost

################################################################################

    def fight_hard(self, logging_on: bool = False) -> int:
        """
        Game simulation with hard difficulty - puzzle 2. Spells sequence taken
        from random fights with the best result (win with the lowest mana cost).

        :param logging_on: if True, additional logging messages are printed
        :return: total mana cost of the fight in case of win; -1 in case of a
        loss (shouldn't happen as the spells are prepared for a win)
        """

        self._new_game(hard_difficulty=True, logging_on=logging_on)

        self._turn(self._poison)
        self._turn(self._drain)
        self._turn(self._recharge)
        self._turn(self._poison)
        self._turn(self._shield)
        self._turn(self._recharge)
        self._turn(self._poison)
        self._turn(self._drain)
        self._turn(self._magic_missile)

        return self._total_mana_cost

################################################################################

    def fight_random(
            self, hard_difficulty: bool, logging_on: bool = False) -> int:
        """
        Usable for both difficulties (both puzzles, 1 and 2). Set the difficulty
        and choose spells randomly. Best results (win with the lowest mana cost)
        were used to get spells sequences in fight_easy() and fight_hard()
        methods.

        :param hard_difficulty: True for puzzle 2, False for puzzle 1
        :param logging_on: if True, additional logging messages are printed
        :return: total fight mana cost in case of a win, -1 in case of a loss
        """

        self._new_game(hard_difficulty, logging_on)

        while True:
            spells = []
            if self._mana >= self.MAGIC_MISSILE_MANA_COST:
                spells.append(self._magic_missile)
            if self._mana >= self.DRAIN_MANA_COST:
                spells.append(self._drain)
            if self._mana >= self.SHIELD_MANA_COST and self._shield_timer <= 1:
                # counters not yet checked so if it is 1 it will be lowered to
                # zero and the spell can be cast
                spells.append(self._shield)
            if self._mana >= self.POISON_MANA_COST and self._poison_timer <= 1:
                # counters not yet checked so if it is 1 it will be lowered to
                # zero and the spell can be cast
                spells.append(self._poison)
            if self._mana >= self.RECHARGE_MANA_COST and self._recharge_timer <= 1:
                # counters not yet checked so if it is 1 it will be lowered to
                # zero and the spell can be cast
                spells.append(self._recharge)

            try:
                result = self._turn(choice(tuple(spells)))
            except IndexError:
                # no spell can be cast
                result = -1

            if result == -1 or result > 0:
                return result

################################################################################

    def _turn(self, spell: Callable) -> int:
        """
        One fight turn with the chosen spell.

        :param spell: spell method
        :return: total fight mana cost in case of a win, -1 in case of a loss,
        zero if the fight is not over yet
        """

        info("\n--- PLAYER TURN ---")
        if self._hard_difficulty is True:
            info("Hard difficulty; player hit points: {} -> {}".format(
                self._player_hit_points, self._player_hit_points - 1))
            self._player_hit_points -= 1

        if self._player_hit_points <= 0:
            info("PLAYER LOSES THE GAME!")
            return -1
        else:
            self._check_counters()
            info("Shield timer: {}".format(self._shield_timer))
            info("Poison timer: {}".format(self._poison_timer))
            info("Recharge timer: {}".format(self._recharge_timer))
            info("Player armor: {}".format(self._armor))
            info("Player hit points: {}".format(self._player_hit_points))
            info("Player mana: {}".format(self._mana))

            if all(self._mana < mana_cost for mana_cost in self.MANA_COSTS):
                info("PLAYER LOSES THE GAME!")
                return -1
            else:
                spell()

                if self._boss_hit_points <= 0:
                    info("PLAYER WINS THE GAME!")
                    return self._total_mana_cost
                else:
                    info("\n--- BOSS TURN ---")
                    self._check_counters()
                    info("Shield timer: {}".format(self._shield_timer))
                    info("Poison timer: {}".format(self._poison_timer))
                    info("Recharge timer: {}".format(self._recharge_timer))
                    info("Boss hit points: {}".format(self._boss_hit_points))
                    boss_damage = max(self._BOSS_DAMAGE - self._armor, 1)
                    info("Boss attacks player for {}: {} -> {}".format(
                        boss_damage,
                        self._player_hit_points,
                        self._player_hit_points - boss_damage))
                    self._player_hit_points -= boss_damage

                    if self._player_hit_points <= 0:
                        info("PLAYER LOSES THE GAME!")
                        return -1
        return 0

################################################################################

    def _new_game(self, hard_difficulty: bool, logging_on: bool) -> None:
        """
        Set all the instance variables for a new game.

        :param hard_difficulty: True for puzzle 2, False for puzzle 1
        :param logging_on: if True, additional logging messages are printed
        """

        # remove all existing handlers so basicConfig() can be called again
        [root.removeHandler(handler) for handler in root.handlers[:]]

        if logging_on is True:
            # see the fight logs
            basicConfig(level=INFO, format='%(message)s')
        else:
            # no logs
            basicConfig(level=WARNING, format='%(message)s')

        self._hard_difficulty = hard_difficulty
        self._player_hit_points = self.PLAYER_INIT_HIT_POINTS
        self._mana = self.PLAYER_INIT_MANA
        self._armor = self.PLAYER_INIT_ARMOR
        self._shield_timer = 0
        self._poison_timer = 0
        self._recharge_timer = 0
        self._total_mana_cost = 0
        self._history = []
        self._boss_hit_points = self.BOSS_INIT_HIT_POINTS

################################################################################

    def _check_counters(self) -> None:
        """
        Manage shield, poison and recharge counters and all its effects.
        """

        if self._shield_timer > 0:
            info("Shield provides additional armor.")
            self._armor = self.SHIELD_ARMOR
            self._shield_timer -= 1
        else:
            self._armor = self.PLAYER_INIT_ARMOR

        if self._poison_timer > 0:
            info("Poison provides additional damage: {} -> {}".format(
                self._boss_hit_points,
                self._boss_hit_points - self.POISON_DAMAGE))
            self._boss_hit_points -= self.POISON_DAMAGE
            self._poison_timer -= 1

        if self._recharge_timer > 0:
            info("Recharge provides additional mana: {} -> {}".format(
                self._mana, self._mana + self.RECHARGE_MANA))
            self._mana += self.RECHARGE_MANA
            self._recharge_timer -= 1

################################################################################

    def _magic_missile(self) -> None:
        """
        Cast the magic missile spell.
        """

        info("Casting magic missile for {} mana: {} -> {}".format(
            self.MAGIC_MISSILE_MANA_COST,
            self._mana,
            self._mana - self.MAGIC_MISSILE_MANA_COST))
        self._mana -= self.MAGIC_MISSILE_MANA_COST
        self._total_mana_cost += self.MAGIC_MISSILE_MANA_COST
        info("Damage for {}: {} -> {}".format(
            self.MAGIC_MISSILE_DAMAGE,
            self._boss_hit_points,
            self._boss_hit_points - self.MAGIC_MISSILE_DAMAGE))
        self._boss_hit_points -= self.MAGIC_MISSILE_DAMAGE
        self._history.append("Magic missile")

################################################################################

    def _drain(self) -> None:
        """
        Cast the drain spell.
        """

        info("Casting drain for {} mana: {} -> {}".format(
            self.DRAIN_MANA_COST,
            self._mana,
            self._mana - self.DRAIN_MANA_COST))
        self._mana -= self.DRAIN_MANA_COST
        self._total_mana_cost += self.DRAIN_MANA_COST
        info("Damage for {}: {} -> {}".format(
            self.DRAIN_DAMAGE,
            self._boss_hit_points,
            self._boss_hit_points - self.DRAIN_DAMAGE))
        self._boss_hit_points -= self.DRAIN_DAMAGE
        info("Heal for {}: {} -> {}".format(
            self.DRAIN_HEAL,
            self._player_hit_points,
            self._player_hit_points + self.DRAIN_HEAL))
        self._player_hit_points += self.DRAIN_HEAL
        self._history.append("Drain")

################################################################################

    def _shield(self) -> None:
        """
        Cast the shield spell.
        """

        info("Casting shield for {} mana: {} -> {}".format(
            self.SHIELD_MANA_COST,
            self._mana,
            self._mana - self.SHIELD_MANA_COST))
        self._mana -= self.SHIELD_MANA_COST
        self._total_mana_cost += self.SHIELD_MANA_COST
        self._shield_timer = self.SHIELD_TIMER
        self._history.append("Shield")

################################################################################

    def _poison(self) -> None:
        """
        Cast the poison spell.
        """

        info("Casting poison for {} mana: {} -> {}".format(
            self.POISON_MANA_COST,
            self._mana,
            self._mana - self.POISON_MANA_COST))
        self._mana -= self.POISON_MANA_COST
        self._total_mana_cost += self.POISON_MANA_COST
        self._poison_timer = self.POISON_TIMER
        self._history.append("Poison")

################################################################################

    def _recharge(self) -> None:
        """
        Cast the recharge spell.
        """

        info("Casting recharge for {} mana: {} -> {}".format(
            self.RECHARGE_MANA_COST,
            self._mana,
            self._mana - self.RECHARGE_MANA_COST))
        self._mana -= self.RECHARGE_MANA_COST
        self._total_mana_cost += self.RECHARGE_MANA_COST
        self._recharge_timer = self.RECHARGE_TIMER
        self._history.append("Recharge")


################################################################################

def fight_random(hard_difficulty: bool,
                 goal_mana_cost: Union[int, None] = None) -> None:
    """
    Set the difficulty and play the game with a random sequence of spells.

    If the goal total mana cost is stated, look for spells sequence that results
    in a win with total mana cost equal to or less to this goal. This can result
    in an infinite loop if the goal is set impossible (too low)!

    If the goal is not stated, do a set number of fights and get the best result
    (win with the lowest total mana cost).

    Regardless, print the total mana cost and spells sequence that lead to this
    result.

    :param hard_difficulty: True for puzzle 2, False for puzzle 1
    :param goal_mana_cost: if stated, look for spells sequence that results in a
    win with total mana cost equal to or less to this goal; can result in an
    infinite loop!
    """

    game = Game()

    if goal_mana_cost is not None:
        while True:
            total_mana_cost = game.fight_random(hard_difficulty)

            if total_mana_cost <= goal_mana_cost:
                print(total_mana_cost, ", ".join(game.history))
                break
    else:
        min_total_mana_cost = maxsize
        min_total_mana_cost_history = None

        for _ in range(RANDOM_FIGHTS_COUNT):
            total_mana_cost = game.fight_random(hard_difficulty)

            if total_mana_cost != -1 and total_mana_cost < min_total_mana_cost:
                min_total_mana_cost = total_mana_cost
                min_total_mana_cost_history = game.history

        print(min_total_mana_cost, ", ".join(min_total_mana_cost_history))


################################################################################

def puzzle_01() -> None:
    """
    In this version, combat still proceeds with the player and the boss taking
    alternating turns. The player still goes first. Now, however, you don't get
    any equipment; instead, you must choose one of your spells to cast. The
    first character at or below 0 hit points loses.

    Since you're a wizard, you don't get to wear armor, and you can't attack
    normally. However, since you do magic damage, your opponent's armor is
    ignored, and so the boss effectively has zero armor as well. As before, if
    armor (from a spell, in this case) would reduce damage below 1, it becomes 1
    instead - that is, the boss' attacks always deal at least 1 damage.

    On each of your turns, you must select one of your spells to cast. If you
    cannot afford to cast any spell, you lose. Spells cost mana; you start with
    500 mana, but have no maximum limit. You must have enough mana to cast a
    spell, and its cost is immediately deducted when you cast it. Your spells
    are Magic Missile, Drain, Shield, Poison, and Recharge.

    -Magic Missile costs 53 mana. It instantly does 4 damage.
    -Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit
     points.
    -Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it
     is active, your armor is increased by 7.
    -Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the
     start of each turn while it is active, it deals the boss 3 damage.
    -Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the
     start of each turn while it is active, it gives you 101 new mana.

    Effects all work the same way. Effects apply at the start of both the
    player's turns and the boss' turns. Effects are created with a timer (the
    number of turns they last); at the start of each turn, after they apply any
    effect they have, their timer is decreased by one. If this decreases the
    timer to zero, the effect ends. You cannot cast a spell that would start an
    effect which is already active. However, effects can be started on the same
    turn they end.

    You start with 50 hit points and 500 mana points. The boss's actual stats
    are in your puzzle input. What is the least amount of mana you can spend and
    still win the fight? (Do not include mana recharge effects as "spending"
    negative mana.)

    :return: None; Answer should be 953.
    """

    # fight_random(hard_difficulty=False)
    game = Game()
    total_mana_cost = game.fight_easy()
    print_puzzle_solution(total_mana_cost)


################################################################################

def puzzle_02() -> None:
    """
    On the next run through the game, you increase the difficulty to hard.

    At the start of each player turn (before any other effects apply), you lose
    1 hit point. If this brings you to or below 0 hit points, you lose.

    With the same starting stats for you and the boss, what is the least amount
    of mana you can spend and still win the fight?

    :return: None; Answer should be 1289.
    """

    # fight_random(hard_difficulty=True)
    game = Game()
    total_mana_cost = game.fight_hard()
    print_puzzle_solution(total_mana_cost)

################################################################################
