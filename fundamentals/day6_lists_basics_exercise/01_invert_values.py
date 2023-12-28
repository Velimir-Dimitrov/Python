string_of_numbers = input().split()
opposite_num_list = []
for current_num in string_of_numbers:
    opposite_num_list.append(-int(current_num))
print(opposite_num_list)