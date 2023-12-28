import re
number_of_strings = int(input())
pattern = r"!([A-Z][a-z]{3,})!:\[([A-Za-z]{8,})]"


for string in range(number_of_strings):
    current_string = input()
    string_to_print = ""
    found_match = re.match(pattern, current_string)
    if found_match:
        filtered_command = found_match.group(1)
        filtered_string = found_match.group(2)
        string_to_print += f"{filtered_command}:"
        for el in found_match.group(2):
            char_num = ord(el)
            string_to_print += f" {char_num}"
        print(string_to_print)
    else:
        print("The message is invalid")

