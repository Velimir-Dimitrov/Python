string_with_numbers = [el.split() for el in input().split('|')]
flatten_list = []
for row in range(len(string_with_numbers)-1, -1, -1):
    flatten_list += string_with_numbers[row]
print(*flatten_list)