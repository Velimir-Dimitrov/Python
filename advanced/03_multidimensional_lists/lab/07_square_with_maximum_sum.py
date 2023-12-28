rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]

biggest_sum = float('-inf')
biggest_sum_location = []

for row in range(rows - 1):
    for col in range(columns - 1):
        first_line_num1 = matrix[row][col]
        first_line_num2 = matrix[row][col + 1]
        second_line_num1 = matrix[row + 1][col]
        second_line_num2 = matrix[row + 1][col + 1]
        current_sum = first_line_num1 + first_line_num2 + second_line_num1 + second_line_num2
        if biggest_sum < current_sum:
            biggest_sum = current_sum
            biggest_sum_location = [[first_line_num1, first_line_num2], [second_line_num1, second_line_num2]]
print(*biggest_sum_location[0])
print(*biggest_sum_location[1])
print(biggest_sum)