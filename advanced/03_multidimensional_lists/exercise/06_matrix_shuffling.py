def valid_coordinates(num1_row, num1_col, num2_row, num2_col, matrix_rows, matrix_columns):
    return 0 <= num1_row < matrix_rows and 0 <= num1_col < matrix_columns \
        and 0 <= num2_row < matrix_rows and 0 <= num2_col < matrix_columns


rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]

while True:
    command = input().split()

    if command[0] == "END":
        break

    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]

    if valid_coordinates(row1, col1, row2, col2, rows, columns):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*matrix[row], sep=' ') for row in range(rows)]
    else:
        print("Invalid input!")