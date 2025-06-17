from functools import lru_cache

@lru_cache
def fibonacci(number):
    if number <= 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)



num = int(input())
print(fibonacci(num))

# # Input
# 5
# 10
# 21