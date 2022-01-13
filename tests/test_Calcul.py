from main import *

c1 = Calcul(10,2,['+'],[10])
c2 = Calcul(100,3,['+','*','/'],[50,10])
c3 = Calcul(100,5,['+','*','/'],[50,10])

def test_get_numbers():
    for i in range(10):
        c1.make_operation()
        c2.make_operation()
        nb1 = c1.numbers_for_operations
        nb2 = c2.numbers_for_operations
        assert len(nb1) == 2
        assert len(nb2) == 3
        for n in nb1:
            assert n < 11
        nb2.sort(reverse=True)
        assert nb2[0]<51
        assert nb2[1]<11
        assert nb2[2]<11


def test_get_operators():
    for i in range(10):
        c1.make_operation()
        c2.make_operation()
        c3.make_operation()
        assert len(c1.operators_for_operations) == 1
        assert len(c2.operators_for_operations) == 2
        assert "+" == c1.operators_for_operations[0]
        for op in c3.operators_for_operations:
            assert op in c3.operators

def test_get_result():
    for i in range(10):
        c1.make_operation()
        c2.make_operation()
        c3.make_operation()
        assert eval(c1.operation_string) == c1.result
        assert eval(c2.operation_string) == c2.result
        assert eval(c3.operation_string) == c3.result
