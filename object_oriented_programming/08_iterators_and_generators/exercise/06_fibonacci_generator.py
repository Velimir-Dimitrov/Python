def fibonacci():
    current_num, next_num = 0, 1
    while True:
        yield current_num
        current_num, next_num = next_num, current_num + next_num


# Test code:
generator = fibonacci()
for i in range(15):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))

