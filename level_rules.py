import random


def level1():
    n1 = random.choice(range(10))
    n2 = random.choice(range(10))
    if n1 + n2 < 11:
        return [n1, n2], "+"
    else:
        return level1()


