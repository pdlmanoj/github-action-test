from apps.calculator import add, substract


def test_add():
    assert add(2, 4) == 6
    assert add(9, -1) == 8  


def test_subtract():
    assert substract(9, 4) == 5
    assert substract(10, 10) == 0 
