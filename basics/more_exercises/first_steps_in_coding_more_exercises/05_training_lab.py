room_length = float(input()) * 100
room_width = float(input()) * 100

real_room_width = room_width - 100
numbers_of_desks_per_row = real_room_width // 70

numbers_of_rows = room_length // 120
room_capacity = int(numbers_of_desks_per_row * numbers_of_rows) - 3
print(room_capacity)

