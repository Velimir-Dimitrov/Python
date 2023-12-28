string_numbers = input().split(", ")
index_list = [index for index in range(len(string_numbers)) if int(string_numbers[index]) % 2 == 0]
print(index_list)