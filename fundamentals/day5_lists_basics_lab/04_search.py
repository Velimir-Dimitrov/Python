number_of_strings = int(input())
special_string = input()
string_list = []
for string in range(number_of_strings):
    current_string = input()
    string_list.append(current_string)
print(string_list)

for index in range(len(string_list) - 1, -1, -1):
    element = string_list[index]
    if special_string not in element:
        string_list.remove(element)
print(string_list)
