n, m = [int(x) for x in input().split()]


neighborhood_matrix = [list(input()) for row in range(n)]
delivery_boy = [[row, col] for col in range(m) for row in range(n) if neighborhood_matrix[row][col] == "B"][0]
locations = ['B', 'A', 'R', 'P']

current_boy_location = delivery_boy.copy()
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()
    direction_row, direction_col = directions[command]
    boy_row, boy_col = current_boy_location
    if neighborhood_matrix[boy_row][boy_col] == "-" and neighborhood_matrix[boy_row][boy_col] not in locations:
        neighborhood_matrix[boy_row][boy_col] = '.'
    new_row = direction_row + boy_row
    new_col = direction_col + boy_col
    if not (0 <= new_row < n and 0 <= new_col < m):
        print("The delivery is late. Order is canceled.")
        initial_row, initial_cow = delivery_boy
        neighborhood_matrix[initial_row][initial_cow] = " "
        break
    elif neighborhood_matrix[new_row][new_col] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        neighborhood_matrix[new_row][new_col] = "R"
        current_boy_location = [new_row, new_col]
        continue
    elif neighborhood_matrix[new_row][new_col] == "*":
        continue
    elif neighborhood_matrix[new_row][new_col] == "A":
        neighborhood_matrix[new_row][new_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break
    current_boy_location = [new_row, new_col]

[print(''.join(neighborhood_matrix[row])) for row in range(n)]

