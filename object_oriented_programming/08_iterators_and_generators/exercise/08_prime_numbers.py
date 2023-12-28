from math import sqrt
def prime_checker(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(list_with_numbers: list):
    for num in list_with_numbers:
        if prime_checker(num):
            yield num


# Test code:
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-2, 0, 0, 1, 1, 0])))
print(list(get_primes([100_000_007, 0, 0 , 1 , 1])))