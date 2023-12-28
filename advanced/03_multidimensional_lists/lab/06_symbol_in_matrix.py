matrix = [[el for el in input()] for row in range(int(input()))]
searched_symbol = input()

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == searched_symbol:
            print(f"({row}, {col})")
            exit()
print(f"{searched_symbol} does not occur in the matrix")
