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


def get_operands(nb_len:int,operands_order:List[str])->List[str]:
    pass

def get_result(numbers:List[int],operands:List[str])-> int:
    pass


