string_num = input().split()
string_words = input()

list_char = [letter for letter in string_words]
word = []

for sequence in string_num:
    letter_index = 0
    for num in sequence:
        letter_index += int(num)
    if letter_index >= len(list_char):
        letter_index -= len(list_char)
    word.append(list_char.pop(letter_index))
print("".join(word))
