def dfs(key, row, col, matrix, visited, directions):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != key:
        return

    visited[row][col] = True

    for (dr, dc) in directions:
        dfs(key, row + dr, col + dc, matrix, visited, directions)


rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]

visited = [[False] * cols for _ in range(rows)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

areas = {}
areas_count = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue

        target_chat = matrix[row][col]
        dfs(target_chat, row, col, matrix, visited, directions)

        if target_chat not in areas:
            areas[target_chat] = 0
        areas[target_chat] += 1
        areas_count += 1

if areas:
    print(f"Areas: {areas_count}")
    for area, count in sorted(areas.items()):
        print(f"Letter '{area}' -> {count}")


# # Example inputs
# 6
# 8
# aacccaac
# baaaaccc
# baabaccc
# bbdaaccc
# ccdccccc
# ccdccccc