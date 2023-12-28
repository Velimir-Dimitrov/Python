def make_bold(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<b>" + f"{result}" + "</b>"
    return wrapper


def make_italic(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<i>" + f"{result}" + "</i>"
    return wrapper


def make_underline(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<u>" + f"{result}" + "</u>"
    return wrapper


# Test code:
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
