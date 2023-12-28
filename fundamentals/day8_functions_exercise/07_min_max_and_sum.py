def check_min_num(some_list):
    return min(some_list)


def check_max_num(some_list):
    return max(some_list)


def calculate_the_sum(some_list):
    return sum(some_list)


string_with_num = input().split()
list_with_int = [int(x) for x in string_with_num]
minimum_number = check_min_num(list_with_int)
maximum_number = check_max_num(list_with_int)
sum_of_all_numbers = calculate_the_sum(list_with_int)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")