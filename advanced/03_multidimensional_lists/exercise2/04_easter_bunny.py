n = int(input())
matrix = [[x for x in input().split()] for row in range(n)]
bunny_location = [[int(row), int(col)] for col in range(n) for row in range(n) if matrix[row][col] == "B"]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

best_direction = ''
maximum_eggs = float('-inf')
best_routine = []

for current_direction, step in directions.items():
    current_eggs = 0
    current_routine = []
    bunny_row = bunny_location[0][0]
    bunny_col = bunny_location[0][1]
    direction_row = step[0]
    direction_col = step[1]
    new_row = bunny_row + direction_row
    new_col = bunny_col + direction_col
    while 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == 'X':
            break
        current_eggs += int(matrix[new_row][new_col])
        current_routine.append([new_row, new_col])
        new_row += direction_row
        new_col += direction_col
    if current_eggs > maximum_eggs:
        maximum_eggs = current_eggs
        best_routine = current_routine
        best_direction = current_direction
print(best_direction)
[print(row) for row in best_routine]
print(maximum_eggs)