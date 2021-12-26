import random
from functools import reduce
from level_rules import *

operands: list = ["+","*","-","/"]

map_levels = {1:level1,
            }

class Calcul:

    def __init__(self, level:int):
        self.numbers, self.operand = map_levels[int]
       

    def set_calcul(self) -> str:
        str_numbers = [str(x) for x in self.numbers]
        return self.operand.join(str_numbers)

    def get_answer(self):
        if self.operand == "+":
            return reduce(lambda a,b: a+b,self.numbers)
        elif self.operand == "*":
            return reduce(lambda a,b: a*b,self.numbers)
        elif self.operand == "-":
            return reduce(lambda a,b: a-b,self.numbers)
        else:
            return reduce(lambda a,b: a/b,self.numbers)

    def make_calcul(self,c_para:dict)-> tuple:
        self.result = max + 1
        while result <= max:
            self.numbers = get_numbers()
            self.operands = get_operands()
            result = get_result(self.numbers,self.operands)









