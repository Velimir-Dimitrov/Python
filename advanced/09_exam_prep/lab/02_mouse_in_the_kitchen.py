n, m = [int(x) for x in input().split(',')]
cupboard = [list(input()) for row in range(n)]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
mouse_position = [[row, col] for col in range(m) for row in range(n) if cupboard[row][col] == "M"][0]
cheese = [[row, col] for col in range(m) for row in range(n) if cupboard[row][col] == "C"]

while True:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break
    direction_row, direction_col = directions[command]
    mouse_row, mouse_col = mouse_position
    new_row = direction_row + mouse_row
    new_col = direction_col + mouse_col
    if (0 > new_row or new_row >= n) or (0 > new_col or new_col >= m):
        print("No more cheese for tonight!")
        break
    elif cupboard[new_row][new_col] == "@":
        continue
    elif cupboard[new_row][new_col] == "T":
        cupboard[mouse_row][mouse_col] = "*"
        cupboard[new_row][new_col] = "M"
        print("Mouse is trapped!")
        break
    elif [new_row, new_col] in cheese:
        cheese.remove([new_row, new_col])
        if not cheese:
            cupboard[mouse_row][mouse_col] = "*"
            cupboard[new_row][new_col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    cupboard[mouse_row][mouse_col] = "*"
    mouse_position = [new_row, new_col]
    cupboard[new_row][new_col] = "M"

[print(''.join(cupboard[row])) for row in range(n)]

