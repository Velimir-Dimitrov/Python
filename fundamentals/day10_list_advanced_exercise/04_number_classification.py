def find_positive_of(some_list):
    return [x for x in some_list if int(x) >= 0]


def find_negative_of(some_list):
    return [x for x in some_list if int(x) < 0]


def find_even_of(some_list):
    return [x for x in some_list if int(x) % 2 == 0]


def find_odd_of(some_list):
    return [x for x in some_list if int(x) % 2 != 0]


numbers = input().split(", ")
positive_numbers = ", ".join(find_positive_of(numbers))
negative_numbers = ", ".join(find_negative_of(numbers))
even_numbers = ", ".join(find_even_of(numbers))
odd_numbers = ", ".join(find_odd_of(numbers))
print(f'Positive: {positive_numbers}\nNegative: {negative_numbers}\nEven: {even_numbers}\nOdd: {odd_numbers}')