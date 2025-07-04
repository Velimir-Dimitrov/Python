list_of_numbers = [int(num) for num in input().split()]

for index in range(len(list_of_numbers) -1):
    current_num = list_of_numbers[index]
    for compare_idx in range(index, len(list_of_numbers)):
        if current_num > list_of_numbers[compare_idx]:
            current_num = list_of_numbers[compare_idx]
            list_of_numbers[compare_idx], list_of_numbers[index] = list_of_numbers[index], list_of_numbers[compare_idx]
print(*list_of_numbers)


# # Training recursive solution
# def recursive_selection_sort(arr, index=0):
#     if index == len(arr) - 1:
#         return
#
#     min_index = index
#
#     for current_index in range(index + 1, len(arr)):
#         if arr[current_index] < arr[min_index]:
#             min_index = current_index
#     arr[index], arr[min_index] = arr[min_index], arr[index]
#
#     recursive_selection_sort(arr, index + 1)
#
# recursive_selection_sort(list_of_numbers)


# # Inputs
# 4 5 3 2 1
# 5 3 4 2 1
# 24 9 80 41 66

