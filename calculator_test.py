import pytest 
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(3, 2) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)