from functools import wraps


def multiply(times):
    def decoder(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times
        return wrapper
    return decoder


# Test code
@multiply(3)
def add_ten(number):
    return number + 10


# print(add_ten.__name__)
print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
