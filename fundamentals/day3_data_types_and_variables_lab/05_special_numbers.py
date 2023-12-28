n = int(input())

for num in range(1, n+1):
    special = False
    digit_sum = 0
    digit = num
    while digit > 0:
        digit_sum += digit % 10
        digit = int(digit/10)
    if digit_sum % 5 == 0 or digit_sum % 7 == 0 or digit_sum % 11 == 0:
        special = True
    print(f'{num} -> {special}')

