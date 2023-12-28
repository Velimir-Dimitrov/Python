total_time = input().split()
finish_line = len(total_time) // 2
left_racer = []
right_racer = []

for index_left in range(finish_line):
    temp_lef = 0
    if int(total_time[index_left]) == 0:
        temp_lef += (sum(left_racer) * 0.8)
        left_racer.clear()
        left_racer.append(temp_lef)
        continue
    left_racer.append(int(total_time[index_left]))

for index_right in range(len(total_time) - 1, finish_line, -1):
    temp_right = 0
    if int(total_time[index_right]) == 0:
        temp_right += (sum(right_racer) * 0.8)
        right_racer.clear()
        right_racer.append(temp_right)
        continue
    right_racer.append(int(total_time[index_right]))

if sum(left_racer) < sum(right_racer):
    print(f"The winner is left with total time: {sum(left_racer):.1f}")
else:
    print(f"The winner is right with total time: {sum(right_racer):.1f}")
