def valid_position(rows, cols, position_r, position_c):
    if position_r < rows and position_c < cols:
        return True

def find_paths(directions, rows, cols, position_r, position_c):

    if not valid_position(rows, cols, position_r, position_c):
        return 0
    if position_r == rows -1 and position_c == cols - 1:
        return 1

    solutions = 0
    for row_move, col_move in directions:
        solutions += find_paths(directions, rows, cols, position_r + row_move, position_c + col_move)

    return solutions


rows = int(input())
cols = int(input())
directions = [(1,0),(0, 1)]

print(find_paths(directions, rows, cols, 0, 0))

# # Inputs
# 3
# 2
#
# 3
# 5


# # Shorter solution without matrix
# def find_paths(rows, cols, r, c):
#     if r >= rows or c >= cols:
#         return 0
#     if r == rows - 1 and c == cols - 1:
#         return 1
#     return find_paths(rows, cols, r + 1, c) + find_paths(rows, cols, r, c + 1)
# 
# rows = int(input())
# cols = int(input())
#
# print(find_paths(rows, cols, 0, 0))
