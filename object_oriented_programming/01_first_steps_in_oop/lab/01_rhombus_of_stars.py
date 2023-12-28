def print_rhombus(size):
    for row in range(1, size + 1):
        print_triangle(size, row)
    for row in range(size - 1, -1, -1):
        print_triangle(size, row)


def print_triangle(size, current_row):
    print(' ' * (size - current_row), end='')
    print(*['*'] * current_row)


print_rhombus(int(input()))



