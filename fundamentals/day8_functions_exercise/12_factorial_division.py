def factorial(number):
    if number == 0:
        return 1
    for current_number in range(1, number):
        number *= current_number
    return number


number_one = int(input())
number_two = int(input())
result = factorial(number_one) / factorial(number_two)
print(f'{result:.2f}')