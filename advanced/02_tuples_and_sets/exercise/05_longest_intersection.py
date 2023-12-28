number_of_lines = int(input())
longest_range = set()

for _ in range(number_of_lines):
    range_numbers = input().split("-")
    current_range = []
    for interval in range(2):
        start_num, end_num = range_numbers[interval].split(",")
        current_set = set()
        for num in range(int(start_num), int(end_num) + 1):
            current_set.add(num)
        current_range.append(current_set)
    current_range = current_range[0].intersection(current_range[1])
    if len(current_range) > len(longest_range):
        longest_range = current_range
longest_range_str = ", ".join([str(el) for el in longest_range])
print(f"Longest intersection is [{longest_range_str}] with length {len(longest_range)}")
