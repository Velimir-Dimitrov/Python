def nested_loop_recursion(idx, array):
    if idx == len(array):
        return print(*array)

    for num in range(1, len(array) + 1):
        array[idx] = num
        nested_loop_recursion(idx + 1, array)


array = [0 for _ in range(int(input()))]
nested_loop_recursion(0, array)

# # Inputs
# 2
# 3