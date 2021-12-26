import random
from typing import List


def level1():
    n1 = random.choice(range(10))
    n2 = random.choice(range(10))
    if n1 + n2 < 11:
        return [n1, n2], "+"
    else:
        return level1()

def get_numbers(nb:int,ranges:List[int]) -> List[int]:
    missing_ranges = nb-len(ranges)
    for i in range(missing_ranges):
        ranges.append(ranges[-1])
    numbers = []
    for r in ranges:
        numbers.append(random.choice(range(r+1)))
    return numbers


def get_operands(nb_len:int,operands:List[str])->List[str]:
    operands_ordered = []
    for i in range(nb_len-1):
        operands_ordered.append(random.choice(operands))
    return operands_ordered

def get_result(numbers:List[int],operands:List[str])-> int:
    dund = {'+':'__add__','*':'__mul__','/':'__truediv__','-':'__sub__'}
    result = numbers[0]
    for n,op in zip(numbers[1:],operands):
        if op == "/" and n == 0:
            n = 1
        calc = getattr(result,dund[op])
        result = calc(n)
    return result



