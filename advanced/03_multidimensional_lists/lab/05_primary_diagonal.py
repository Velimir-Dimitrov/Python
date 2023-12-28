matrix = [[int(x) for x in input().split()]for row in range(int(input()))]
primary_diagonal_sum = 0

for row in range(len(matrix)):
    col = row
    primary_diagonal_sum += matrix[row][col]

#
# secondary_diagonal = 0
# n = len(matrix)
# for row in range(n):
#     for col in range(n):
#         if (row + col) == (n - 1):
#             diagonal_sum += matrix[row][col]
# print(secondary_diagonal)

print(primary_diagonal_sum)