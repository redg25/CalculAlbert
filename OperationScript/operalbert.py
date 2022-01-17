"""This module create a class to generate random operations based on various parameters"""
import random
from typing import List, Optional,Union
#from typing_extensions import Literal

# Ops = List[Literal['+','-','*','/']]
Ops = List[str]
FloatInt = Optional[Union[float, int]]


class Calcul:

    """
    generate random operations based on 4 parameters:
    - Maximum result expected
    - Number of numbers in the operations
    - Operators to be used
    - Range for each number of the operation
    Returns:
         - string: representation of the operation
         - integer: result
    Eval was not used because it calculates using fractions
    and I want each single operation to result as an integer.
    For example: 14/3*6 will eval to 28 as it is 14*6/3
    but if we calculate one operation at the time, we get 14/3 = 4.6667
    """

    def __init__(self, max_result:int, max_nb:int, operators:Ops, ranges:List[int]):
        self.max_result = max_result  # Maximum result for the operation
        self.max_nb = max_nb  # Number of elements in operation
        self.operators = operators   # Possible operators to be used
        self.ranges = ranges  # Ranges for elements
        self.numbers_for_operations: List[int] = []  # List of operation's elements
        self.operators_for_operations: Ops = []  # List of operation's operators
        self.operation_string = ''  # String representation of the generated operation
        self.result: FloatInt = None  # Result of the operation

    def __get_operation_string(self):
        self.operation_string = ''
        for i, number in enumerate(self.numbers_for_operations):
            if i == len(self.numbers_for_operations) - 1:
                self.operation_string = self.operation_string + str(number)
            else:
                self.operation_string = self.operation_string \
                                        + str(number) \
                                        + self.operators_for_operations[i]


    def make_operation(self)-> tuple:
        """Generate a random operation then
         returns the string representation and the result as an integer"""

        self.result = self.max_result + 1
        while not self.result or self.result > self.max_result or self.result < 0:
            self.numbers_for_operations = []
            self.operators_for_operations = []
            self.__get_numbers()
            self.__get_operators()
            self.__get_operation_string()
            self.result = self.__get_result(self.numbers_for_operations.copy(),
                                            self.operators_for_operations.copy())
        return self.operation_string, self.result

    def __get_numbers(self):
        missing_ranges = self.max_nb-len(self.ranges)
        for _ in range(missing_ranges):
            self.ranges.append(self.ranges[-1])
        for max_range in self.ranges:
            self.numbers_for_operations.append(random.choice(range(2,max_range+1)))
        random.shuffle(self.numbers_for_operations)

    def __get_operators(self):
        for _ in range(self.max_nb-1):
            self.operators_for_operations.append(random.choice(self.operators))

    def __get_result(self, ls_nb: List[int], ls_op: Ops) -> FloatInt:
        """ Retrieve the result of an operation based on a list of numbers and
        a list of operands.
        Multiplication and division are done first
        then all others operations from left to right.
       """

        def calculate_mul_and_div(ls_nb: List[int], operator: str, i: int):
            first_number = ls_nb[i]
            calc = getattr(first_number, dund[operator])
            first_number = calc(ls_nb[i+1])
            return first_number

        self.result = 0
        # mapping string operands with their dunder
        dund = {'+': '__add__', '*': '__mul__', '/': '__truediv__', '-': '__sub__'}
        # Calculate multiplication and division first
        for i, operator in enumerate(ls_op):
            if operator in ('*', '/'):
                self.result = calculate_mul_and_div(ls_nb,operator,i)
                if (isinstance(self.result, float) and self.result.is_integer()) \
                        or isinstance(self.result, int):
                    self.result = int(self.result)
                    del ls_op[i]
                    ls_nb[i+1] = self.result
                    del ls_nb[i]
                    return self.__get_result(ls_nb, ls_op)
                else:
                    return None

        self.result = ls_nb[0]
        # Calculate remaining operations from left to right
        for number, operator in zip(ls_nb[1:], ls_op):
            calc = getattr(self.result, dund[operator])
            self.result = calc(number)
        return self.result
