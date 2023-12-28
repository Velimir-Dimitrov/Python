def chars_between(char_start, char_end):
    chars_between_list = []
    for dec in range(ord(char_start)+1, ord(char_end)):
        chars_between_list.append(chr(dec))
    return " ".join(chars_between_list)


char1 = input()
char2 = input()
print(chars_between(char1, char2))
