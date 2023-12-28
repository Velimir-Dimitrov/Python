def find_free_chairs_in(rooms: int):
    total_chairs = 0
    total_visitors = 0
    for room in range(rooms):
        chairs, visitors = input().split(" ")
        total_chairs += int(len(chairs))
        total_visitors += int(visitors)
        if int(len(chairs)) < int(visitors):
            diff = abs(int(len(chairs)) - int(visitors))
            print(f"{diff} more chairs needed in room {room + 1}")

    return total_chairs - total_visitors


number_of_rooms = int(input())
total_free_chairs = find_free_chairs_in(number_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")


