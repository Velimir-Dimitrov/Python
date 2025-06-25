def merge_arrays(left, right):
    sorted_array = []

    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_array.append(left[left_idx])
            left_idx += 1
        else:
            sorted_array.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        sorted_array.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        sorted_array.append(right[right_idx])
        right_idx += 1

    return sorted_array


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    left = arr[:mid_idx]
    right = arr[mid_idx:]

    return merge_arrays(merge_sort(left), merge_sort(right))


list_of_numbers = [int(num) for num in input().split()]
result = merge_sort(list_of_numbers)
print(*result)


# # Example inputs
# 5 4 3 2 1 0
# 4 1 8 9 3 8 1 9 4