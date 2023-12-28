rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_square_sum = float('-inf')
max_row = 0
max_col = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(column, column + 3):
                current_sum += matrix[r][c]
        if max_square_sum < current_sum:
            max_square_sum = current_sum
            max_row = row
            max_col = column

print(f"Sum = {max_square_sum}")
[print(*[matrix[row][col] for col in range(max_col, max_col + 3)]) for row in range(max_row, max_row + 3)]
