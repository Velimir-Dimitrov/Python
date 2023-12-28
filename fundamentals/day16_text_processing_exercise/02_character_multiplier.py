strings_line = input().split()
string_one = ""
string_two = ""
total_sum = 0

for string in strings_line:
    if len(string_one) < len(string):
        string_two = string_one
        string_one = string
    else:
        string_two = string


for index in range(len(string_one)):
    if index <= len(string_two) - 1:
        total_sum += ord(string_one[index]) * ord(string_two[index])
    else:
        total_sum += ord(string_one[index])
print(total_sum)

