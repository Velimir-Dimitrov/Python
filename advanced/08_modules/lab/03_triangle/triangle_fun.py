def print_triangle(num):
    num = int(num)
    for row in range(1, num+1):
        for n in range(1, row + 1):
            print(n, end=' ')
        print()
    for negative_r in range(num - 1, 0, -1):
        for negative_n in range(1, negative_r + 1):
            print(negative_n, end=' ')
        print()