def reverse_array(idx, array_input):
    if idx == len(array_input) // 2:
        return
    swap_idx = len(array_input) - 1 - idx
    array_input[idx], array_input[swap_idx] = array_input[swap_idx], array_input[idx]
    reverse_array(idx + 1, array_input)

array_input = input().split()
reverse_array(0, array_input)
print(" ".join(array_input))


# # Input
# 1 2 3 4 5 6


# # Alternative solutions
#
# def reverse_array(array, index, reversed_array):
#     if index < -(len(array)):
#         return ' '.join(reversed_array)
#     reversed_array.append(array[index])
#     return reverse_array(array, index - 1, reversed_array)

# def reverse_array(array, index=0):
#     if index == len(array):
#         return
#     reverse_array(array, index + 1)
#     print(array[index], end=' ')
#