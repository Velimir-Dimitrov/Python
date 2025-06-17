def array_sum(list_of_numbers, list_index):
    if list_index == len(list_of_numbers) - 1:
        return list_of_numbers[list_index]
    return list_of_numbers[list_index] + array_sum(list_of_numbers, list_index + 1)


nums = [int(num) for num in input().split()]

print(array_sum(nums, 0))







