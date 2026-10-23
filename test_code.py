# calculator code
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    if x < 0:
        return "Error: Square root of negative number is not allowed."
    return math.hypot(x, 0)