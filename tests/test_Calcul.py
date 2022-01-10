from main import Calcul
from level_rules import *

set_int_1 = [2,3]
set_int_2 = [2,3,4]
set_int_3 = [20,2,2]

op1 = ["+"]
op2 = ['*','*']
op3 = ["+","*"]
op4 = ['/','/']

para_set_1 = {'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10]}
para_set_2 = {'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10,5]}
para_set_3 = {'max_result':10,'max_nb':3,'operands':['+'],'ranges':[10,5]}
para_set_4 = {'max_result':10,'max_nb':2,'operands':['+','*'],'ranges':[10]}
para_set_5 = {'max_result':10,'max_nb':3,'operands':['+','*'],'ranges':[10]}


def test_get_numbers():
    for i in range(10):
        nb = get_numbers(para_set_1['max_nb'],para_set_1['ranges'],False)
        assert len(nb) == 2
        for n in nb:
            assert n < 11
        nb = get_numbers(para_set_2['max_nb'], para_set_2['ranges'],False)
        assert len(nb) == 2
        assert nb[0]<11
        assert nb[1]<6
        nb = get_numbers(para_set_3['max_nb'], para_set_3['ranges'],False)
        assert len(nb) == 3
        assert nb[0] < 11
        assert nb[1] < 6
        assert nb[2] < 6
        nb = get_numbers(para_set_3['max_nb'], para_set_3['ranges'], True)
        assert nb[0]>=nb[1]>=nb[2]

def test_get_operands():
    nb_add = 0
    nb_multiply = 0
    for i in range(10):
        op = get_operands(para_set_5['max_nb'],para_set_5['operands'])
        assert len(op) == 2
        assert op[0] in ['+','*'] and op[1] in ['+','*']
        if (op[0] or op[1]) == '+': nb_add += 1
        if (op[0] or op[1]) == '*': nb_multiply += 1
    assert nb_add > 2 and nb_multiply > 2

def test_get_result():
    assert get_result(set_int_1, op1,False) == 5
    assert get_result(set_int_2, op2,False) == 24
    assert get_result(set_int_2, op3,False) == 14
    assert get_result(set_int_3, op4,True) == 5