__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some 
unknown benefactor. It comes with instructions and an example program, but the 
computer itself seems to be malfunctioning. She's curious what the program does, 
and would like you to help her run it.
"""

from re import compile
from src.utils.utils import print_puzzle_solution


################################################################################

class Computer(object):
    INPUT_FILE_PATH = "src/day_23/input.txt"
    KEY_REGISTER_A = "a"
    KEY_REGISTER_B = "b"

    KEY_INSTRUCTION_HLF = "hlf"
    KEY_INSTRUCTION_TPL = "tpl"
    KEY_INSTRUCTION_INC = "inc"
    KEY_INSTRUCTION_JMP = "jmp"
    KEY_INSTRUCTION_JIE = "jie"
    KEY_INSTRUCTION_JIO = "jio"

    KEY_INSTRUCTION = "INSTRUCTION"
    KEY_REGISTER = "REGISTER"
    KEY_OFFSET = "OFFSET"

################################################################################

    def __init__(self):
        """
        Creates the two registers, a and b - a dictionary where register name
        directly from the program is used as a key) and an instructions dict,
        where again, instruction name directly from the program is used as a
        key. Value is then a lambda function that calls the specific function.
        """

        self._registers = {
            self.KEY_REGISTER_A: 0,
            self.KEY_REGISTER_B: 0
        }
        self._INSTRUCTIONS = {
            self.KEY_INSTRUCTION_HLF: lambda r, offset: self._hlf(r),
            self.KEY_INSTRUCTION_TPL: lambda r, offset: self._tpl(r),
            self.KEY_INSTRUCTION_INC: lambda r, offset: self._inc(r),
            self.KEY_INSTRUCTION_JMP: lambda r, offset: self._jmp(offset),
            self.KEY_INSTRUCTION_JIE: lambda r, offset: self._jie(r, offset),
            self.KEY_INSTRUCTION_JIO: lambda r, offset: self._jio(r, offset)
        }
        self._program_counter = 0
        self._program = []

################################################################################

    def load_program(self) -> None:
        """
        Loads program from the input file. Every program line is represented as
        a dictionary with an instruction, register and offset (register and
        offset can be None if this parameter is not used with the specific
        instruction).
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            lines = f.readlines()
            instruction_pattern = compile(r"^(\D{3}) ")
            register_pattern = compile(r" ([a|b])")
            offset_pattern = compile(r" ([+|-]\d+)")

            for line in lines:
                instruction = instruction_pattern.findall(line)[0]
                program_line = {
                    self.KEY_INSTRUCTION: instruction
                }
                try:
                    register = register_pattern.findall(line)[0]
                    program_line[self.KEY_REGISTER] = register
                except IndexError:
                    program_line[self.KEY_REGISTER] = None
                try:
                    offset = int(offset_pattern.findall(line)[0])
                    program_line[self.KEY_OFFSET] = offset
                except IndexError:
                    program_line[self.KEY_OFFSET] = None

                self._program.append(program_line)

            self._program = tuple(self._program)

################################################################################

    def run_program(self) -> None:
        """
        Runs the program until it tries to run an instruction beyond the ones
        defined.
        """

        while 0 <= self._program_counter < len(self._program):
            program_line = self._program[self._program_counter]
            instruction = program_line[self.KEY_INSTRUCTION]
            register = program_line[self.KEY_REGISTER]
            offset = program_line[self.KEY_OFFSET]
            self._INSTRUCTIONS[instruction](register, offset)

################################################################################

    @property
    def register_a(self) -> int:
        """
        :return: register a value
        """

        return self._registers[self.KEY_REGISTER_A]

################################################################################

    @property
    def register_b(self) -> int:
        """
        :return: register b value
        """

        return self._registers[self.KEY_REGISTER_B]

################################################################################

    @register_a.setter
    def register_a(self, value) -> None:
        """
        Sets the register a value (only positive integers or 0 are accepted).

        :param value: new register a value
        """

        if value >= 0:
            self._registers[self.KEY_REGISTER_A] = value

################################################################################

    @register_b.setter
    def register_b(self, value) -> None:
        """
        Sets the register b value (only positive integers or 0 are accepted).

        :param value: new register b value
        """

        if value >= 0:
            self._registers[self.KEY_REGISTER_B] = value

################################################################################

    def _hlf(self, r: str) -> None:
        """
        hlf r sets register r to half its current value, then continues with the
        next instruction.

        :param r: register
        """

        self._registers[r] //= 2
        self._program_counter += 1

################################################################################

    def _tpl(self, r: str) -> None:
        """
        tpl r sets register r to triple its current value, then continues with
        the next instruction.

        :param r: register
        """

        self._registers[r] *= 3
        self._program_counter += 1

################################################################################

    def _inc(self, r: str) -> None:
        """
        inc r increments register r, adding 1 to it, then continues with the
        next instruction.

        :param r: register
        """

        self._registers[r] += 1
        self._program_counter += 1

################################################################################

    def _jmp(self, offset: int) -> None:
        """
        jmp offset is a jump; it continues with the instruction offset away
        relative to itself.

        :param offset: where to move the program counter relative to the current
        instruction
        """

        self._program_counter += offset

################################################################################

    def _jie(self, r: str, offset: int) -> None:
        """
        jie r, offset is like jmp, but only jumps if register r is even ("jump
        if even").

        :param r: register
        :param offset: where to move the program counter relative to the current
        instruction
        """

        if self._registers[r] % 2 == 0:
            self._program_counter += offset
        else:
            self._program_counter += 1

################################################################################

    def _jio(self, r: str, offset: int) -> None:
        """
        jio r, offset is like jmp, but only jumps if register r is 1
        ("jump if one", not odd).

        :param r: register
        :param offset: where to move the program counter relative to the current
        instruction
        """

        if self._registers[r] == 1:
            self._program_counter += offset
        else:
            self._program_counter += 1


################################################################################

def puzzle_01() -> None:
    """
    The manual explains that the computer supports two registers and six
    instructions (truly, it goes on to remind the reader, a state-of-the-art
    technology). The registers are named a and b, can hold any non-negative
    integer, and begin with a value of 0. The instructions are as follows:

    -hlf r sets register r to half its current value, then continues with the
     next instruction.
    -tpl r sets register r to triple its current value, then continues with the
     next instruction.
    -inc r increments register r, adding 1 to it, then continues with the next
     instruction.
    -jmp offset is a jump; it continues with the instruction offset away
     relative to itself.
    -jie r, offset is like jmp, but only jumps if register r is even ("jump if
     even").
    -jio r, offset is like jmp, but only jumps if register r is 1
     ("jump if one", not odd).

    All three jump instructions work with an offset relative to that
    instruction. The offset is always written with a prefix + or - to indicate
    the direction of the jump (forward or backward, respectively). For example,
    jmp +1 would simply continue with the next instruction, while jmp +0 would
    continuously jump back to itself forever.

    The program exits when it tries to run an instruction beyond the ones
    defined.

    What is the value in register b when the program in your puzzle input is
    finished executing?

    :return: None; Answer should be 307.
    """

    computer = Computer()
    computer.load_program()
    computer.run_program()
    print_puzzle_solution(computer.register_b)


################################################################################

def puzzle_02() -> None:
    """
    The unknown benefactor is very thankful for releasi-- er, helping little
    Jane Marie with her computer. Definitely not to distract you, what is the
    value in register b after the program is finished executing if register a
    starts as 1 instead?

    :return: None; Answer should be 160.
    """

    computer = Computer()
    computer.load_program()
    computer.register_a = 1
    computer.run_program()
    print_puzzle_solution(computer.register_b)

################################################################################
