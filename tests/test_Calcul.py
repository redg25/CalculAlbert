from main import Calcul
from level_rules import *

set_int_1 = [2,3]
set_int_2 = [2,3,4]
set_int_3 = [20,2,2]
# op1 = "+"
# op2 = "*"
# op3 = "-"
# op4 = "/"
# ex1 = Calcul(set_int_1,op1)
# ex2 = Calcul(set_int_2,op2)
# ex3 = Calcul(set_int_3,op4)
para_set_1 = {'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10]}
para_set_2 = {'max_result':10,'max_nb':2,'operands':['+'],'ranges':[10,5]}
para_set_3 = {'max_result':10,'max_nb':3,'operands':['+'],'ranges':[10,5]}

# def test_setcalcul():
#     assert ex1.set_calcul() == "2+3"
#     assert ex2.set_calcul() == "2*3*4"
#
# def test_get_answer():
#     assert ex1.get_answer() == 5
#     assert ex2.get_answer() == 24
#     assert ex3.get_answer() == 5

def test_get_numbers():
    for i in range(10):
        nb = get_numbers(para_set_1['max_nb'],para_set_1['ranges'])
        assert len(nb) == 2
        for n in nb:
            assert n < 11
        nb = get_numbers(para_set_2['max_nb'], para_set_2['ranges'])
        assert len(nb) == 2
        assert nb[0]<11
        assert nb[1]<6
        nb = get_numbers(para_set_3['max_nb'], para_set_3['ranges'])
        assert len(nb) == 3
        assert nb[0] < 11
        assert nb[1] < 6
        assert nb[2] < 6

