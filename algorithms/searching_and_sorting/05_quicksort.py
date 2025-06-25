def quick_sort(start, end, arr):
    if start >= end:
        return

    pivot= start
    left = start + 1
    right =  end

    while left <= right:
        if arr[left] > arr[pivot] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[pivot] >= arr[left]:
            left += 1
        if arr[pivot] <= arr[right]:
            right -= 1
    arr[right], arr[pivot] = arr[pivot], arr[right]

    quick_sort(start, right - 1, arr)
    quick_sort(right + 1, end, arr)


list_of_numbers = [int(num) for num in input().split()]
quick_sort(0, len(list_of_numbers) -1, list_of_numbers)

print(*list_of_numbers)


# # Example inputs
# 5 4 3 2 1 0
# 4 1 8 9 3 8 1 9 4