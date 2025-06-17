def find_paths(matrix, row, col, path, directions):
    if not (0 <= row < len(matrix) and 0 <= col < len(matrix[0])):
        return
    if matrix[row][col] in ['*', 'v']:
        return
    if matrix[row][col] == 'e':
        print(''.join(path))
        return

    matrix[row][col] = 'v'

    for direction, (dr, dc) in directions.items():
        path.append(direction)
        find_paths(matrix, row + dr, col + dc, path, directions)
        path.pop()

    matrix[row][col] = '-'


rows = int(input())
cols = int(input())
labyrinth = [list(input()) for _ in range(rows)]

directions = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

find_paths(labyrinth, 0, 0, [], directions)


# # Inputs
# 3
# 3
# ---
# -*-
# --e

# 3
# 5
# -**-e
# -----
# *****