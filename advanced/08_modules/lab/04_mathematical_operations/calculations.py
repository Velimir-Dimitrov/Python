def divide(num1, num2):
    if num2 == 0:
        return print("You cannot divide by zero.")
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2


def add(num1, num2):
    return num1 + num2


def power(num1, num2):
    return num1 ** num2


mapper = {
    "/": divide,
    "*": multiply,
    "-": subtract,
    "+": add,
    "^": power
}