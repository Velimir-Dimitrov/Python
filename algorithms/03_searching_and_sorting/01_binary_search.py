def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
    return -1


list_of_nums = [int(num) for num in input().split()]
searched_num = int(input())
print(binary_search(list_of_nums, searched_num))

# # Recursive version
# def binary_search(start_index, end_index, arr, target):
#     if start_index > end_index:
#         return -1
#     mid = (start_index + end_index) // 2
#     if arr[mid] == target:
#         return mid
#     if arr[mid] < target:
#         return binary_search(mid + 1, end_index, arr, target)
#     elif arr[mid] > target:
#         return binary_search(start_index, mid - 1, arr, target)
#
#
# list_of_nums = [int(num) for num in input().split()]
# searched_num = int(input())
# start_index = 0
# end_index = len(list_of_nums) - 1
#
# print(binary_search(start_index, end_index, list_of_nums, searched_num))


# # Input
# 1 2 3 4 5
# 1
# # Output
# # 0
#
# -1 0 1 2 4
# 1
# # Output
# # 1