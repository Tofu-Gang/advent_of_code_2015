from typing import Dict

from numpy import array
from re import compile

"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic
gates! Unfortunately, little Bobby is a little under the recommended age range,
and he needs help assembling the circuit.
"""

# operators from the puzzle input
AND = "AND"
OR = "OR"
LSHIFT = "LSHIFT"
RSHIFT = "RSHIFT"
NOT = "NOT"
DENOMINATOR = "->"

# python counterparts to the operators in the puzzle input; to be used in eval()
BITWISE_AND = "&"
BITWISE_OR = "|"
BITWISE_LSHIFT = "<<"
BITWISE_RSHIFT = ">>"
BITWISE_NOT = "~"

BINARY_OPERATORS = (AND, OR, LSHIFT, RSHIFT)
BINARY_BITWISE_OPERATORS = (BITWISE_AND, BITWISE_OR, BITWISE_LSHIFT, BITWISE_RSHIFT)
GOAL_WIRE = "a"

################################################################################

def _load_instructions() -> Dict[str, str]:
    """
    Loads the puzzle input and creates a dictionary where keys are strings-names
    of the wires and values are expressions that can be evaluated directly by
    eval() function.

    :return: wires dictionary
    """

    with open("src/day_07/input.txt", "r") as f:
        instructions = f.readlines()
        wires = {}

        # first create an entry for each wire
        [wires.update({instruction.split(DENOMINATOR)[1].strip(): None})
         for instruction in instructions]

        for instruction in instructions:
            expression = instruction.split(DENOMINATOR)[0].strip()
            result_wire = instruction.split(DENOMINATOR)[1].strip()

            if any([operator in expression for operator in BINARY_OPERATORS]):
                # binary operator
                operator_index = [expression.count(operator)
                                  for operator in BINARY_OPERATORS].index(1)
                operator = BINARY_OPERATORS[operator_index]
                bitwise_operator = BINARY_BITWISE_OPERATORS[operator_index]
                operand_left = expression.split(operator)[0].strip()
                operand_right = expression.split(operator)[1].strip()

                expression_to_eval = "("
                if operand_left in wires:
                    expression_to_eval += "wires[\"" + operand_left + "\"]"
                else:
                    expression_to_eval += operand_left
                expression_to_eval += bitwise_operator
                if operand_right in wires:
                    expression_to_eval += "wires[\"" + operand_right + "\"])"
                else:
                    expression_to_eval += operand_right + ")"
                wires[result_wire] = expression_to_eval
            elif NOT in expression:
                # unary operator NOT
                operand = expression.split(NOT)[1].strip()

                expression_to_eval = "("
                if operand in wires:
                    expression_to_eval += BITWISE_NOT \
                                          + "wires[\"" + operand + "\"])"
                else:
                    expression_to_eval += BITWISE_NOT + operand + ")"
                wires[result_wire] = expression_to_eval
            else:
                if expression in wires:
                    wires[result_wire] = "(wires[\"" + expression + "\"])"
                else:
                    # 16-bit signal to wire
                    wires[result_wire] = expression
        return wires

################################################################################

def _get_16_bit_number(input_number: int) -> int:
    """
    Converts the input number to 16bit signal value (a number from 0 to 65535).

    :param input_number: input number to be converted
    :return: 16bit signal value
    """

    return int(array([input_number], dtype="uint16"))

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

    wires = _load_instructions()

    while True:
        for key1 in wires:
            # look for wires that can be evaluated directly to an integer value
            try:
                int(eval(wires[key1]))
                # search for all usages of this wire
                for key2 in wires:
                    if "\""+key1+"\"" in str(wires[key2]):
                        # and replace it with its integer value
                        wire_in_expression = "wires[\""+key1+"\"]"
                        value_to_replace = str(_get_16_bit_number(int(eval(wires[key1]))))
                        wires[key2] = wires[key2].replace(wire_in_expression, value_to_replace)
            except (TypeError, ValueError):
                # this wire cannot be evaluated directly to an integer value, yet
                pass
        try:
            # let's see if the signal value in the goal wire can be evaluated
            print(_get_16_bit_number(int(eval(wires[GOAL_WIRE]))))
            break
        except ValueError:
            # hmm, not yet
            pass

################################################################################

def puzzle_02() -> None:
    """
    :return: None
    """

    pass

################################################################################