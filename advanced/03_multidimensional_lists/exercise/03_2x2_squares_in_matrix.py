rows, columns = [int(x) for x in input().split()]
matrix = [[el for el in input().split()] for row in range(rows)]

identical_chars = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current_el = matrix[row][column]
        right_el = matrix[row][column + 1]
        below_el = matrix[row + 1][column]
        diagonal_el = matrix[row + 1][column + 1]
        if current_el == right_el == below_el == diagonal_el:
            identical_chars += 1
print(identical_chars)