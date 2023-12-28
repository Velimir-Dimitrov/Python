def location_validity_check(row, column, matrix_len):
    return 0 <= new_row < size and 0 <= new_col < size


def naughty_gifting(row, column, matrix_locations):
    return matrix_locations.remove([row, column])


def nice_gifting(row, column, matrix_location):
    matrix_location.remove([row, column])


number_of_presents = int(input())
size = int(input())
neighborhood = [[x for x in input().split()] for row in range(size)]


santa_location = [[row, col] for col in range(size) for row in range(size) if neighborhood[row][col] == "S"][0]
naughty_kids_locations = [[row, col] for col in range(size) for row in range(size) if neighborhood[row][col] == "X"]
nice_kids_locations = [[row, col] for col in range(size) for row in range(size) if neighborhood[row][col] == "V"]
cookies_locations = [[row, col] for col in range(size) for row in range(size) if neighborhood[row][col] == "C"]

directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0),}

count_nice_kids = 0

while True:
    command = input()
    if command == "Christmas morning":
        break

    move_row, move_col = directions[command]
    santa_row, santa_col = santa_location
    new_row = move_row + santa_row
    new_col = move_col + santa_col
    if location_validity_check(new_row, new_col, size):
        neighborhood[santa_row][santa_col] = "-"
        neighborhood[new_row][new_col] = 'S'
        santa_location = [new_row, new_col]
        if [new_row, new_col] in naughty_kids_locations:
            naughty_gifting(new_row, new_col, naughty_kids_locations)
            continue
        elif [new_row, new_col] in nice_kids_locations:
            nice_gifting(new_row, new_col, nice_kids_locations)
            number_of_presents -= 1
            count_nice_kids += 1
        elif [new_row, new_col] in cookies_locations:
            cookies_locations.remove([new_row, new_col])
            for direction, move in directions.items():
                if number_of_presents == 0 or not nice_kids_locations:
                    break
                step_row, step_col = move
                cookie_row = new_row + step_row
                cookie_col = new_row + step_col

                if neighborhood[cookie_row][cookie_col] == '-':
                    continue
                elif [cookie_row, cookie_col] in naughty_kids_locations:
                    naughty_gifting(cookie_row, cookie_col, naughty_kids_locations)

                elif [cookie_row, cookie_col] in nice_kids_locations:
                    nice_gifting(cookie_row, cookie_col, nice_kids_locations)
                    count_nice_kids += 1
                number_of_presents -= 1
                neighborhood[cookie_row][cookie_col] = "-"
    if number_of_presents == 0 or not nice_kids_locations:
        break

if number_of_presents == 0 and nice_kids_locations:
    print("Santa ran out of presents!")
[print(*neighborhood[row]) for row in range(size)]
if not nice_kids_locations:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids_locations)} nice kid/s.")



