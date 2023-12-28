import re
numbers = input()
phone_filter = r"\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b"
phone_numbers = re.findall(phone_filter, numbers)
print(*phone_numbers, sep=", ")