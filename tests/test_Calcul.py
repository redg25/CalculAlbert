from main import Calcul

set_int_1 = [2,3]
set_int_2 = [2,3,4]
set_int_3 = [20,2,2]
op1 = "+"
op2 = "*"
op3 = "-"
op4 = "/"
ex1 = Calcul(set_int_1,op1)
ex2 = Calcul(set_int_2,op2)
ex3 = Calcul(set_int_3,op4)

def test_setcalcul():
    assert ex1.set_calcul() == "2+3"
    assert ex2.set_calcul() == "2*3*4"

def test_get_answer():
    assert ex1.get_answer() == 5
    assert ex2.get_answer() == 24
    assert ex3.get_answer() == 5