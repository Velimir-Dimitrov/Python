def check_even(num):
    if num % 2 == 0:
        return True
    return False


numbers_in_string = input().split()
list_of_integers = [int(x) for x in numbers_in_string]
list_even_numbers = list(filter(check_even, list_of_integers))
print(list_even_numbers)
