string = input()
char_dict = {}

for char in string:
    if char == " ":
        continue
    elif char not in char_dict:
        char_dict[char] = 0
    char_dict[char] += 1

[(print(f"{key} -> {occurrences}")) for key, occurrences in char_dict.items()]
