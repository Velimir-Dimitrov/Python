string_with_repeating_chars = input()
new_string = ""

while string_with_repeating_chars:
    new_string += string_with_repeating_chars[0]
    strip_string = new_string[-1]
    string_with_repeating_chars = string_with_repeating_chars.lstrip(strip_string)
print(new_string)

# main_string = input()
# for pos, letter in enumerate(range(len(main_string) - 1), 1):
#     if main_string[letter] != main_string[pos]:
#         print(main_string[letter], end="")
#
# print(main_string[-1])