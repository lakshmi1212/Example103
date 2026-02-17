import pytest
from src.math_operations import subtract

def test_subtract_integers():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_subtract_floats():
    assert subtract(5.5, 3.5) == 2.0
    assert subtract(-1.2, 1.2) == -2.4
    assert subtract(0.0, 0.0) == 0.0

def test_subtract_mixed_types():
    assert subtract(5, 3.5) == 1.5
    assert subtract(-1.5, 2) == -3.5

@pytest.mark.parametrize("a,b", [("5", 3), (None, 1), ([], {})])
def test_subtract_invalid_types(a, b):
    with pytest.raises(TypeError):
        subtract(a, b)
