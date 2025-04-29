from src.operators import add, sub, mul

def test_add():
    assert add(1, 2) == 3
    assert add(3, 5) == 8


def test_sub():
    assert sub(3, 1) == 2
    assert sub(5, 6) == -1

def test_mul():
    assert mul(5, 4) == 20