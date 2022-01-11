import random
from typing import List


operators: list = ["+","*","-","/"]

class Calcul:

    def __init__(self,max_result:int,max_nb:int,operators:operators,ranges:List[int]):
        self.max_result = max_result
        self.max_nb = max_nb
        self.operators = operators
        self.ranges = ranges
        self.numbers_for_operations = []
        self.operators_for_operations = []


    def _get_calcul_string(self) -> str:
        calcul_str = ''
        for i, n in enumerate(self.numbers_for_operations):
            if i == len(self.numbers_for_operations) - 1:
                calcul_str = calcul_str + str(n)+"="
            else:
                calcul_str = calcul_str + str(n) + self.operators_for_operations[i]
        return calcul_str

    def make_calcul(self)-> tuple:
        self.result = self.max_result + 1
        is_division = "/" in self.operators
        while not self.result or  self.result > self.max_result or self.result < 0:
            self.numbers_for_operations = []
            self.operators_for_operations = []
            self.__get_numbers()
            self.__get_operators()
            self.calcul_string = self._get_calcul_string()
            self.result  = self.__get_result(self.numbers_for_operations.copy(),self.operators_for_operations.copy())
        return (self.calcul_string,self.result)


    def __get_numbers(self):
        missing_ranges = self.max_nb-len(self.ranges)
        for i in range(missing_ranges):
            self.ranges.append(self.ranges[-1])
        for r in self.ranges:
            self.numbers_for_operations.append(random.choice(range(2,r+1)))
        random.shuffle(self.numbers_for_operations)


    def __get_operators(self):
        for i in range(self.max_nb-1):
            self.operators_for_operations.append(random.choice(self.operators))

    def __get_result(self,ls_nb,ls_op)-> int:
        """ Retrieve the result of an operation based on a list of numbers and
        a list of operands.
        Multiplication and division are done first then all others calculs from left to right.
       """

        def calcul_mul_and_div(ls_nb,op,i):
            n1 = ls_nb[i]
            calc = getattr(n1,dund[op])
            n1 = calc(ls_nb[i+1])
            return n1

        self.result = 0
        # mapping string operands with their dunder
        dund = {'+':'__add__','*':'__mul__','/':'__truediv__','-':'__sub__'}
        # Calculate multiplication and division first
        for i, op in enumerate(ls_op):
            if op == '*' or op == '/':
                self.result = calcul_mul_and_div(ls_nb,op,i)
                if (type(self.result) == float and self.result.is_integer()) or type(self.result) == int:
                    self.result = int(self.result)
                    del ls_op[i]
                    ls_nb[i+1]=self.result
                    del ls_nb[i]
                    return self.__get_result(ls_nb,ls_op)
                else:
                    return None

        self.result = ls_nb[0]
        # Calculate remaining operations from left to right
        for n,op in zip(ls_nb[1:],ls_op):
            calc = getattr(self.result,dund[op])
            self.result = calc(n)
        return self.result




