import pytest
from src.math_operations import add

def test_add_integers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_floats():
    assert add(2.5, 3.5) == 6.0
    assert add(-1.2, 1.2) == 0.0
    assert add(0.0, 0.0) == 0.0

def test_add_mixed_types():
    assert add(2, 3.5) == 5.5
    assert add(-1.5, 2) == 0.5

@pytest.mark.parametrize("a,b", [("2", 3), (None, 1), ([], {})])
def test_add_invalid_types(a, b):
    with pytest.raises(TypeError):
        add(a, b)
