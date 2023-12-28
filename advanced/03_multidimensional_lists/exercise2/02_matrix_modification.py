def coordinates_are_valid(row, column, matrix_range):
    return 0 <= row < matrix_range and 0 <= column < matrix_range


n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]

command = input()

while command != "END":
    action, given_row, given_col, given_value = command.split()
    given_row = int(given_row)
    given_col = int(given_col)
    given_value = int(given_value)
    if coordinates_are_valid(given_row, given_col, n):
        if action == "Add":
            matrix[given_row][given_col] += given_value
        elif action == "Subtract":
            matrix[given_row][given_col] -= given_value
    else:
        print("Invalid coordinates")
    command = input()
[print(*matrix[row]) for row in range(n)]


