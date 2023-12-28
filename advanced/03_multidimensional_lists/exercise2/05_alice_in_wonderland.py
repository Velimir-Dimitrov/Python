n = int(input())
wonderland = [[x for x in input().split()] for row in range(n)]
alice_location = [[row, col] for col in range(n) for row in range(n) if wonderland[row][col] == "A"]

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

tea_collected = 0
party_not_attended = False

while True:
    if tea_collected >= 10:
        party_not_attended = False
        break
    direction = input()
    alice_row = alice_location[0][0]
    alice_col = alice_location[0][1]
    move_row = moves[direction][0]
    move_col = moves[direction][1]
    new_location_row = alice_row + move_row
    new_location_col = alice_col + move_col
    wonderland[alice_row][alice_col] = "*"
    if not (0 <= new_location_row < n and 0 <= new_location_col < n):
        party_not_attended = True
        break
    elif wonderland[new_location_row][new_location_col] == "R":
        party_not_attended = True
        wonderland[new_location_row][new_location_col] = "*"
        break
    else:
        if wonderland[new_location_row][new_location_col].isdigit():
            tea_collected += int(wonderland[new_location_row][new_location_col])
        wonderland[new_location_row][new_location_col] = "*"
        alice_location = [[new_location_row, new_location_col]]
if party_not_attended:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*wonderland[row]) for row in range(n)]