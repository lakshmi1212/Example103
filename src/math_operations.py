def add(a, b):
    """Add two numbers and return the result."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a - b
