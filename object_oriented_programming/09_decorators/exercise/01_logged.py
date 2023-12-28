def logged(function):
    def wrapper(*args):
        result = f"you called {function.__name__}{args}\nit returned {function(*args)}"
        return result

    return wrapper


# Test code:

@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

