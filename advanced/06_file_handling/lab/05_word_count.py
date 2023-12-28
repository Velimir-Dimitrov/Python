import os
import re

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

key_words_path = os.path.join(WORKING_DIR, "words.txt")
key_words_file = open(key_words_path, "w")
key_words_file.write(input())

text_path = os.path.join(WORKING_DIR, "input.txt")
text_file = open(text_path, "w")
text_string = ""
while True:
    line = input()
    if line == '':
        break
    text_string += line
text_file.write(text_string)
key_words_file.close()
text_file.close()

key_words_file = open(key_words_path, 'r')
text_file = open(text_path, 'r')

key_words = key_words_file.read().split()
text = text_file.read().lower()

found_words_dict = {}
for word in key_words:
    pattern = rf'\b{word}\b'
    result = re.findall(pattern, text)
    found_words_dict[word] = len(result)

[print(f"{key} - {value}") for key, value in sorted(found_words_dict.items(), key=lambda kvp: -kvp[1])]

key_words_file.close()
text_file.close()









