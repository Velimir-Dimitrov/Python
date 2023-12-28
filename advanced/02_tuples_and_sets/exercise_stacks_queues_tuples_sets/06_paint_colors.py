from collections import deque

substrings = deque(input().split())
found_colors = []

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {"orange": ['red', 'yellow'],
                    "purple": ['red', 'blue'],
                    "green": ['yellow', 'blue']}

while substrings:
    first_part = substrings.popleft()
    second_part = substrings.pop() if substrings else ''
    current_string_one = first_part + second_part
    current_string_two = second_part + first_part
    if current_string_one in main_colors or current_string_one in secondary_colors:
        found_colors.append(current_string_one)
    elif current_string_two in main_colors or current_string_two in secondary_colors:
        found_colors.append(current_string_two)
    else:
        if len(first_part) > 1:
            substrings.insert(len(substrings) // 2, first_part[:-1], )
        if len(second_part) > 1:
            substrings.insert(len(substrings) // 2, second_part[:-1], )

for color in found_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in found_colors:
                found_colors.remove(color)
                break

print(found_colors)