def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multyply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("на ноль делить нельзя")
    return a / b

def rem_divide(a, b):
    if b == 0:
        raise ValueError("на ноль делить нельзя")
    return a % b

def check(number):
    return number % 2 == 0