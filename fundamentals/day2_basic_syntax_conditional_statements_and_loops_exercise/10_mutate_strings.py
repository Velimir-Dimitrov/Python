word1 = input()
word2 = input()
first_part = ''
last_word = ''

for i in range(len(word2)):
    second_part = ''
    first_part += word2[i]
    for x in range(len(word1)):
        if i < x:
            second_part += word1[x]
        else:
            continue
    current_word = first_part + second_part
    if current_word == last_word or current_word == word1:
        continue
    else:
        print(current_word)
        last_word = current_word
