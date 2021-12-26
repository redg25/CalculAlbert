import random
from functools import reduce
from level_rules import *

operands: list = ["+","*","-","/"]

map_levels = {1:level1,
            }

class Calcul:

    def __init__(self,c_para):
        self.c_para = c_para
       

    # def set_calcul(self) -> str:
    #     str_numbers = [str(x) for x in self.numbers]
    #     return self.operand.join(str_numbers)
    #
    # def get_answer(self):
    #     if self.operand == "+":
    #         return reduce(lambda a,b: a+b,self.numbers)
    #     elif self.operand == "*":
    #         return reduce(lambda a,b: a*b,self.numbers)
    #     elif self.operand == "-":
    #         return reduce(lambda a,b: a-b,self.numbers)
    #     else:
    #         return reduce(lambda a,b: a/b,self.numbers)

    def make_calcul(self)-> tuple:
        self.result = self.c_para['max_result'] + 1
        while not isinstance(self.result, int) or self.result > self.c_para['max_result']:
            self.numbers = get_numbers(self.c_para['max_nb'],self.c_para['ranges'])
            self.operands = get_operands(len(self.numbers),self.c_para['operands'])
            self.result = get_result(self.numbers,self.operands)
        return self.result





c1 = Calcul({'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10]})
c1.make_calcul()
print (c1.numbers,c1.operands,c1.result)
c2 = Calcul({'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10,5]})
c2.make_calcul()
print (c2.numbers,c2.operands,c2.result)
c3 = Calcul({'max_result':100,'max_nb':3,'operands':['+','*'],'ranges':[10]})
c3.make_calcul()
print (c3.numbers,c3.operands,c3.result)
# c4= Calcul({'max_result':100,'max_nb':3,'operands':['/'],'ranges':[100]})
# c4.make_calcul()
# print (c4.numbers,c4.operands,c4.result)





