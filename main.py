import random
from functools import reduce
from level_rules import *

operators: list = ["+","*","-","/"]

class Calcul:

    def __init__(self,max_result:int,max_nb:int,operators:operators,ranges:List[int]):
        self.max_result = max_result
        self.max_nb = max_nb
        self.operators = operators
        self.ranges = ranges


    def _get_calcul_string(self) -> str:
        calcul_str = ''
        for i, n in enumerate(self.numbers):
            if i == len(self.numbers) - 1:
                calcul_str = calcul_str + str(n)+"="
            else:
                calcul_str = calcul_str + str(n) + self.operators[i]
        return calcul_str

    def make_calcul(self)-> tuple:
        self.result = self.max_result + 1
        is_division = "/" in self.operators
        while not self.result or  self.result > self.max_result or self.result < 0:
            self.numbers = get_numbers(self.max_nb,self.ranges, is_division)
            self.operators = get_operands(len(self.numbers),self.operators)
            self.calcul_string = self._get_calcul_string()
            self.result = get_result(self.numbers,self.operators)
        return (self.calcul_string,self.result)










