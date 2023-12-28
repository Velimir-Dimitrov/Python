def fill_the_box(*args):
    box_height, box_length, box_width, cubes_list = args[0], args[1], args[2], args[3:]
    box_volume = int(box_height) * int(box_length) * int(box_width)
    total_cubes = 0
    for index in range(len(cubes_list)):
        if cubes_list[index] == "Finish":
            break
        cubes = int(cubes_list[index])
        total_cubes += cubes
    if box_volume > total_cubes:
        return f"There is free space in the box. You could put {box_volume - total_cubes} more cubes."
    return f"No more free space! You have {total_cubes - box_volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))