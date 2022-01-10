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
        numbers.append(random.choice(range(2,r+1)))
    random.shuffle(numbers)
    # if is_division:
    #     numbers.sort(reverse=True)
    return numbers


def get_operands(nb_len:int,operands:List[str])->List[str]:
    operands_ordered = []
    for i in range(nb_len-1):
        operands_ordered.append(random.choice(operands))
    return operands_ordered

def get_result(numbers:List[int],operands:List[str])-> int:
    """ Retrieve the result of an operation based on a list of numbers and
    a list of operands.
    Multiplication is done first then all others calculs from left to right.
    Requires that, if there is a division, it is always given a teh first element of the list of operands"""

    # mapping string operands with their dunder
    dund = {'+':'__add__','*':'__mul__','/':'__truediv__','-':'__sub__'}
    # create copy of the numbers and operands parameters from the Calcul instance
    ls_nb = numbers.copy()
    ls_op = operands.copy()
    # Calculate multiplication first
    for i, op in enumerate(ls_op):
        if op == "*":
            mul_res = ls_nb[i]*ls_nb[i+1]
            del ls_op[i]
            ls_nb[i+1]=mul_res
            del ls_nb[i]
            return get_result(ls_nb,ls_op)
    for i, op in enumerate(ls_op):
        if op == "/":
            div_res = ls_nb[i]/ls_nb[i+1]
            # return None if the result of the division is not an integer
            if type(div_res) == float and div_res.is_integer():
                div_res = int(div_res)
            else:
                return None
            del ls_op[i]
            ls_nb[i+1]=div_res
            del ls_nb[i]
            return get_result(ls_nb,ls_op)
    result = ls_nb[0]
    # Calculate remaining operations from left to right
    for n,op in zip(ls_nb[1:],ls_op):
        calc = getattr(result,dund[op])
        result = calc(n)
    #Cast the result to int from float if there was a division in the calcul and the result is an integer

    return result



