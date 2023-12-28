n = int(input())

fishing_area = [list(input()) for row in range(n)]
ship_position = [[row, col] for col in range(n) for row in range(n) if fishing_area[row][col] == "S"][0]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

QUOTA = 20
collected_fish = 0

while True:
    command = input()
    if command == "collect the nets":
        break
    direction_row, direction_col = directions[command]
    ship_row, ship_col = ship_position
    new_row = direction_row + ship_row
    new_col = direction_col + ship_col
    if not 0 <= new_row < n:
        new_row = n - 1 if 0 > new_row else 0
    elif not 0 <= new_col < n:
        new_col = n - 1 if 0 > new_col else 0
    if fishing_area[new_row][new_col].isdigit():
        collected_fish += int(fishing_area[new_row][new_col])
    elif fishing_area[new_row][new_col] == "W":
        collected_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{new_row},{new_col}]")
        exit()

    fishing_area[ship_row][ship_col] = "-"
    fishing_area[new_row][new_col] = "S"
    ship_position = [new_row, new_col]

if collected_fish >= QUOTA:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - collected_fish} tons of fish more.")
if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")
[print(''.join(fishing_area[row])) for row in range(n)]