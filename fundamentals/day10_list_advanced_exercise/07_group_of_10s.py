def group_sort(some_list, some_group):
    return [num for num in some_list if num <= some_group]


numbers_list = [int(num) for num in input().split(", ")]
group = 10

while numbers_list:
    list_of_numbers = group_sort(numbers_list, group)
    numbers_list = [num for num in numbers_list if num not in list_of_numbers]
    print(f"Group of {group}'s: {list_of_numbers}")
    group += 10
    list_of_numbers = []

