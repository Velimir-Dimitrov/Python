rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]

primary_diagonal = [matrix[n][n] for n in range(rows)]
secondary_diagonal = [matrix[n][rows - n - 1] for n in range(rows)]

# for row in range(rows):
#     for col in range(len(matrix)):
#         if row == col:
#             primary_diagonal.append(matrix[row][col])
#         if (row + col) == (len(matrix) - 1):
#             secondary_diagonal.append(matrix[row][col])
#
print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
#

