floors = int(input())
rooms_per_floor = int(input())

for floor in range(floors, 0, -1):

    room_type = "A" if floor % 2 else "O"

    if floor == floors:
        room_type = "L"

    for rooms in range(0, rooms_per_floor):
        print(f'{room_type}{floor}{rooms}', end = " ")
    print()



