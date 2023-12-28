from collections import deque
rows, columns = [int(x) for x in input().split()]
random_string = deque(input())

snake_matrix = []

for row in range(rows):
    snake_matrix.append([''] * columns)
    for col in range(columns):
        if row % 2 == 0:
            snake_matrix[row][col] = random_string[0]
        else:
            snake_matrix[row][-1 - col] = random_string[0]
        random_string.rotate(-1)

[print(*snake_matrix[row], sep='') for row in range(rows)]

