import re
text = input()
filter_numbers = r"[0-9]+"
while text:
    numbers = re.findall(filter_numbers, text)
    if numbers:
        print(*numbers, end=" ")
    text = input()