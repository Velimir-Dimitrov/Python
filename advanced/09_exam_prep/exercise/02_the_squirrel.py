from collections import deque
n = int(input())
directions = deque(input().split(', '))
field_matrix = [list(input()) for row in range(n)]

mapper = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}


squirrel_position = [[row, col] for col in range(n) for row in range(n) if field_matrix[row][col] == "s"][0]
collected_hazelnuts = 0

while True:
    if collected_hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break
    if not directions:
        print("There are more hazelnuts to collect.")
        break
    direction_row, direction_col = mapper[directions.popleft()]
    squirrel_row, squirrel_col = squirrel_position
    new_row = direction_row + squirrel_row
    new_col = direction_col + squirrel_col
    if (0 > new_row or new_row >= n) or (0 > new_col or new_col >= n):
        print("The squirrel is out of the field.")
        break
    elif field_matrix[new_row][new_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    elif field_matrix[new_row][new_col] == "h":
        collected_hazelnuts += 1
    squirrel_position = [new_row, new_col]
    field_matrix[squirrel_row][squirrel_col] = "*"

print(f"Hazelnuts collected: {collected_hazelnuts}")