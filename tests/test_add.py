import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(10, 20) == 30

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-10, -20) == -30

def test_add_mixed_sign_numbers():
    assert add(-2, 3) == 1
    assert add(2, -3) == -1

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)
    assert add(-2.5, 2.5) == pytest.approx(0.0)
