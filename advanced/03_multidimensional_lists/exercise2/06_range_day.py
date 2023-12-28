def are_coordinates_valid(row, column, matrix_length):
    return 0 <= row < matrix_length and 0 <= column < matrix_length


shooting_field = [[x for x in input().split()] for row in range(5)]
shooter_position = [[row, col] for col in range(5) for row in range(5) if shooting_field[row][col] == "A"]
shooter_position = shooter_position[0]
targets = [[row, col] for col in range(5) for row in range(5) if shooting_field[row][col] == "x"]
shot_targets = []

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

number_of_commands = int(input())

for _ in range(number_of_commands):
    if not targets:
        break
    command = input().split()
    action = command[0]
    direction = command[1]
    direction_row, direction_col = directions[direction]
    shooter_row, shooter_col = shooter_position

    if action == "shoot":
        steps = 1
        while True:

            new_row = direction_row * steps + shooter_row
            new_col = direction_col * steps + shooter_col
            if not are_coordinates_valid(new_row, new_col, len(shooting_field)):
                break
            if shooting_field[new_row][new_col] == 'x':
                shot_targets.append([new_row, new_col])
                targets.remove([new_row, new_col])
                shooting_field[new_row][new_col] = '.'
                break
            steps += 1
    elif action == "move":
        steps = int(command[2])
        new_row = direction_row * steps + shooter_row
        new_col = direction_col * steps + shooter_col
        validity_check = are_coordinates_valid(new_row, new_col, len(shooting_field))

        if validity_check and shooting_field[new_row][new_col] == '.':
            shooting_field[shooter_row][shooter_col], shooting_field[new_row][new_col] = \
                shooting_field[new_row][new_col], shooting_field[shooter_row][shooter_col]
            shooter_position = [new_row, new_col]

if targets:
    print(f"Training not completed! {len(targets)} targets left.")
else:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
print(*shot_targets, sep='\n')
