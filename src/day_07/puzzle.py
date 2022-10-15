__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic
gates! Unfortunately, little Bobby is a little under the recommended age range,
and he needs help assembling the circuit.
"""

from typing import Union, Any
from re import compile, findall
from src.utils.utils import print_puzzle_solution


################################################################################

class Assembly(object):
    # operators from the puzzle input
    AND = "AND"
    OR = "OR"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"
    NOT = "NOT"
    DENOMINATOR = "->"

    # functions to evaluate the instructions
    FUNCTIONS = {
        AND: lambda operands: operands[0] & operands[1],
        OR: lambda operands: operands[0] | operands[1],
        LSHIFT: lambda operands: operands[0] << operands[1],
        RSHIFT: lambda operands: operands[0] >> operands[1],
        NOT: lambda operands: ~operands[0],
        None: lambda operands: operands[0]
    }

    INPUT_FILE_PATH = "src/day_07/input.txt"
    GOAL_WIRE = "a"
    OVERRIDDEN_WIRE = "b"

################################################################################

    def __init__(self):
        """
        Load instructions and initialize the wires dictionary.
        """

        self._instructions = None
        self._wires = None
        self._reset_wires()

################################################################################

    def process_instructions(self) -> None:
        """
        Try to update the wires dictionary with each instruction. If successful,
        remove the instruction; eventually, all instructions are successfully
        processed and none remains.
        """

        while len(self._instructions) > 0:
            instruction = self._instructions.pop(0)
            operator = self._get_operator(instruction)
            operands = self._get_operands(instruction)
            result_wire = self._get_result_wire(instruction)

            try:
                self._wires[result_wire] = self.FUNCTIONS[operator](operands)
                if self._wires[result_wire] is None:
                    # the wires dict was not updated; add the instruction back
                    # so it is eventually processed again
                    self._instructions.append(instruction)
            except TypeError:
                # the wires dict was not updated; add the instruction back so it
                # is eventually processed again
                self._instructions.append(instruction)

################################################################################

    def override(self) -> None:
        """
        Finish the assembly and get goal wire signal value. Reset all wires,
        load all instructions back so they are processed again and store a
        signal value to the overriden wire. Then, remove the instructions that
        would store a signal value to the overriden wire.
        """

        self.process_instructions()
        goal_signal = self.get_goal_wire_signal
        self._reset_wires()
        self._wires[self.OVERRIDDEN_WIRE] = goal_signal
        self._instructions = list(filter(
            lambda instruction:
            self._get_result_wire(instruction) != self.OVERRIDDEN_WIRE,
            self._instructions))

################################################################################

    @property
    def get_goal_wire_signal(self) -> int:
        """
        :return: goal wire signal value
        """

        return self._wires[self.GOAL_WIRE]

################################################################################

    def _reset_wires(self) -> None:
        """
        Load instructions and initialize the wires dictionary.
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._instructions = f.readlines()
            self._wires = {}
            [self._wires.update({self._get_result_wire(instruction): None})
             for instruction in self._instructions]

################################################################################

    def _get_operator(self, instruction: str) -> Union[str, None]:
        """
        :param instruction: one instruction from the input file
        :return: operator from the instruction, or None if a direct signal is
        provided to a wire or a wire is redirected to the result wire
        """

        pattern = compile("{}|{}|{}|{}|{}".format(
            self.AND, self.OR, self.LSHIFT, self.RSHIFT, self.NOT))
        try:
            return findall(pattern, instruction)[0]
        except IndexError:
            return None

################################################################################

    def _get_operands(self, instruction: str) -> tuple[Union[int, Any], ...]:
        """
        :param instruction: one instruction from the input file
        :return: operand(s) from the instruction
        """

        left = instruction.split(self.DENOMINATOR)[0].strip()
        operator = self._get_operator(instruction)
        return tuple(int(operand.strip()) if operand.strip().isnumeric()
                     else self._wires[operand.strip()]
                     for operand in left.split(operator)
                     if len(operand) > 0)

################################################################################

    def _get_result_wire(self, instruction: str) -> str:
        """
        :param instruction: one instruction from the input file
        :return: result wire of the instruction
        """

        return instruction.split(self.DENOMINATOR)[1].strip()


################################################################################

def puzzle_01() -> None:
    """
    Each wire has an identifier (some lowercase letters) and can carry a 16-bit
    signal (a number from 0 to 65535). A signal is provided to each wire by a
    gate, another wire, or some specific value. Each wire can only get a signal
    from one source, but can provide its signal to multiple destinations. A gate
    provides no signal until all of its inputs have a signal.

    The included instructions booklet describes how to connect the parts
    together: x AND y -> z means to connect wires x and y to an AND gate, and
    then connect its output to wire z.

    Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If,
    for some reason, you'd like to emulate the circuit instead, almost all
    programming languages (for example, C, JavaScript, or Python) provide
    operators for these gates.

    In little Bobby's kit's instructions booklet (provided as your puzzle
    input), what signal is ultimately provided to wire a?

    :return: None; Answer should be 956.
    """

    assembly = Assembly()
    assembly.process_instructions()
    print_puzzle_solution(assembly.get_goal_wire_signal)


################################################################################

def puzzle_02() -> None:
    """
    Now, take the signal you got on wire a, override wire b to that signal, and
    reset the other wires (including wire a). What new signal is ultimately
    provided to wire a?

    :return: None; Answer should be 40149.
    """

    assembly = Assembly()
    assembly.override()
    assembly.process_instructions()
    print_puzzle_solution(assembly.get_goal_wire_signal)

################################################################################
