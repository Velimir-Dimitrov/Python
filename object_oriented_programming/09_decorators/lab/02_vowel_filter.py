def vowel_filter(function):
    def wrapper():
        return [char for char in function() if char in "aeyuio"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
