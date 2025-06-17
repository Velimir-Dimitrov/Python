def calculate_recursively_factorial(num):
    if num == 0:
        return 1
    return num * calculate_recursively_factorial(num - 1)

num = int(input())

print(calculate_recursively_factorial(num))


## Inputs
# 5
# 10