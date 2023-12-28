number_of_lines = int(input())
even_numbers_set = set()
odd_numbers_set = set()


for row in range(1, number_of_lines + 1):
    current_name = input()
    element_sum = 0
    for el in current_name:
        element_sum += ord(el)
    name_result = element_sum // row
    if name_result % 2 == 0:
        even_numbers_set.add(name_result)
    else:
        odd_numbers_set.add(name_result)

even_sum = sum(even_numbers_set)
odd_sum = sum(odd_numbers_set)

if odd_sum == even_sum:
    union_values = even_numbers_set.union(odd_numbers_set)
    print(*union_values, sep=", ")
elif odd_sum > even_sum:
    diff_values = odd_numbers_set.difference(even_numbers_set)
    print(*diff_values, sep=", ")
elif odd_sum < even_sum:
    symmetric_diff_values = even_numbers_set.symmetric_difference(odd_numbers_set)
    print(*symmetric_diff_values, sep=", ")