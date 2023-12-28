def sort_ascending_order(some_list):
    return sorted(some_list)


string_with_numbers = input().split()
list_with_int = [int(x) for x in string_with_numbers]
print(sort_ascending_order(list_with_int))