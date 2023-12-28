words = input().lower().split(" ")
count = 0
words_dict = dict.fromkeys(words, count)

for word in words:
    words_dict[word] += 1

[print(key, end=" ") for key in words_dict if words_dict[key] % 2 != 0]
