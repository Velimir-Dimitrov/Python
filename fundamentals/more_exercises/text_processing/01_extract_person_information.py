def find_name(string):
    name_start_index = string.find("@")
    name_end_index = string.find("|")
    return string[name_start_index+1:name_end_index]


def find_age(string):
    age_start_index = string.find("#")
    age_end_index = string.find("*")
    return string[age_start_index+1:age_end_index]


number_of_lines = int(input())

for line in range(number_of_lines):
    string_line = input()
    name = find_name(string_line)
    age = find_age(string_line)
    print(f"{name} is {age} years old.")
