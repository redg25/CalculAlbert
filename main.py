import random
from functools import reduce
from level_rules import *

operands: list = ["+","*","-","/"]

map_levels = {1:level1,
            }

class Calcul:

    def __init__(self,c_para):
        self.c_para = c_para
       

    def _get_calcul_string(self) -> str:
        calcul_str = ''
        for i, n in enumerate(self.numbers):
            if i == len(self.numbers) - 1:
                calcul_str = calcul_str + str(n)+"="
            else:
                calcul_str = calcul_str + str(n) + self.operands[i]
        return calcul_str

    def make_calcul(self)-> tuple:
        self.result = self.c_para['max_result'] + 1
        is_division = "/" in self.c_para['operands']
        while not isinstance(self.result, int) or self.result > self.c_para['max_result']:
            self.numbers = get_numbers(self.c_para['max_nb'],self.c_para['ranges'],is_division)
            self.operands = get_operands(len(self.numbers),self.c_para['operands'])
            self.result = get_result(self.numbers,self.operands,is_division)
        return (self._get_calcul_string(),self.result)





c1 = Calcul({'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10]})
print(c1.make_calcul())
#print (c1.numbers,c1.operands,c1.result)
c2 = Calcul({'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10,1]})
print(c2.make_calcul())
#print (c2.numbers,c2.operands,c2.result)
c3 = Calcul({'max_result':100,'max_nb':3,'operands':['+','*'],'ranges':[10]})
print(c3.make_calcul())
#print (c3.numbers,c3.operands,c3.result)
c4= Calcul({'max_result':100,'max_nb':3,'operands':['/'],'ranges':[1000,500,500]})
print(c4.make_calcul())
#print (c4.numbers,c4.operands,c4.result)





