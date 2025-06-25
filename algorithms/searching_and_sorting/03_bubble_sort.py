list_of_numbers = [int(num) for num in input().split()]
is_sorted = False
counter = 0

# While loop solution
while not is_sorted:
    is_sorted = True

    for index in range(1, len(list_of_numbers) - counter):
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            list_of_numbers[index - 1], list_of_numbers[index] = list_of_numbers[index], list_of_numbers[index - 1]
            is_sorted = False
    counter += 1

# # For loop solution
# for idx1 in range(len(list_of_numbers)):
#     for idx2 in range(1, len(list_of_numbers) - idx1):
#         if list_of_numbers[idx2 - 1] > list_of_numbers[idx2]:
#             list_of_numbers[idx2 - 1], list_of_numbers[idx2] = list_of_numbers[idx2], list_of_numbers[idx2 - 1]


print(*list_of_numbers)


# # Example inputs
# 5 4 3 2 1 0
# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43
