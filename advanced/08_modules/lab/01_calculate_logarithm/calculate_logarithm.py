from math import log


def calculate_logarithm(num1, num2):
    if num2 == 'natural':
        return print(f"{log(float(num1)):.2f}")
    return print(f"{log(float(num1), float(num2)):.2f}")