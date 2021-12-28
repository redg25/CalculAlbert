import random
from typing import List


def level1():
    n1 = random.choice(range(10))
    n2 = random.choice(range(10))
    if n1 + n2 < 11:
        return [n1, n2], "+"
    else:
        return level1()

def get_numbers(nb:int,ranges:List[int],is_division:bool) -> List[int]:
    missing_ranges = nb-len(ranges)
    for i in range(missing_ranges):
        ranges.append(ranges[-1])
    numbers = []
    for r in ranges:
        numbers.append(random.choice(range(1,r+1)))
    if is_division:
        numbers.sort(reverse=True)
    return numbers


def get_operands(nb_len:int,operands:List[str])->List[str]:
    operands_ordered = []
    for i in range(nb_len-1):
        operands_ordered.append(random.choice(operands))
    return operands_ordered

def get_result(numbers:List[int],operands:List[str],is_division:bool)-> int:
    dund = {'+':'__add__','*':'__mul__','/':'__truediv__','-':'__sub__'}
    result = numbers[0]
    for n,op in zip(numbers[1:],operands):
        calc = getattr(result,dund[op])
        result = calc(n)
    #Cast the result to int from float if there was a division in the calcul and the result is an integer
    if is_division and result.is_integer():
        result = int(result)
    return result



