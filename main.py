import random
from functools import reduce
from level_rules import *

toperands: list = ["+","*","-","/"]

map_levels = {1:level1,
            }

class Calcul:

    def __init__(self,max_result:int,max_nb:int,operands:toperands,ranges:List[int]):
        self.max_result = max_result
        self.max_nb = max_nb
        self.operands = operands
        self.ranges = ranges


    def _get_calcul_string(self) -> str:
        calcul_str = ''
        for i, n in enumerate(self.numbers):
            if i == len(self.numbers) - 1:
                calcul_str = calcul_str + str(n)+"="
            else:
                calcul_str = calcul_str + str(n) + self.operands[i]
        return calcul_str

    def make_calcul(self)-> tuple:
        self.result = self.max_result + 1
        is_division = "/" in self.operands
        while not self.result or  self.result > self.max_result or self.result < 0:
            self.numbers = get_numbers(self.max_nb,self.ranges, is_division)
            self.operands = get_operands(len(self.numbers),self.operands)
            calcul_string = self._get_calcul_string()
            self.result = get_result(self.numbers,self.operands)
        return (calcul_string,self.result)





c1 = Calcul(20,3,['+','-'],[15])
print(c1.make_calcul())
# #print (c1.numbers,c1.operands,c1.result)
# c2 = Calcul(10,2,['+'],[10,1])
# print(c2.make_calcul())
#print (c2.numbers,c2.operands,c2.result)
c3 = Calcul(1000,4,['+','*','/','-'],[500,100,10])
print(c3.make_calcul())
#print (c3.numbers,c3.operands,c3.result)
# c4= Calcul(100,3,['/'],[1000,500,500])
# print(c4.make_calcul())
#print (c4.numbers,c4.operands,c4.result)




