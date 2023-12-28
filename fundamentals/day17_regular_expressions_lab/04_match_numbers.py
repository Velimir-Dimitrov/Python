import re
numbers = input()
valid_filter = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
valid_numbers = re.finditer(valid_filter, numbers)
for number in valid_numbers:
    print(number.group(), end=" ")