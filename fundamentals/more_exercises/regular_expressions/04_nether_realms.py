import re
string_with_demons = input().replace(" ", "").split(",")
char_filter = r"[^0-9\+\-\*\/\.]"
num_filter = r"([-+]?\d+(\.\d+)?)"
divide_multiple_filter = r"[*/]"
demon_dict = {}

for demon in string_with_demons:
    health = 0
    damage = 0
    list_of_chars = re.findall(char_filter, demon)
    list_of_char_codes = [ord(char) for char in list_of_chars]
    health += sum(list_of_char_codes)
    list_of_nums = re.findall(num_filter, demon)
    damage += sum([float(num[0]) for num in list_of_nums])
    list_of_commands = re.findall(divide_multiple_filter, demon)
    for command in list_of_commands:
        if command == "*":
            damage *= 2
        elif command == "/":
            damage /= 2
    demon_dict[demon] = [health, damage]

sorted_demon_dict = sorted(demon_dict.keys())
for demon in sorted_demon_dict:
    print(f"{demon} - {demon_dict[demon][0]} health, {demon_dict[demon][1]:.2f} damage")