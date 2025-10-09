"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""


def add(a, b):
    """Add two numbers together"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b"""
    return a**b


def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5
