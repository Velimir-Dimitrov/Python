def is_it_in(list1, list2):
    result = []
    for word1 in list1:
        for word2 in list2:
            if word1 in word2:
                result.append(word1)
                break
    return result


sequence_one = input().split(", ")
sequence_two = input().split(", ")
print(is_it_in(sequence_one,sequence_two))