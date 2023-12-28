# rows = int(input())
# matrix = []
# flattening_matrix = []
#
# for row in range(rows):
#     matrix.append([int(x) for x in input().split(', ')])
#
# for row in range(rows):
#     for col in range(len(matrix[row])):
#         flattening_matrix.append(matrix[row][col])
# print(flattening_matrix)

matrix = [[int(x) for x in input().split(', ')] for row in range(int(input()))]
flattening_matrix = [num for sub_matrix in matrix for num in sub_matrix]
print(flattening_matrix)